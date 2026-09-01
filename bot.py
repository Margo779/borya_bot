import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Веб-сервер для удержания порта на Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Borya is alive!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHandler)
    server.serve_forever()

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

import asyncio
import random
from datetime import date, datetime, timedelta
import aiohttp
import aiosqlite
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    FSInputFile,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    LabeledPrice,
    PreCheckoutQuery,
)

from predictions import PAID_PREDICTIONS

# === КОНФИГУРАЦИЯ ===
BOT_TOKEN = "8820100460:AAGS4-haGYH-W-vg7xHkdrJI3HWcKMPFPqg"
CRYPTO_BOT_TOKEN = "628976:AA2wMF2x654qMgbneE74cbBS1RAVyuCJyY9"

VIDEO_PLAY_TIME = 9.5
CACHED_VIDEO_ID = None
DB_NAME = "borya_bot.db"

# Цены
PRICE_QUESTION_STARS = 50   
PRICE_RENT_STARS = 250      
PRICE_QUESTION_USDT = 1.1   
PRICE_RENT_USDT = 5.5       

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class FortuneForm(StatesGroup):
    waiting_for_single_question = State()

FREE_PREDICTIONS = [
    "Сегодня отличный день для новых начинаний! Доверьтесь интуиции и делайте первый шаг.",
    "Вас ждет приятное известие во второй половине дня. Будьте внимательны к мелочам!",
    "Не торопите события — всё сложится лучшим образом само собой.",
    "Интуиция сегодня — ваш главный советчик. Слушайте свое сердце.",
    "Скоро перед вами откроется новая интересная возможность!"
]

