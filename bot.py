<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Боря гадает — предсказания от волнистого попугайчика</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yeseva+One&family=Marck+Script&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --void:#050308;
    --deep:#0c0714;
    --royal:#1c0f2e;
    --gold:#eabc5b;
    --gold-soft:#c9a25a;
    --gold-dim:rgba(234,188,91,0.35);
    --purple-1:#7a3aa8;
    --purple-2:#5d2463;
    --purple-3:#3c1442;
    --cream:#f2e9ef;
    --cream-dim:#b8a9c4;
    --tg-blue: #0088cc;
    --font-display:'Yeseva One', serif;
    --font-script:'Marck Script', cursive;
    --font-body:'PT Serif', serif;
    --font-ui:'Montserrat', sans-serif;
  }

  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{
    margin:0;
    background:
      radial-gradient(ellipse 70% 40% at 15% 0%, rgba(93,36,99,0.35), transparent 60%),
      radial-gradient(ellipse 50% 35% at 100% 10%, rgba(122,16,48,0.18), transparent 60%),
      linear-gradient(180deg, var(--void) 0%, var(--deep) 45%, var(--royal) 100%);
    color:var(--cream);
    font-family:var(--font-body);
    overflow-x:hidden;
    min-height:100vh;
    padding-bottom: 120px; 
  }
  a{color:inherit; text-decoration:none;}

  /* Header */
  header{
    position:sticky; top:0; z-index:80;
    display:flex; align-items:center; justify-content:space-between;
    padding:14px 5vw;
    background:rgba(5,3,8,0.85);
    backdrop-filter:blur(10px);
    border-bottom:1px solid rgba(234,188,91,0.14);
  }
  .logo{
    font-family:var(--font-display);
    font-size:1.3rem;
    color:var(--gold);
    display:flex; align-items:center; gap:8px;
    white-space:nowrap;
  }
  nav.desktop-nav{display:flex; gap:28px;}
  nav.desktop-nav a{
    font-family:var(--font-ui); font-size:.9rem; color:var(--cream-dim); transition:color .2s;
  }
  nav.desktop-nav a:hover{color:var(--gold);}

  .header-actions {
    display: flex; align-items: center; gap: 12px;
  }

  .lang-switch{
    display:flex; align-items:center;
    border:1px solid rgba(234,188,91,0.3);
    border-radius:20px; overflow:hidden;
    background: rgba(12, 7, 20, 0.6);
  }
  .lang-switch button{
    font-family:var(--font-ui); font-size:.75rem; font-weight:600;
    background:transparent; color:var(--cream-dim);
    border:none; padding:6px 12px; cursor:pointer; transition:all 0.2s;
  }
  .lang-switch button.active{background:var(--gold); color:var(--void);}

  .burger-btn {
    display: none; background: transparent; border: none;
    color: var(--gold); font-size: 1.5rem; cursor: pointer; padding: 4px;
  }
  .mobile-menu {
    display: none; position: fixed; top: 60px; left: 0; right: 0;
    background: rgba(12, 7, 20, 0.96); backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(234,188,91,0.2);
    padding: 20px; flex-direction: column; gap: 16px; z-index: 79;
    text-align: center;
  }
  .mobile-menu.active { display: flex; }
  .mobile-menu a {
    font-family: var(--font-ui); font-size: 1rem; color: var(--cream);
    padding: 10px 0; border-bottom: 1px solid rgba(234,188,91,0.1);
  }

  /* Main Hero Container */
  .hero{
    position:relative; z-index:1;
    max-width:1200px; margin:20px auto 0;
    padding:20px 5vw;
    display:grid; grid-template-columns:1fr 1fr; gap:36px; align-items:center;
  }
  .hero-text h1{
    font-family:var(--font-display);
    font-size:clamp(2rem, 4vw, 3.4rem);
    color:var(--gold); margin:0 0 14px;
    text-shadow:0 0 30px rgba(234,188,91,0.2);
  }
  .hero-text p.sub{
    color:var(--cream-dim); font-size:1rem; line-height:1.6; margin:0 0 24px;
  }

  .question-box{
    background:rgba(10,6,16,0.7);
    border:1px solid rgba(234,188,91,0.28);
    border-radius:16px; padding:16px; margin-bottom:18px;
  }
  textarea#question{
    width:100%; min-height:90px; resize:none;
    background:transparent; border:none; outline:none;
    color:var(--cream); font-family:var(--font-body); font-size:16px; font-style:italic;
  }
  .char-count{text-align:right; font-family:var(--font-ui); font-size:.75rem; color:rgba(184,169,196,0.5);}

  .pay-cta{display:flex; flex-direction:column; gap:12px;}
  .btn-pay{
    width:100%; display:flex; align-items:center; justify-content:center; gap:8px;
    font-family:var(--font-ui); font-weight:600; font-size:.92rem;
    color:var(--cream);
    background:linear-gradient(160deg, var(--purple-1), var(--purple-2) 55%, var(--purple-3));
    border:1px solid rgba(234,188,91,0.35); padding:14px 12px; border-radius:12px;
    cursor:pointer; transition:transform .2s ease, opacity .2s ease;
  }
  .btn-pay:hover{transform:translateY(-2px); border-color:var(--gold);}
  .btn-pay:active{transform:scale(0.98); opacity: 0.9;}

  /* Media Container */
  .hero-photo{position:relative; display:flex; justify-content:center;}
  .media-container {
    position: relative; width: 100%; max-width: 480px;
    border-radius: 20px; overflow: hidden; background: #000;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8);
    border: 1px solid rgba(234,188,91,0.25);
  }
  .media-container img, .media-container video {
    width: 100%; height: auto; display: block;
    mask-image: radial-gradient(circle, black 70%, transparent 98%);
    -webkit-mask-image: radial-gradient(circle, black 70%, transparent 98%);
  }
  .media-container video {
    position: absolute; top: 0; left: 0; opacity: 0; transition: opacity 0.3s ease; pointer-events: none;
  }
  .media-container.playing video { opacity: 1; }

  /* Modal */
  .modal-overlay {
    position: fixed; inset: 0; z-index: 200;
    background: rgba(5, 3, 8, 0.85); backdrop-filter: blur(8px);
    display: none; align-items: center; justify-content: center; padding: 16px;
  }
  .modal-overlay.active { display: flex; }
  .modal-card {
    background: var(--deep); border: 1px solid var(--gold);
    border-radius: 20px; padding: 24px; max-width: 440px; width: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8); text-align: center;
  }
  .modal-card h3 { font-family: var(--font-display); color: var(--gold); margin-top: 0; font-size: 1.3rem; }
  .currency-rates {
    background: rgba(255,255,255,0.05); border-radius: 12px; padding: 12px; margin: 16px 0;
    font-family: var(--font-ui); font-size: 0.85rem; text-align: left; line-height: 1.7;
  }
  .pay-option-btn {
    width: 100%; padding: 14px 12px; margin-bottom: 10px; border-radius: 10px;
    border: 1px solid rgba(234,188,91,0.3); background: rgba(28,15,46,0.8);
    color: var(--cream); font-family: var(--font-ui); font-weight: 600; font-size: 0.88rem;
    cursor: pointer; display: flex; align-items: center; justify-content: space-between;
  }
  .btn-close-modal {
    background: transparent; border: none; color: var(--cream-dim);
    font-size: 0.85rem; cursor: pointer; margin-top: 10px; text-decoration: underline;
  }

  /* Fortune Scroll Section */
  .fortune-section{
    position:relative; z-index:1; max-width:1100px; margin:40px auto; padding:0 5vw;
  }
  .scroll-wrap{
    background:rgba(21,12,34,0.4); border:1px solid rgba(234,188,91,0.2);
    border-radius:20px; padding:28px 24px; text-align:center;
  }
  .scroll-wrap h3{font-family:var(--font-display); color:var(--gold); margin-top:0; font-size: 1.5rem;}
  .scroll-paper{
    background:linear-gradient(160deg,#f6ecd6,#efe0bd); color:#3a2a12;
    padding:20px; border-radius:8px; font-size:1.05rem; line-height:1.6; min-height:90px;
    display:flex; align-items:center; justify-content:center; white-space: pre-line;
  }

  /* Reviews Section (Отзывы) */
  .reviews-section {
    max-width: 1100px; margin: 50px auto; padding: 0 5vw;
  }
  .section-title {
    font-family: var(--font-display); color: var(--gold); font-size: 1.8rem;
    text-align: center; margin-bottom: 30px;
  }
  .reviews-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;
  }
  .review-card {
    background: rgba(12, 7, 20, 0.6); border: 1px solid rgba(234,188,91,0.18);
    border-radius: 16px; padding: 20px; line-height: 1.5; font-size: 0.92rem;
  }
  .review-author {
    font-family: var(--font-ui); font-weight: 700; color: var(--gold);
    margin-bottom: 6px; display: flex; align-items: center; justify-content: space-between;
  }
  .stars { color: #f5c518; font-size: 0.85rem; }

  /* Footer & Contacts (Почта и контакты) */
  footer {
    max-width: 1100px; margin: 60px auto 0; padding: 30px 5vw 10px;
    border-top: 1px solid rgba(234,188,91,0.15);
    display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px;
    font-family: var(--font-ui); font-size: 0.88rem; color: var(--cream-dim);
  }
  .footer-contacts a { color: var(--gold); text-decoration: underline; }
  .footer-contacts a:hover { color: #fff; }

  /* Sticky Telegram Bar */
  .tg-float-bar {
    position:fixed; bottom:12px; left:50%; transform:translateX(-50%);
    z-index:100; width:92%; max-width:500px;
    background:rgba(21,12,34,0.94); backdrop-filter:blur(10px);
    border:1px solid rgba(0,136,204,0.6); border-radius:16px; padding:10px 14px;
    display:flex; align-items:center; justify-content:space-between; gap:10px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
  }
  .tg-bar-title {font-family:var(--font-ui); font-weight:700; font-size:0.85rem; color:var(--cream);}
  .btn-tg-open {
    font-family:var(--font-ui); font-weight:600; font-size:0.8rem;
    color:#fff; background:var(--tg-blue); border:none; padding:8px 12px; border-radius:8px; white-space:nowrap; cursor:pointer;
  }

  @media (max-width:850px){
    nav.desktop-nav{display:none;}
    .burger-btn{display:block; font-size: 1.8rem; padding: 6px 12px;}
    .hero{grid-template-columns:1fr; text-align:center; padding-top:10px; gap: 20px;}
    .hero-photo{order:-1;}
    .question-box{text-align:left;}
    .btn-pay {padding: 16px 12px; font-size: 0.95rem;}
    footer {flex-direction: column; text-align: center;}
  }
</style>
</head>
<body>

<header>
  <div class="logo">🪶 <span data-i18n="logoTitle">Боря гадает</span></div>
  
  <nav class="desktop-nav">
    <a href="#fortune" data-i18n="navFortune">Гадание</a>
    <a href="#reviews" data-i18n="navReviews">Отзывы</a>
    <a href="#contacts" data-i18n="navContacts">Контакты</a>
  </nav>

  <div class="header-actions">
    <div class="lang-switch">
      <button class="lang-btn active" data-lang="ru" onclick="switchLang('ru')">RU</button>
      <button class="lang-btn" data-lang="en" onclick="switchLang('en')">EN</button>
    </div>
    <button class="burger-btn" onclick="toggleMobileMenu()" aria-label="Меню">☰</button>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu">
  <a href="#fortune" onclick="toggleMobileMenu()" data-i18n="navFortune">Гадание</a>
  <a href="#reviews" onclick="toggleMobileMenu()" data-i18n="navReviews">Отзывы</a>
  <a href="#contacts" onclick="toggleMobileMenu()" data-i18n="navContacts">Контакты</a>
</div>

<main>
  <section class="hero">
    <div class="hero-photo">
      <div class="media-container" id="mediaBox">
        <img src="borya.jpg" alt="Попугай Боря гадает">
        <video id="boryaVideo" src="borya.mp4" playsinline muted preload="auto"></video>
      </div>
    </div>

    <div class="hero-text">
      <h1 data-i18n="heroTitle">Боря гадает</h1>
      <p class="sub" data-i18n="heroSub">Задайте вопрос, и волнистый предсказатель вытащит ваш индивидуальный свиток.</p>

      <div class="question-box">
        <textarea id="question" maxlength="200" placeholder="Напишите ваш вопрос здесь..." data-i18n-ph="inputPlaceholder"></textarea>
        <div class="char-count"><span id="char-count">0</span> / 200</div>
      </div>

      <div class="pay-cta">
        <button class="btn-pay" onclick="openPaymentModal('question', 100)" data-i18n="btnPayQuestion">Гадание на вопрос — 100 ₽ / $1.2 ✨</button>
        <button class="btn-pay" onclick="openPaymentModal('rent', 500)" style="background:linear-gradient(160deg, #7a1030, #5d2463);" data-i18n="btnPayRent">Аренда Бори на неделю — 500 ₽ / $6 👑</button>
        <button class="btn-pay" id="free-btn" style="background:transparent; border:1px solid rgba(234,188,91,0.5); color:var(--gold);" data-i18n="btnFree">Бесплатный свиток дня 🎁</button>
      </div>
    </div>
  </section>

  <section class="fortune-section" id="fortune">
    <div class="scroll-wrap">
      <h3 data-i18n="fortuneTitle">Предсказание Бори</h3>
      <div class="scroll-paper" id="fortune-text">
        <span data-i18n="fortuneDefault">Нажмите кнопку гадания, чтобы Боря вытащил ответ...</span>
      </div>
    </div>
  </section>

  <!-- Блок с отзывами -->
  <section class="reviews-section" id="reviews">
    <h2 class="section-title" data-i18n="reviewsTitle">Отзывы наших гостей</h2>
    <div class="reviews-grid">
      <div class="review-card">
        <div class="review-author">Елена С. <span class="stars">★★★★★</span></div>
        <p data-i18n="rev1">«Спросила у Бори про смену работы. Свиток попался очень точный и поддержал меня! Боря просто прелесть 🦜»</p>
      </div>
      <div class="review-card">
        <div class="review-author">Михаил <span class="stars">★★★★★</span></div>
        <p data-i18n="rev2">«Взяли подписку на неделю для всей семьи. Каждое утро начинаем с пернатого предсказания. Поднимает настроение!»</p>
      </div>
      <div class="review-card">
        <div class="review-author">Анна К. <span class="stars">★★★★★</span></div>
        <p data-i18n="rev3">«Очень милый и добрый проект. Бесплатный свиток дня попал прямо в точку. Спасибо огромное!»</p>
      </div>
    </div>
  </section>
</main>

<div class="modal-overlay" id="payModal">
  <div class="modal-card">
    <h3 data-i18n="modalTitle">Выберите способ оплаты</h3>
    <p style="font-size:0.85rem; color:var(--cream-dim);" data-i18n="modalSub">Автоматическое зачисление на вашу карту.</p>
    
    <div class="currency-rates" id="modalRates">
      <div><span data-i18n="rateRub">Сумма в рублях:</span> <b id="rubVal">100 ₽</b></div>
      <div><span data-i18n="rateUsd">Сумма в долларах:</span> <b id="usdVal">$1.20</b></div>
      <div><span data-i18n="rateGel">К зачислению (TBC GEL):</span> <b id="gelVal">~3.20 GEL</b></div>
    </div>

    <button class="pay-option-btn" onclick="processPayment('tg_bot')" style="border-color:var(--tg-blue);">
      <span data-i18n="payTgBot">✈️ Перейти к оплате в Telegram</span> ➔
    </button>

    <button class="pay-option-btn" onclick="processPayment('card_web')">
      <span data-i18n="payCardWeb">💳 Оплата картой (СБП / МИР / Visa / MC)</span> ➔
    </button>

    <button class="btn-close-modal" onclick="closePaymentModal()" data-i18n="btnClose">Отмена</button>
  </div>
</div>

<div class="tg-float-bar">
    <div>
        <div class="tg-bar-title">✈️ Telegram <span>Боря Гадает</span></div>
        <div style="font-size:0.75rem; color:var(--cream-dim);" data-i18n="tgBarSub">Гадания прямо в боте</div>
    </div>
    <a href="https://t.me/BoryaFortuneBot" target="_blank"><button class="btn-tg-open" data-i18n="btnTgOpen">Открыть Бот</button></a>
</div>

<!-- Футер с контактами и почтой -->
<footer id="contacts">
  <div>© 2026 Боря гадает. Все права защищены.</div>
  <div class="footer-contacts">
    <span data-i18n="contactText">Связь с нами:</span> 
    <a href="mailto:support@boryafortune.com">support@boryafortune.com</a> | 
    <a href="https://t.me/BoryaFortuneBot" target="_blank">Telegram</a>
  </div>
</footer>

<script>
  let currentLang = 'ru';

  const translations = {
    ru: {
      logoTitle: "Боря гадает",
      navFortune: "Гадание",
      navReviews: "Отзывы",
      navContacts: "Контакты",
      heroTitle: "Боря гадает",
      heroSub: "Задайте вопрос, и волнистый предсказатель вытащит ваш индивидуальный свиток.",
      inputPlaceholder: "Напишите ваш вопрос здесь...",
      btnPayQuestion: "Гадание на вопрос — 100 ₽ / $1.2 ✨",
      btnPayRent: "Аренда Бори на неделю — 500 ₽ / $6 👑",
      btnFree: "Бесплатный свиток дня 🎁",
      fortuneTitle: "Предсказание Бори",
      fortuneDefault: "Нажмите кнопку гадания, чтобы Боря вытащил ответ...",
      reviewsTitle: "Отзывы наших гостей",
      rev1: "«Спросила у Бори про смену работы. Свиток попался очень точный и поддержал меня! Боря просто прелесть 🦜»",
      rev2: "«Взяли подписку на неделю для всей семьи. Каждое утро начинаем с пернатого предсказания. Поднимает настроение!»",
      rev3: "«Очень милый и добрый проект. Бесплатный свиток дня попал прямо в точку. Спасибо огромное!»",
      contactText: "Связь с нами:",
      modalTitle: "Выберите способ оплаты",
      modalSub: "Автоматическое зачисление на вашу карту.",
      rateRub: "Сумма в рублях:",
      rateUsd: "Сумма в долларах:",
      rateGel: "К зачислению (TBC GEL):",
      payCardWeb: "💳 Оплата картой (СБП / МИР / Visa / MC)",
      payTgBot: "✈️ Перейти к оплате в Telegram",
      btnClose: "Отмена",
      tgBarSub: "Гадания прямо в боте",
      btnTgOpen: "Открыть Бот",
      msgEnterQuestion: "Пожалуйста, сначала введите ваш вопрос!",
      msgDailyScroll: "🎁 [Свиток Дня]\n Сегодня удача на вашей стороне, смело затевайте новое!"
    },
    en: {
      logoTitle: "Borya Divines",
      navFortune: "Fortune",
      navReviews: "Reviews",
      navContacts: "Contacts",
      heroTitle: "Borya Divines",
      heroSub: "Ask your question, and the wise budgie will draw your unique scroll.",
      inputPlaceholder: "Type your personal question here...",
      btnPayQuestion: "Ask a Question — 100 ₽ / $1.2 ✨",
      btnPayRent: "Rent Borya for a week — 500 ₽ / $6 👑",
      btnFree: "Free Daily Scroll 🎁",
      fortuneTitle: "Borya's Prediction",
      fortuneDefault: "Click a button above to let Borya pick your scroll...",
      reviewsTitle: "Guest Reviews",
      rev1: "«Asked Borya about changing jobs. The scroll was accurate and truly supportive! Borya is lovely 🦜»",
      rev2: "«Got a weekly sub for the family. We start every morning with a feathered prediction. Brings pure joy!»",
      rev3: "«Such a sweet project. Free daily scroll hit the mark. Thank you so much!»",
      contactText: "Contact us:",
      modalTitle: "Choose Payment Method",
      modalSub: "Automatic deposit to your card.",
      rateRub: "Amount in RUB:",
      rateUsd: "Amount in USD:",
      rateGel: "Total (TBC GEL):",
      payCardWeb: "💳 Pay with Card (SBP / Visa / MC)",
      payTgBot: "✈️ Pay via Telegram",
      btnClose: "Cancel",
      tgBarSub: "Fortunes right in the bot",
      btnTgOpen: "Open Bot",
      msgEnterQuestion: "Please enter your question first!",
      msgDailyScroll: "🎁 [Daily Scroll]\n Today fortune is on your side, take the leap!"
    }
  };

  function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('active');
  }

  function switchLang(lang) {
    currentLang = lang;
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (translations[lang][key]) {
        el.innerText = translations[lang][key];
      }
    });

    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
      const key = el.getAttribute('data-i18n-ph');
      if (translations[lang][key]) {
        el.placeholder = translations[lang][key];
      }
    });
  }

  const RUB_GEL = 0.031;
  let currentType = '';
  let currentRubBase = 100;

  const video = document.getElementById('boryaVideo');
  const mediaBox = document.getElementById('mediaBox');

  function openPaymentModal(type, baseRub) {
    if (type === 'question' && !document.getElementById('question').value.trim()) {
      alert(translations[currentLang].msgEnterQuestion);
      return;
    }
    currentType = type;
    currentRubBase = baseRub;

    document.getElementById('rubVal').innerText = baseRub + ' ₽';
    document.getElementById('usdVal').innerText = '$' + (baseRub / 85).toFixed(2);
    document.getElementById('gelVal').innerText = '~' + (baseRub * RUB_GEL).toFixed(2) + ' GEL';

    document.getElementById('payModal').classList.add('active');
  }

  function closePaymentModal() {
    document.getElementById('payModal').classList.remove('active');
  }

  function processPayment(provider) {
    closePaymentModal();
    const q = encodeURIComponent(document.getElementById('question').value.trim() || 'Запрос гадания');

    if (provider === 'tg_bot') {
      window.open(`https://t.me/BoryaFortuneBot?start=${q}`, '_blank');
    } else if (provider === 'card_web') {
      window.open(`https://lava.top`, '_blank');
    }
  }

  function startBoryaDivination(text) {
    mediaBox.classList.add('playing');
    video.currentTime = 0;
    
    video.play().catch(() => showScrollResult(text));
    video.onended = () => {
      mediaBox.classList.remove('playing');
      showScrollResult(text);
    };
  }

  function showScrollResult(text) {
    document.getElementById('fortune-text').innerHTML = `<span>${text}</span>`;
    document.getElementById('fortune').scrollIntoView({ behavior: 'smooth' });
  }

  document.getElementById('free-btn').addEventListener('click', () => {
    startBoryaDivination(translations[currentLang].msgDailyScroll);
  });

  document.getElementById('question').addEventListener('input', (e) => {
    document.getElementById('char-count').textContent = e.target.value.length;
  });
</script>
</body>
</html>
