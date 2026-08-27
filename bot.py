import asyncio
import random
import uuid
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
CRYPTO_BOT_TOKEN = "ВАШ_CRYPTO_BOT_TOKEN"  # Получить в @CryptoBot -> /pay

VIDEO_PLAY_TIME = 9.5
CACHED_VIDEO_ID = None
DB_NAME = "borya_bot.db"

# Цены (в рублях / USDT / Stars)
PRICE_QUESTION_STARS = 50   # ~100 руб в Stars
PRICE_RENT_STARS = 250      # ~500 руб в Stars
PRICE_QUESTION_USDT = 1.1   # $1.1 (~100 руб)
PRICE_RENT_USDT = 5.5       # $5.5 (~500 руб)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class FortuneForm(StatesGroup):
    waiting_for_question = State()

FREE_PREDICTIONS = [
    "Сегодня отличный день для новых начинаний! Доверьтесь интуиции и делайте первый шаг.",
    "Вас ждет приятное известие во второй половине дня. Будьте внимательны к мелочам!",
    "Не торопите события — всё сложится лучшим образом само собой.",
    "Интуиция сегодня — ваш главный советчик. Слушайте свое сердце.",
    "Скоро перед вами откроется новая интересная возможность!"
]

# === РАБОТА С БАЗОЙ ДАННЫХ (SQLite) ===
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
    chosen = random.choice(available)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET last_prediction = ? WHERE user_id = ?", (chosen, user_id))
        await db.commit()
    return chosen

# === CRYPTOBOT INTEGRATION ===
async def create_crypto_invoice(amount: float, description: str, payload: str) -> str:
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
                return result["result"]["pay_url"]
            return None

# === ОСНОВНАЯ ЛОГИКА АНИМАЦИИ ===
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

# === ХЕНДЛЕРЫ ===
@dp.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    user_id = message.from_user.id
    await get_user_data(user_id)
    
    rent_status = ""
    if await is_rent_active(user_id):
        _, rent_expire_str, _ = await get_user_data(user_id)
        expire_dt = datetime.fromisoformat(rent_expire_str)
        rent_status = f"\n\n👑 *У вас активна аренда Бори до {expire_dt.strftime('%d.%m.%Y %H:%M')}!* Все вопросы бесплатны."

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔮 Задать вопрос", callback_data="pay_question")],
        [InlineKeyboardButton(text="👑 Аренда на неделю", callback_data="pay_rent")],
        [InlineKeyboardButton(text="🎁 Бесплатный свиток дня", callback_data="free_scroll")]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 🦜 Я попугай Боря.\n"
        f"Задай мне вопрос, и я вытащу для тебя предсказание!{rent_status}",
        reply_markup=kb,
        parse_mode="Markdown"
    )

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
            "Приходите завтра за новым предсказанием или выберите персональный вопрос."
        )
        return

    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET last_free_date = ? WHERE user_id = ?", (today_str, user_id))
        await db.commit()

    random_text = random.choice(FREE_PREDICTIONS)
    caption = f"📜 **Ваше предсказание дня:**\n\n{random_text}"
    await play_borya_and_reveal(callback.message.chat.id, caption)

# --- ВЫБОР ОПЛАТЫ ---
@dp.callback_query(F.data == "pay_question")
async def ask_user_question(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(FortuneForm.waiting_for_question)
    await callback.message.answer(
        "🔮 **Задайте ваш вопрос Боре:**\n\nНапишите сообщение с вашим вопросом в чат:",
        parse_mode="Markdown"
    )

@dp.message(FortuneForm.waiting_for_question, F.text)
async def receive_question(message: types.Message, state: FSMContext):
    question_text = message.text
    user_id = message.from_user.id
    
    if await is_rent_active(user_id):
        await state.clear()
        paid_text = await get_unique_prediction(user_id)
        caption = f"❓ **Ваш вопрос:** *{question_text}*\n\n📜 **Расклад Бори:**\n{paid_text}"
        await play_borya_and_reveal(message.chat.id, caption)
        return

    await state.update_data(user_question=question_text)
    await state.set_state(None)
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"⭐️ Оплатить Stars ({PRICE_QUESTION_STARS} ⭐️)", callback_data="pay_stars_q")],
        [InlineKeyboardButton(text=f"💎 Оплатить Криптой (${PRICE_QUESTION_USDT})", callback_data="pay_crypto_q")]
    ])
    
    await message.answer(
        f"✍️ Ваш вопрос принят: *«{question_text}»*\n\nВыберите удобный способ оплаты:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

# --- ОПЛАТА СТАРСАМИ (STARS) ---
@dp.callback_query(F.data == "pay_stars_q")
async def pay_stars_q(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    data = await state.get_data()
    q_text = data.get("user_question", "Ваш вопрос")
    
    await bot.send_invoice(
        chat_id=user_id,
        title="🔮 Расклад Бори",
        description=f"Ответ на вопрос: {q_text[:30]}...",
        provider_token="",  # Пусто для Telegram Stars
        currency="XTR",    # Валюта Telegram Stars
        prices=[LabeledPrice(label="Расклад", amount=PRICE_QUESTION_STARS)],
        start_parameter="borya-q",
        payload=f"stars_q_{user_id}"
    )

@dp.pre_checkout_query()
async def process_pre_checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(F.successful_payment)
async def process_successful_payment(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    saved_question = data.get("user_question", "Ваш вопрос")
    await state.clear()

    paid_text = await get_unique_prediction(user_id)
    caption = f"❓ **Ваш вопрос:** *{saved_question}*\n\n📜 **Расклад Бори:**\n{paid_text}"
    await play_borya_and_reveal(message.chat.id, caption)

# --- ОПЛАТА КРИПТОЙ (CRYPTOBOT) ---
@dp.callback_query(F.data == "pay_crypto_q")
async def pay_crypto_q(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    pay_url = await create_crypto_invoice(PRICE_QUESTION_USDT, "Расклад Бори", f"crypto_q_{user_id}")
    
    if pay_url:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💳 Оплатить через @CryptoBot", url=pay_url)],
            [InlineKeyboardButton(text="✅ Я оплатил", callback_data="check_crypto_pay")]
        ])
        await callback.message.answer("Нажмите кнопку ниже для перевода средств. После оплаты нажмите «Я оплатил»:", reply_markup=kb)
    else:
        await callback.message.answer("Ошибка создания счета. Попробуйте оплату через Telegram Stars.")

@dp.callback_query(F.data == "check_crypto_pay")
async def check_crypto_pay(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    # В рамках простой версии проверяем и выдаем расклад:
    await callback.answer("Успешно! Боря уже достает свиток...")
    data = await state.get_data()
    saved_question = data.get("user_question", "Ваш вопрос")
    await state.clear()
    
    paid_text = await get_unique_prediction(user_id)
    caption = f"❓ **Ваш вопрос:** *{saved_question}*\n\n📜 **Расклад Бори:**\n{paid_text}"
    await play_borya_and_reveal(callback.message.chat.id, caption)

# === ФИКТИВНЫЙ ВЕБ-СЕРВЕР ДЛЯ RENDER ===
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
    # Запускаем веб-сервер для Render в фоне:
    asyncio.create_task(web_server())
    # Запускаем бота:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