# === БАЗА ДАННЫХ ===
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                last_free_date TEXT,
                rent_expire_date TEXT,
                last_prediction TEXT
            )
        """)
        await db.commit()

async def get_user_data(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT last_free_date, rent_expire_date, last_prediction FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            if not row:
                await db.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
                await db.commit()
                return None, None, None
            return row

async def is_rent_active(user_id: int) -> bool:
    _, rent_expire_str, _ = await get_user_data(user_id)
    if rent_expire_str:
        expire_dt = datetime.fromisoformat(rent_expire_str)
        return datetime.now() < expire_dt
    return False

async def set_rent(user_id: int, days: int = 7):
    expire_dt = datetime.now() + timedelta(days=days)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET rent_expire_date = ? WHERE user_id = ?", (expire_dt.isoformat(), user_id))
        await db.commit()
    return expire_dt

async def get_unique_prediction(user_id: int) -> str:
    _, _, last_text = await get_user_data(user_id)
    available = [p for p in PAID_PREDICTIONS if p != last_text]
    if not available:
        available = PAID_PREDICTIONS
    chosen = random.choice(available)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET last_prediction = ? WHERE user_id = ?", (chosen, user_id))
        await db.commit()
    return chosen

# === CRYPTOBOT API ===
async def create_crypto_invoice(amount: float, description: str, payload: str):
    url = "https://pay.crypt.bot/api/createInvoice"
    headers = {"Crypto-Pay-API-Token": CRYPTO_BOT_TOKEN}
    data = {
        "asset": "USDT",
        "amount": str(amount),
        "description": description,
        "payload": payload
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as resp:
            result = await resp.json()
            if result.get("ok"):
                return result["result"]["pay_url"], result["result"]["invoice_id"]
            return None, None

async def check_crypto_invoice_status(invoice_id: int) -> bool:
    url = "https://pay.crypt.bot/api/getInvoices"
    headers = {"Crypto-Pay-API-Token": CRYPTO_BOT_TOKEN}
    params = {"invoice_ids": invoice_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as resp:
            result = await resp.json()
            if result.get("ok") and result["result"]["items"]:
                status = result["result"]["items"][0]["status"]
                return status == "paid"
    return False

# === ФОНОВЫЙ АВТОПЕРЕОДЧИК ОПЛАТЫ ===
async def background_crypto_checker(chat_id: int, user_id: int, invoice_id: int, payment_type: str, state: FSMContext):
    for _ in range(90):
        await asyncio.sleep(10)
        if await check_crypto_invoice_status(invoice_id):
            if payment_type == "rent":
                expire_dt = await set_rent(user_id, days=7)
                await bot.send_message(
                    chat_id=chat_id,
                    text=f"👑 **Оплата получена! Аренда Бори активирована** до {expire_dt.strftime('%d.%m.%Y %H:%M')}!\n\n"
                         "🔮 Теперь любые ваши сообщения в чат будут автоматически обрабатываться Борей бесплатно!",
                    parse_mode="Markdown"
                )
            elif payment_type == "question":
                await state.set_state(FortuneForm.waiting_for_single_question)
                await bot.send_message(
                    chat_id=chat_id,
                    text="✅ **Оплата через CryptoBot получена!**\n\n✍️ Теперь напишите ваш вопрос Боре в чат:",
                    parse_mode="Markdown"
                )
            return

# === АНИМАЦИЯ БОРЯ ===
async def play_borya_and_reveal(chat_id: int, final_text: str):
    global CACHED_VIDEO_ID
    video_to_send = CACHED_VIDEO_ID if CACHED_VIDEO_ID else FSInputFile("borya.mp4")
    
    video_msg = await bot.send_video(
        chat_id=chat_id,
        video=video_to_send,
        caption="🔮 *Боря всматривается в судьбу и тянется за свитком...*",
        parse_mode="Markdown",
        supports_streaming=True
    )

    if not CACHED_VIDEO_ID and video_msg.video:
        CACHED_VIDEO_ID = video_msg.video.file_id

    await asyncio.sleep(VIDEO_PLAY_TIME)

    try:
        await bot.delete_message(chat_id=chat_id, message_id=video_msg.message_id)
    except Exception:
        pass

    await bot.send_photo(
        chat_id=chat_id,
        photo=FSInputFile("borya.jpg"),
        caption=final_text,
        parse_mode="Markdown"
    )

# === ГЛАВНОЕ МЕНЮ (Универсальная функция) ===
async def send_main_menu(message_or_callback, text_prefix=""):
    user_id = message_or_callback.from_user.id
    await get_user_data(user_id)
    
    rent_status = ""
    if await is_rent_active(user_id):
        _, rent_expire_str, _ = await get_user_data(user_id)
        expire_dt = datetime.fromisoformat(rent_expire_str)
        rent_status = f"\n\n👑 *У вас активна аренда Бори до {expire_dt.strftime('%d.%m.%Y %H:%M')}!* Все вопросы бесплатны."

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔮 Задать вопрос", callback_data="pay_question_menu")],
        [InlineKeyboardButton(text="👑 Аренда на неделю", callback_data="pay_rent_menu")],
        [InlineKeyboardButton(text="🎁 Бесплатный свиток дня", callback_data="free_scroll")]
    ])
    
    text = f"{text_prefix}Чик-чирик! 🦜 Я попугай Боря.\nВыберите вариант взаимодействия:{rent_status}"
    
    # Если это callback (нажатие на кнопку), редактируем текущее сообщение, чтобы оно не дублировалось бесконечно
    if isinstance(message_or_callback, types.CallbackQuery):
        try:
            await message_or_callback.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
        except Exception:
            await message_or_callback.message.answer(text, reply_markup=kb, parse_mode="Markdown")
    else:
        await message_or_callback.answer(text, reply_markup=kb, parse_mode="Markdown")

@dp.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await send_main_menu(message)

@dp.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await send_main_menu(callback)

@dp.callback_query(F.data == "free_scroll")
async def send_free_fortune(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    user_id = callback.from_user.id
    today_str = date.today().isoformat()

    last_free_date, _, _ = await get_user_data(user_id)

    if last_free_date == today_str:
        await callback.message.answer(
            "Чик-чирик! 🦜 На сегодня ваш бесплатный свиток уже получен.\n\n"
            "Приходите завтра за новым предсказанием или выберите платный сеанс."
        )
        return

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET last_free_date = ? WHERE user_id = ?", (today_str, user_id))
        await db.commit()

    random_text = random.choice(FREE_PREDICTIONS)
    caption = f"📜 **Ваше предсказание дня:**\n\n{random_text}"
    await play_borya_and_reveal(callback.message.chat.id, caption)


# ==========================================
# СЦЕНАРИЙ 1: АРЕНДА
# ==========================================

@dp.callback_query(F.data == "pay_rent_menu")
async def pay_rent_menu(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"⭐️ Оплатить аренду Stars ({PRICE_RENT_STARS} ⭐️)", callback_data="pay_stars_rent")],
        [InlineKeyboardButton(text=f"💎 Оплатить аренду Криптой (${PRICE_RENT_USDT})", callback_data="pay_crypto_rent")],
        [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="main_menu")]
    ])
    await callback.message.edit_text(
        "👑 **Аренда Бори на 7 дней:**\n\nВсе вопросы и расклады в течение недели станут абсолютно бесплатными!\nВыберите способ оплаты:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "pay_stars_rent")
async def pay_stars_rent(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await bot.send_invoice(
        chat_id=user_id,
        title="👑 Аренда Бори на 7 дней",
        description="Безлимитные вопросы попугаю Боре на неделю",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="Аренда 7 дней", amount=PRICE_RENT_STARS)],
        start_parameter="borya-rent",
        payload=f"stars_rent_{user_id}"
    )

@dp.callback_query(F.data == "pay_crypto_rent")
async def pay_crypto_rent(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    pay_url, invoice_id = await create_crypto_invoice(PRICE_RENT_USDT, "Аренда Бори на 7 дней", f"crypto_rent_{user_id}")
    if pay_url:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить в CryptoBot", url=pay_url)],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="main_menu")]
        ])
        # Отправляем новым сообщением, чтобы старое меню выбора никуда не исчезало
        await callback.message.answer(
            "💎 **Счет на оплату аренды создан!**\n\n"
            "Нажмите кнопку ниже для перевода. Как только оплата пройдет, Боря **автоматически** активирует аренду прямо здесь!",
            reply_markup=kb,
            parse_mode="Markdown"
        )
        asyncio.create_task(background_crypto_checker(chat_id, user_id, invoice_id, "rent", state))
    else:
        await callback.message.answer("Ошибка создания счета. Попробуйте оплату через Telegram Stars.")


# ==========================================
# СЦЕНАРИЙ 2: РАЗОВЫЙ ПЛАТНЫЙ СЕАНС
# ==========================================

@dp.callback_query(F.data == "pay_question_menu")
async def pay_question_menu(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    
    if await is_rent_active(callback.from_user.id):
        await callback.message.edit_text(
            "👑 **У вас активна аренда!**\n\n🔮 Напишите ваш вопрос Боре прямо в чат:",
            parse_mode="Markdown"
        )
        return

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"⭐️ Оплатить Stars ({PRICE_QUESTION_STARS} ⭐️)", callback_data="pay_stars_q")],
        [InlineKeyboardButton(text=f"💎 Оплатить Криптой (${PRICE_QUESTION_USDT})", callback_data="pay_crypto_q")],
        [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="main_menu")]
    ])
    await callback.message.edit_text(
        "🔮 **Разовый платный сеанс:**\n\nВыберите удобный способ оплаты:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "pay_stars_q")
async def pay_stars_q(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await bot.send_invoice(
        chat_id=user_id,
        title="🔮 Расклад Бори",
        description="Оплата разового вопроса попугаю Боре",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="Расклад", amount=PRICE_QUESTION_STARS)],
        start_parameter="borya-q",
        payload=f"stars_q_{user_id}"
    )

@dp.callback_query(F.data == "pay_crypto_q")
async def pay_crypto_q(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id
    pay_url, invoice_id = await create_crypto_invoice(PRICE_QUESTION_USDT, "Расклад Бори", f"crypto_q_{user_id}")
    
    if pay_url:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить в CryptoBot", url=pay_url)],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="main_menu")]
        ])
        # Отправляем новым сообщением, сохраняя главное меню выше
        await callback.message.answer(
            "💎 **Счет на оплату расклада создан!**\n\n"
            "Нажмите кнопку ниже для перевода. Как только оплата пройдет, Боря **автоматически** попросит вас написать вопрос!",
            reply_markup=kb,
            parse_mode="Markdown"
        )
        asyncio.create_task(background_crypto_checker(chat_id, user_id, invoice_id, "question", state))
    else:
        await callback.message.answer("Ошибка создания счета. Попробуйте оплату через Telegram Stars.")

@dp.pre_checkout_query()
async def process_pre_checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(F.successful_payment)
async def process_successful_payment(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    payload = message.successful_payment.invoice_payload
    
    if payload.startswith("stars_rent_"):
        expire_dt = await set_rent(user_id, days=7)
        await message.answer(
            f"👑 **Оплата Stars прошла успешно! Аренда Бори активирована** до {expire_dt.strftime('%d.%m.%Y %H:%M')}!\n\n"
            "Теперь вы можете задавать любые вопросы прямо в чате бесплатно."
        )
    elif payload.startswith("stars_q_"):
        await state.set_state(FortuneForm.waiting_for_single_question)
        await message.answer(
            "✅ **Оплата Stars прошла успешно!**\n\n✍️ Теперь напишите ваш вопрос Боре в чат:",
            parse_mode="Markdown"
        )


# ==========================================
# ОБРАБОТКА ТЕКСТОВЫХ СООБЩЕНИЙ
# ==========================================

@dp.message(F.text)
async def handle_user_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    question_text = message.text
    current_state = await state.get_state()

    # СЛУЧАЙ А: У пользователя активна аренда
    if await is_rent_active(user_id):
        await state.clear()
        paid_text = await get_unique_prediction(user_id)
        caption = f"❓ **Ваш вопрос:** *{question_text}*\n\n📜 **Расклад Бори (по аренде):**\n{paid_text}"
        
        try:
            await message.reply("🔮 Боря изучает ваш вопрос...")
        except Exception:
            pass
            
        await play_borya_and_reveal(message.chat.id, caption)
        return

    # СЛУЧАЙ Б: Пользователь оплатил разовый сеанс и прислал сам вопрос
    if current_state == FortuneForm.waiting_for_single_question.state:
        await state.clear()
        paid_text = await get_unique_prediction(user_id)
        caption = f"❓ **Ваш вопрос:** *{question_text}*\n\n📜 **Расклад Бори:**\n{paid_text}"
        
        await play_borya_and_reveal(message.chat.id, caption)
        return

    # СЛУЧАЙ В: Пользователь просто пишет текст без оплаты и без аренды — показываем меню
    await send_main_menu(message, text_prefix="Чик-чирик! 🦜 Чтобы Боря сделал для вас расклад, ")


# --- ВЕБ-СЕРВЕР ДЛЯ RENDER ---
async def handle(request):
    return aiohttp.web.Response(text="Borya Bot is running!")

async def web_server():
    app = aiohttp.web.Application()
    app.router.add_get("/", handle)
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()

async def main():
    await init_db()
    asyncio.create_task(web_server())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
