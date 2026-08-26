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
    padding-bottom: 110px; 
  }
  a{color:inherit; text-decoration:none;}

  #stars{position:fixed; inset:0; z-index:0; pointer-events:none;}

  /* Header */
  header{
    position:sticky; top:0; z-index:80;
    display:flex; align-items:center; justify-content:space-between;
    padding:16px 5vw;
    background:rgba(5,3,8,0.75);
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
  nav.desktop-nav{display:flex; gap:24px;}
  nav.desktop-nav a{
    font-family:var(--font-ui); font-size:.88rem; color:var(--cream-dim); transition:color .2s;
  }
  nav.desktop-nav a:hover{color:var(--gold);}

  .lang-switch{
    display:flex; align-items:center;
    border:1px solid rgba(234,188,91,0.3);
    border-radius:20px; overflow:hidden;
  }
  .lang-switch button{
    font-family:var(--font-ui); font-size:.75rem; font-weight:600;
    background:transparent; color:var(--cream-dim);
    border:none; padding:5px 12px; cursor:pointer; transition:all 0.2s;
  }
  .lang-switch button.active{background:var(--gold); color:var(--void);}

  /* Hero Section */
  .hero{
    position:relative; z-index:1;
    max-width:1200px; margin:0 auto;
    padding:30px 5vw;
    display:grid; grid-template-columns:1fr 1fr; gap:30px; align-items:center;
  }
  .hero-text h1{
    font-family:var(--font-display);
    font-size:clamp(2rem,4vw,3.2rem);
    color:var(--gold); margin:0 0 14px;
    text-shadow:0 0 30px rgba(234,188,91,0.2);
  }
  .hero-text p.sub{
    color:var(--cream-dim); font-size:1rem; line-height:1.6; margin:0 0 24px;
  }

  .question-box{
    background:rgba(10,6,16,0.7);
    border:1px solid rgba(234,188,91,0.28);
    border-radius:16px; padding:14px 16px; margin-bottom:18px;
  }
  textarea#question{
    width:100%; min-height:80px; resize:none;
    background:transparent; border:none; outline:none;
    color:var(--cream); font-family:var(--font-body); font-size:1rem; font-style:italic;
  }
  .char-count{text-align:right; font-family:var(--font-ui); font-size:.75rem; color:rgba(184,169,196,0.5);}

  .pay-cta{display:flex; flex-direction:column; gap:10px;}
  .btn-pay{
    width:100%; display:flex; align-items:center; justify-content:center; gap:8px;
    font-family:var(--font-ui); font-weight:600; font-size:.95rem;
    color:var(--cream);
    background:linear-gradient(160deg, var(--purple-1), var(--purple-2) 55%, var(--purple-3));
    border:1px solid rgba(234,188,91,0.35); padding:14px; border-radius:12px;
    cursor:pointer; transition:transform .2s ease;
  }
  .btn-pay:active{transform:scale(0.98);}

  /* Media Player (Photo/Video) */
  .hero-photo{position:relative; display:flex; justify-content:center;}
  .media-container {
    position: relative; width: 100%; max-width: 550px;
    border-radius: 20px; overflow: hidden; background: #000;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8);
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

  /* Modal Payment Window */
  .modal-overlay {
    position: fixed; inset: 0; z-index: 200;
    background: rgba(5, 3, 8, 0.85); backdrop-filter: blur(8px);
    display: none; align-items: center; justify-content: center; padding: 20px;
  }
  .modal-overlay.active { display: flex; }
  .modal-card {
    background: var(--deep); border: 1px solid var(--gold);
    border-radius: 20px; padding: 24px; max-width: 440px; width: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.8); text-align: center;
  }
  .modal-card h3 { font-family: var(--font-display); color: var(--gold); margin-top: 0; }
  .currency-rates {
    background: rgba(255,255,255,0.05); border-radius: 12px; padding: 12px; margin: 16px 0;
    font-family: var(--font-ui); font-size: 0.88rem; text-align: left; line-height: 1.8;
  }
  .pay-option-btn {
    width: 100%; padding: 12px; margin-bottom: 8px; border-radius: 10px;
    border: 1px solid rgba(234,188,91,0.3); background: rgba(28,15,46,0.8);
    color: var(--cream); font-family: var(--font-ui); font-weight: 600;
    cursor: pointer; display: flex; align-items: center; justify-content: space-between;
  }
  .btn-close-modal {
    background: transparent; border: none; color: var(--cream-dim);
    font-size: 0.85rem; cursor: pointer; margin-top: 10px; text-decoration: underline;
  }

  /* Fortune Scroll Section */
  .fortune-section{
    position:relative; z-index:1; max-width:1000px; margin:20px auto; padding:0 5vw;
  }
  .scroll-wrap{
    background:rgba(21,12,34,0.4); border:1px solid rgba(234,188,91,0.2);
    border-radius:20px; padding:24px; text-align:center;
  }
  .scroll-wrap h3{font-family:var(--font-display); color:var(--gold); margin-top:0;}
  .scroll-paper{
    background:linear-gradient(160deg,#f6ecd6,#efe0bd); color:#3a2a12;
    padding:20px; border-radius:8px; font-size:1.05rem; line-height:1.5; min-height:90px;
    display:flex; align-items:center; justify-content:center; white-space: pre-line;
  }

  /* Info Sections */
  section.info{position:relative; z-index:1; max-width:1100px; margin:0 auto; padding:40px 5vw;}
  section.info h2{font-family:var(--font-display); font-size:clamp(1.6rem,3.2vw,2.2rem); color:var(--gold); margin:0 0 16px;}

  /* Reviews */
  .reviews-grid{display:grid; grid-template-columns:repeat(3,1fr); gap:20px; margin-top:20px;}
  .review-card{background:rgba(21,12,34,0.4); border:1px solid rgba(234,188,91,0.16); border-radius:16px; padding:20px;}
  .review-stars{color:var(--gold); font-size:.95rem; margin-bottom:10px;}
  .review-card p{color:var(--cream-dim); font-size:.94rem; line-height:1.6; margin:0 0 14px;}
  .review-name{font-family:var(--font-ui); font-size:.82rem; color:var(--gold-soft); font-weight:600;}

  /* Form for Reviews */
  .add-review-box {
    background: rgba(12, 7, 20, 0.7);
    border: 1px solid rgba(234,188,91,0.25);
    border-radius: 18px; padding: 24px; margin-top: 30px;
    max-width: 650px;
  }
  .add-review-box h3 { font-family: var(--font-display); color: var(--gold); margin-top: 0; font-size: 1.2rem; }
  .form-group { margin-bottom: 14px; text-align: left; }
  .form-group label { display: block; font-family: var(--font-ui); font-size: 0.85rem; color: var(--cream-dim); margin-bottom: 6px; }
  .form-group input, .form-group textarea, .form-group select {
    width: 100%; background: rgba(5,3,8,0.6); border: 1px solid rgba(234,188,91,0.2);
    border-radius: 10px; padding: 10px 14px; color: var(--cream); font-family: var(--font-ui); font-size: 0.9rem; outline: none;
  }
  .form-group textarea { resize: vertical; min-height: 70px; }
  .btn-submit-review {
    background: var(--gold); color: var(--void); border: none; font-family: var(--font-ui);
    font-weight: 700; font-size: 0.9rem; padding: 12px 24px; border-radius: 10px; cursor: pointer; transition: opacity 0.2s;
  }
  .btn-submit-review:hover { opacity: 0.9; }

  /* About & Contacts */
  .about-grid{display:grid; grid-template-columns:140px 1fr; gap:26px; align-items:center; margin-top:20px;}
  .about-portrait{
    aspect-ratio:1/1; border-radius:50%; overflow:hidden;
    border:2px solid rgba(234,188,91,0.4); display:flex; align-items:center; justify-content:center;
    background:radial-gradient(circle at 35% 30%, rgba(127,178,65,.3), rgba(21,12,34,.9)); font-size:3rem;
  }
  .about-grid p{color:var(--cream-dim); line-height:1.7; margin:0 0 12px; font-size:1rem;}

  .contact-grid{display:grid; grid-template-columns:repeat(2,1fr); gap:20px; margin-top:20px;}
  .contact-card{background:rgba(21,12,34,0.4); border:1px solid rgba(234,188,91,0.16); border-radius:16px; padding:22px; text-align:center;}
  .contact-card .ic{font-size:1.6rem; display:block; margin-bottom:8px;}
  .contact-card b{display:block; font-family:var(--font-ui); font-size:.85rem; color:var(--gold); margin-bottom:4px;}
  .contact-card span{font-size:.88rem; color:var(--cream-dim);}

  /* Sticky Telegram Floating Bar */
  .tg-float-bar {
    position:fixed; bottom:15px; left:50%; transform:translateX(-50%);
    z-index:100; width:92%; max-width:500px;
    background:rgba(21,12,34,0.92); backdrop-filter:blur(10px);
    border:1px solid rgba(0,136,204,0.6); border-radius:16px; padding:12px 16px;
    display:flex; align-items:center; justify-content:space-between; gap:10px;
  }
  .tg-bar-title {font-family:var(--font-ui); font-weight:700; font-size:0.88rem; color:var(--cream);}
  .btn-tg-open {
    font-family:var(--font-ui); font-weight:600; font-size:0.8rem;
    color:#fff; background:var(--tg-blue); border:none; padding:10px 14px; border-radius:10px; white-space:nowrap; cursor:pointer;
  }

  footer{
    position:relative; z-index:1; padding:26px 5vw 34px;
    border-top:1px solid rgba(234,188,91,0.14);
    display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:14px;
    font-family:var(--font-ui); font-size:.78rem; color:rgba(184,169,196,0.6);
  }

  /* Mobile Media Queries */
  @media (max-width:850px){
    nav.desktop-nav{display:none;}
    .hero{grid-template-columns:1fr; text-align:center; padding-top:20px;}
    .hero-photo{order:-1;}
    .question-box{text-align:left;}
    .reviews-grid, .about-grid, .contact-grid{grid-template-columns:1fr;}
    .tg-bar-title span {display:none;}
  }
</style>
</head>
<body>

<header>
  <div class="logo">🪶 <span data-i18n="logoTitle">Боря гадает</span></div>
  <nav class="desktop-nav">
    <a href="#fortune" data-i18n="navFortune">Гадание</a>
    <a href="#reviews" data-i18n="navReviews">Отзывы</a>
    <a href="#about" data-i18n="navAbout">О Боре</a>
    <a href="#contacts" data-i18n="navContacts">Контакты</a>
  </nav>
  <div class="lang-switch">
    <button id="btn-ru" class="active" onclick="switchLang('ru')">RU</button>
    <button id="btn-en" onclick="switchLang('en')">EN</button>
  </div>
</header>

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

  <section class="info" id="reviews">
    <h2 data-i18n="reviewsTitle">Отзывы счастливчиков</h2>
    <div class="reviews-grid" id="reviewsContainer">
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p>«Боря просто чудо! Спросила про повышение, он вытащил свиток "Скоро взлетишь". И правда!»</p>
        <div class="review-name">— Лена К.</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p>«Скептически относился, но вопрос задал. В итоге принял верное решение. Боря шарит!»</p>
        <div class="review-name">— Игорь С.</div>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★☆</div>
        <p>«Очень мило наблюдать за процессом. Предсказание подняло настроение на весь день!»</p>
        <div class="review-name">— Ольга П.</div>
      </div>
    </div>

    <!-- Интерактивная форма добавления отзыва -->
    <div class="add-review-box">
      <h3 data-i18n="addReviewTitle">Оставить свой отзыв</h3>
      <form id="reviewForm">
        <div class="form-group">
          <label data-i18n="lblReviewName">Ваше имя:</label>
          <input type="text" id="revName" required placeholder="Например: Анна М." data-i18n-ph="phReviewName">
        </div>
        <div class="form-group">
          <label data-i18n="lblReviewStars">Оценка:</label>
          <select id="revStars">
            <option value="★★★★★">★★★★★ (5/5)</option>
            <option value="★★★★☆">★★★★☆ (4/5)</option>
            <option value="★★★☆☆">★★★☆☆ (3/5)</option>
          </select>
        </div>
        <div class="form-group">
          <label data-i18n="lblReviewText">Ваш отзыв:</label>
          <textarea id="revText" required placeholder="Поделитесь своими впечатлениями..." data-i18n-ph="phReviewText"></textarea>
        </div>
        <button type="submit" class="btn-submit-review" data-i18n="btnSubmitReview">Отправить отзыв</button>
      </form>
    </div>
  </section>

  <section class="info" id="about">
    <h2 data-i18n="aboutTitle">О попугайчике Боре</h2>
    <div class="about-grid">
      <div class="about-portrait">🦜</div>
      <div>
        <p data-i18n="aboutP1">Боря — не просто волнистый попугайчик. Он потомственный прорицатель в седьмом поколении.</p>
        <p data-i18n="aboutP2">Боря обладает уникальной интуицией и способностью выбирать именно тот свиток, который нужен вам в данный момент.</p>
      </div>
    </div>
  </section>

  <section class="info" id="contacts">
    <h2 data-i18n="contactsTitle">Связаться с нами</h2>
    <div class="contact-grid">
      <div class="contact-card">
        <span class="ic">📩</span>
        <b>Email</b>
        <span>madammarisha2011@yandex.ru</span>
      </div>
      <div class="contact-card">
        <span class="ic">✈️</span>
        <b data-i18n="contactTgBot">Telegram Бот</b>
        <span>@BoryaFortuneBot</span>
      </div>
    </div>
  </section>
</main>

<!-- Модальное окно выбора оплаты с автоконвертацией -->
<div class="modal-overlay" id="payModal">
  <div class="modal-card">
    <h3 data-i18n="modalTitle">Выберите способ оплаты</h3>
    <p style="font-size:0.85rem; color:var(--cream-dim);" data-i18n="modalSub">Зачисление производится на карту TBC Bank (Грузия) в GEL.</p>
    
    <div class="currency-rates" id="modalRates">
      <div><span data-i18n="rateRub">Сумма в рублях:</span> <b id="rubVal">100 ₽</b></div>
      <div><span data-i18n="rateUsd">Сумма в долларах:</span> <b id="usdVal">$1.20</b></div>
      <div><span data-i18n="rateGel">К зачислению (TBC GEL):</span> <b id="gelVal">~3.20 GEL</b></div>
    </div>

    <button class="pay-option-btn" onclick="processPayment('card_gel')">
      <span data-i18n="payCardGel">💳 Международная карта (USD / GEL)</span> ➔
    </button>
    <button class="pay-option-btn" onclick="processPayment('card_rub')">
      <span data-i18n="payCardRub">🇷🇺 Карта РФ / СБП (Рубли)</span> ➔
    </button>
    <button class="pay-option-btn" onclick="processPayment('tg_bot')" style="border-color:var(--tg-blue);">
      <span data-i18n="payTgBot">✈️ Оплатить через Telegram Bot</span> ➔
    </button>

    <button class="btn-close-modal" onclick="closePaymentModal()" data-i18n="btnClose">Отмена</button>
  </div>
</div>

<div class="tg-float-bar">
    <div>
        <div class="tg-bar-title">✈️ Telegram-бот <span>Боря Гадает</span></div>
        <div style="font-size:0.75rem; color:var(--cream-dim);" data-i18n="tgBarSub">Гадания прямо в мессенджере</div>
    </div>
    <a href="https://t.me/BoryaFortuneBot" target="_blank"><button class="btn-tg-open" data-i18n="btnTgOpen">Открыть Бот</button></a>
</div>

<footer>
  <div>&copy; 2026 Боря гадает. Все права защищены перьями.</div>
</footer>

<script>
  let currentLang = 'ru';

  // База текстов интерфейса (Перевод RU / EN)
  const translations = {
    ru: {
      logoTitle: "Боря гадает",
      navFortune: "Гадание",
      navReviews: "Отзывы",
      navAbout: "О Боре",
      navContacts: "Контакты",
      heroTitle: "Боря гадает",
      heroSub: "Задайте вопрос, и волнистый предсказатель вытащит ваш индивидуальный свиток.",
      inputPlaceholder: "Напишите ваш вопрос здесь...",
      btnPayQuestion: "Гадание на вопрос — 100 ₽ / $1.2 ✨",
      btnPayRent: "Аренда Бори на неделю — 500 ₽ / $6 👑",
      btnFree: "Бесплатный свиток дня 🎁",
      fortuneTitle: "Предсказание Бори",
      fortuneDefault: "Нажмите кнопку гадания, чтобы Боря вытащил ответ...",
      reviewsTitle: "Отзывы счастливчиков",
      addReviewTitle: "Оставить свой отзыв",
      lblReviewName: "Ваше имя:",
      phReviewName: "Например: Анна М.",
      lblReviewStars: "Оценка:",
      lblReviewText: "Ваш отзыв:",
      phReviewText: "Поделитесь своими впечатлениями...",
      btnSubmitReview: "Отправить отзыв",
      aboutTitle: "О попугайчике Боре",
      aboutP1: "Боря — не просто волнистый попугайчик. Он потомственный прорицатель в седьмом поколении.",
      aboutP2: "Боря обладает уникальной интуицией и способностью выбирать именно тот свиток, который нужен вам в данный момент.",
      contactsTitle: "Связаться с нами",
      contactTgBot: "Telegram Бот",
      modalTitle: "Выберите способ оплаты",
      modalSub: "Зачисление производится на карту TBC Bank (Грузия) в GEL.",
      rateRub: "Сумма в рублях:",
      rateUsd: "Сумма в долларах:",
      rateGel: "К зачислению (TBC GEL):",
      payCardGel: "💳 Международная карта (USD / GEL)",
      payCardRub: "🇷🇺 Карта РФ / СБП (Рубли)",
      payTgBot: "✈️ Оплатить через Telegram Bot",
      btnClose: "Отмена",
      tgBarSub: "Гадания прямо в мессенджере",
      btnTgOpen: "Открыть Бот"
    },
    en: {
      logoTitle: "Borya Divines",
      navFortune: "Fortune",
      navReviews: "Reviews",
      navAbout: "About Borya",
      navContacts: "Contacts",
      heroTitle: "Borya Divines",
      heroSub: "Ask your question, and the wise budgie will draw your unique scroll.",
      inputPlaceholder: "Type your personal question here...",
      btnPayQuestion: "Ask a Question — 100 ₽ / $1.2 ✨",
      btnPayRent: "Rent Borya for a week — 500 ₽ / $6 👑",
      btnFree: "Free Daily Scroll 🎁",
      fortuneTitle: "Borya's Prediction",
      fortuneDefault: "Click a button above to let Borya pick your scroll...",
      reviewsTitle: "Happy Clients Reviews",
      addReviewTitle: "Leave Your Review",
      lblReviewName: "Your Name:",
      phReviewName: "E.g., Ann M.",
      lblReviewStars: "Rating:",
      lblReviewText: "Your Review:",
      phReviewText: "Share your experience...",
      btnSubmitReview: "Submit Review",
      aboutTitle: "About Borya the Budgie",
      aboutP1: "Borya is no ordinary budgerigar. He is a 7th generation hereditary fortune teller.",
      aboutP2: "Borya possesses unique intuition and picking exactly the scroll you need right now.",
      contactsTitle: "Contact Us",
      contactTgBot: "Telegram Bot",
      modalTitle: "Choose Payment Method",
      modalSub: "Payment is processed via TBC Bank (Georgia) in GEL.",
      rateRub: "Amount in RUB:",
      rateUsd: "Amount in USD:",
      rateGel: "Total (TBC GEL):",
      payCardGel: "💳 International Card (USD / GEL)",
      payCardRub: "🇷🇺 Russian Card / SBP",
      payTgBot: "✈️ Pay via Telegram Bot",
      btnClose: "Cancel",
      tgBarSub: "Fortunes right in your messenger",
      btnTgOpen: "Open Bot"
    }
  };

  // База из 100 предсказаний (RU / EN)
  const fortunesData = {
    ru: [
      "Сегодня идеальный день, чтобы сделать первый шаг к вашей давней мечте!",
      "Обратите внимание на знаки вокруг: Вселенная готовит вам приятный сюрприз.",
      "Не бойтесь задержек — всё складывается именно так, как должно.",
      "Вас ждет неожиданная, но очень теплая встреча или сообщение.",
      "Доверьтесь интуиции: сегодня она станет вашим лучшим проводником.",
      "Скоро откроется дверь, которую вы считали навсегда закрытой.",
      "Удача любит смелых: сделайте шаг вперед, даже если немного страшно!",
      "Ваш труд скоро принесет плоды, о которых вы даже не мечтали.",
      "Отпустите сомнения: вы на верном пути!",
      "Финансовый поток готовит для вас приятное прибавление.",
      "Человек из прошлого принесет добрые новости.",
      "Отличный момент для обновления — в мыслях, доме или делах.",
      "Ваше обаяние сегодня на максимуме, используйте это!",
      "Трудности временны, а вот ваш опыт останется с вами навсегда.",
      "Будьте готовы к спонтанному путешествию или приятной поездке.",
      "Кто-то тайный искренне восхищается вашей мудростью и добротой.",
      "Совсем скоро вы услышите слова, которых так долго ждали.",
      "Вам удастся найти идеальное решение запутанной задачи.",
      "Сегодня Боря видит, что гармония и покой уже на пороге вашего дома.",
      "Позвольте себе немного отдыха: вы это заслужили!",
      "Вселенная убирает лишнее из вашей жизни, освобождая место новому.",
      "Ваша идея принесет вам не только радость, но и успех.",
      "Маленький шаг сегодня приведет к большому триумфу завтра.",
      "Будьте открыты новым знакомствам — среди них есть ключевой человек.",
      "Вам улыбнется удача там, где вы совсем этого не ждали.",
      "Счастье ближе, чем кажется. Оглянитесь вокруг!",
      "Скоро появится человек, который поддержит ваши главные начинания.",
      "Ваша энергия привлекает только позитивные события.",
      "Сегодня отличный день для покупок и подарков самому себе.",
      "Не сравнивайте себя с другими: ваш путь уникален и прекрасен.",
      "Боря чирикнул: 'Всё будет даже лучше, чем ты планируешь!'",
      "Пришло время поверить в свои силы на 100%.",
      "Скоро вас порадует доброе известие издалека.",
      "Любовное вдохновение накроет вас с головой.",
      "Период неопределенности подходит к концу.",
      "Ваш внутренний свет притягивает нужных людей.",
      "Не бойтесь просить о помощи — вам с радостью откликнутся.",
      "Смело стройте планы на будущее, звезды на вашей стороне.",
      "Улыбнитесь! Сегодня ваш день для маленьких чудес.",
      "То, что кажется препятствием, окажется вашей новой возможностью.",
      "Ваши финансовые дела скоро заметно пойдут в гору.",
      "Забота о себе сегодня — ваш главный приоритет.",
      "Боря шепчет, что ваш самый важный проект увенчается успехом.",
      "Вас ждет вечер, полный уюта и душевных разговоров.",
      "Не сходите с выбранной дороги: цель уже близко.",
      "Добро, которое вы сделали недавно, вернется к вам в троекратном размере.",
      "Ваше творческое мышление поможет решить любую проблему.",
      "Впереди время приятных покупок и обновлений.",
      "Один звонок изменит ход ваших текущих дел в лучшую сторону.",
      "Будьте честны с собой — и ответы придут моментально.",
      "Слушайте свое сердце, оно точно знает правильный маршрут.",
      "Вас ждет приятная похвала или признание ваших заслуг.",
      "Время отпустить старые обиды и открыть сердце новому.",
      "Успех любит подготовленных: вы готовы к новому рывку!",
      "Боря видит в вашем будущем много смеха и радости.",
      "Ваш оптимизм станет главным ключом к решению задачи.",
      "Ожидайте удачной сделки или выгодного предложения.",
      "Сегодня идеальный день для творчества и вдохновения.",
      "Отношения с близкими станут еще теплее и доверительнее.",
      "Будьте внимательны к мелочам: там скрыта подсказка судьбы.",
      "Вам удастся сохранить баланс даже в бурном потоке событий.",
      "Новое начинание принесет плоды быстрей, чем вы думали.",
      "Не бойтесь менять планы по ходу: гибкость принесет победу.",
      "Судьба готовит для вас яркое и радостное событие.",
      "Ваша искренность покорит даже самых строгих людей.",
      "Откройтесь неожиданностям — они принесут вам радость.",
      "Боря гарантирует: ваш вопрос решится в вашу пользу!",
      "Скоро вы обретете ясность там, где раньше был туман.",
      "Ваши старания замечают и очень высоко ценят.",
      "Оставьте тревоги позади, впереди только светлая полоса.",
      "Отличный момент для того, чтобы порадовать близкого человека.",
      "Ваша интуиция защитит вас от любых неверных шагов.",
      "Вам предстоит узнать кое-что очень приятное и интересное.",
      "Жизнь готовит вам мягкий поворот к лучшему.",
      "Будьте смелее в своих желаниях — Вселенная слушат!",
      "Ваша внутренний покой — это ваша лучшая защита.",
      "Скоро вас ждет вдохновляющий успех на работе или в учебе.",
      "Не переживайте по пустякам: все наладится само собой.",
      "Боря подмигивает: 'Твое желание уже исполняется!'",
      "Приятный подарок или бонус порадует вас в ближайшие дни.",
      "Ваш опыт поможет кому-то сделать важный и правильный выбор.",
      "Впереди время стабильности, уюта и гармонии.",
      "Позвольте себе мечтать масштабно!",
      "Все сомнения развеются, как дым, уже совсем скоро.",
      "Вы являетесь источником вдохновения для многих людей.",
      "Ваши финансовые решения сегодня будут максимально удачными.",
      "Смело открывайте новую главу жизни — там много счастья.",
      "Каждый шаг делает вас сильнее и ближе к цели.",
      "Боря уверен: сегодня вас ждет хотя бы один волшебный момент!",
      "Подарите миру улыбку — и мир улыбнется вам в ответ.",
      "Скоро вы найдете ответ на вопрос, который долго мучил вас.",
      "Ваши таланты раскроются с новой неожиданной стороны.",
      "Ждите приятных новостей, касающихся вашей семьи.",
      "Время действовать! Удача на вашей стороне.",
      "Ваша доброта возвращается к вам самым чудесным образом.",
      "Будьте готовы принять подарок судьбы с открытым сердцем.",
      "Сегодняшний день принесет вам чувство глубокого удовлетворения.",
      "Боря кивает: 'Ты справишься абсолютно со всем!'",
      "Верьте в себя так, как Боря верит в вас!",
      "Впереди вас ждет грандиозный прорыв и радость!"
    ],
    en: [
      "Today is the perfect day to take the first step towards your dream!",
      "Pay attention to signs around: the Universe has a surprise for you.",
      "Don't fear delays — everything is unfolding just as it should.",
      "An unexpected but very warm message or meeting awaits you.",
      "Trust your intuition: today it will be your best guide.",
      "A door you thought was closed forever will open soon.",
      "Fortune favors the bold: step forward even if it's a bit scary!",
      "Your hard work will soon bear fruits beyond your expectations.",
      "Let go of doubts: you are on the right path!",
      "A financial flow is preparing a pleasant boost for you.",
      "Someone from the past will bring great news.",
      "A great moment for renewal — in thoughts, home, or business.",
      "Your charm is at its peak today, make use of it!",
      "Troubles are temporary, but your experience stays forever.",
      "Be ready for a spontaneous trip or pleasant journey.",
      "Someone secretly admires your wisdom and kindness.",
      "Very soon you will hear words you've waited for so long.",
      "You will find the ideal solution to a complex puzzle.",
      "Borya sees that peace and harmony are on your doorstep.",
      "Allow yourself a little rest: you've earned it!",
      "The Universe removes what's unnecessary to make room for the new.",
      "Your idea will bring you not only joy, but great success.",
      "A small step today leads to a grand triumph tomorrow.",
      "Be open to new acquaintances — a key person is among them.",
      "Fortune will smile upon you where you least expect it.",
      "Happiness is closer than it seems. Look around!",
      "Someone will appear soon to support your dream project.",
      "Your positive energy attracts only good events.",
      "Today is a wonderful day for treats and gifts for yourself.",
      "Don't compare yourself to others: your journey is unique.",
      "Borya chirped: 'Everything will be even better than planned!'",
      "It is time to believe in your power 100%.",
      "Good news from afar will bring a big smile soon.",
      "Romantic inspiration will surround you completely.",
      "A period of uncertainty is coming to a smooth end.",
      "Your inner light naturally attracts the right people.",
      "Don't hesitate to ask for help — people will gladly answer.",
      "Dream big: the stars are completely on your side.",
      "Smile! Today is your day for tiny magical miracles.",
      "What seems like an obstacle will turn into a new door.",
      "Your financial affairs are about to improve significantly.",
      "Self-care is your highest priority today.",
      "Borya whispers that your main project will succeed brilliantly.",
      "An evening full of warmth and cozy talks is waiting for you.",
      "Stay on your chosen path: the goal is very close.",
      "The kindness you gave recently will return threefold.",
      "Your creative mind will easily solve any problem.",
      "Ahead lies a time of pleasant purchases and updates.",
      "A single call will change things in your favor.",
      "Be honest with yourself — and answers will arrive instantly.",
      "Listen to your heart: it knows the best route.",
      "Expect well-deserved praise and recognition of your work.",
      "Time to let go of old grudges and embrace new beginnings.",
      "Success loves readiness: you are ready for a victory!",
      "Borya sees lots of joy and laughter in your future.",
      "Your optimism is the main key to solving the issue.",
      "Expect a successful deal or a profitable offer.",
      "Today is ideal for inspiration and artistic creativity.",
      "Relationships with loved ones will become warmer.",
      "Be attentive to details: a secret clue is hidden there.",
      "You will maintain balance even in a storm of events.",
      "A new beginning will bear fruit faster than expected.",
      "Don't fear changing plans: flexibility brings victory.",
      "Destiny is preparing a joyful event just for you.",
      "Your sincerity will win over even the toughest people.",
      "Open up to surprises — they will bring pure joy.",
      "Borya guarantees: your question will resolve in your favor!",
      "Soon you will find clarity where fog used to be.",
      "Your efforts are noticed and deeply appreciated.",
      "Leave worries behind, only bright days lie ahead.",
      "Great moment to bring joy to someone close to you.",
      "Your intuition will shield you from any wrong steps.",
      "You are about to learn something very pleasant.",
      "Life is taking a gentle turn for the better.",
      "Be bolder in your dreams — the Universe hears you!",
      "Your inner calm is your ultimate protection.",
      "An inspiring achievement at work or study awaits.",
      "Don't worry about small things: all will settle easily.",
      "Borya winks: 'Your wish is already coming true!'",
      "A pleasant gift or bonus will delight you soon.",
      "Your experience will help someone make the right choice.",
      "Ahead lies a period of comfort, stability, and peace.",
      "Allow yourself to dream big and bold!",
      "All doubts will vanish like smoke very soon.",
      "You are a true source of inspiration for many.",
      "Your financial choices today will be extremely wise.",
      "Step confidently into a new chapter — happiness is there.",
      "Every step brings you closer to your ultimate goal.",
      "Borya is sure: at least one magic moment awaits today!",
      "Give the world a smile — and it will smile back at you.",
      "Soon you will find the answer to a long-standing question.",
      "Your talents will unfold in a brand new way.",
      "Expect joyful news regarding your family.",
      "Time to act! Luck is completely on your side.",
      "Your kindness returns to you in the most wonderful way.",
      "Be ready to accept destiny's gift with an open heart.",
      "Today will bring you a deep sense of satisfaction.",
      "Borya nods: 'You can handle absolutely everything!'",
      "Believe in yourself as much as Borya believes in you!",
      "A grand breakthrough and pure joy lie ahead!"
    ]
  };

  // Переключение языка (RU / EN)
  function switchLang(lang) {
    currentLang = lang;
    document.getElementById('btn-ru').classList.toggle('active', lang === 'ru');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');

    // Перевод обычных текстов
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (translations[lang][key]) {
        el.innerText = translations[lang][key];
      }
    });

    // Перевод placeholder
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
      const key = el.getAttribute('data-i18n-ph');
      if (translations[lang][key]) {
        el.placeholder = translations[lang][key];
      }
    });
  }

  // Конвертация курсов
  const RUB_GEL = 0.031;

  let currentType = '';
  let currentRubBase = 100;

  const video = document.getElementById('boryaVideo');
  const mediaBox = document.getElementById('mediaBox');

  function openPaymentModal(type, baseRub) {
    if (type === 'question' && !document.getElementById('question').value.trim()) {
      alert(currentLang === 'ru' ? 'Пожалуйста, сначала введите ваш вопрос!' : 'Please enter your question first!');
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
    const q = document.getElementById('question').value.trim();

    if (provider === 'tg_bot') {
      const encodedQ = encodeURIComponent(q || 'Запрос гадания');
      window.open(`https://t.me/BoryaFortuneBot?start=${encodedQ}`, '_blank');
      return;
    }

    const randomFortune = getRandomFortune();
    startBoryaDivination(q ? `[${currentLang === 'ru' ? 'Ответ на вопрос' : 'Answer'}]: "${q}"\n\n✨ ${randomFortune}` : `👑 ${randomFortune}`);
  }

  function getRandomFortune() {
    const arr = fortunesData[currentLang];
    return arr[Math.floor(Math.random() * arr.length)];
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
    const randomFortune = getRandomFortune();
    startBoryaDivination(`🎁 [${currentLang === 'ru' ? 'Свиток Дня' : 'Daily Scroll'}]\n\n${randomFortune}`);
  });

  document.getElementById('question').addEventListener('input', (e) => {
    document.getElementById('char-count').textContent = e.target.value.length;
  });

  // Обработка формы отзыва
  document.getElementById('reviewForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('revName').value.trim();
    const stars = document.getElementById('revStars').value;
    const text = document.getElementById('revText').value.trim();

    if (!name || !text) return;

    // Создаем карточку отзыва
    const card = document.createElement('div');
    card.className = 'review-card';
    card.innerHTML = `
      <div class="review-stars">${stars}</div>
      <p>«${text}»</p>
      <div class="review-name">— ${name}</div>
    `;

    // Вставляем отзыв первым в список
    const container = document.getElementById('reviewsContainer');
    container.insertBefore(card, container.firstChild);

    // Очищаем форму
    document.getElementById('reviewForm').reset();
    alert(currentLang === 'ru' ? 'Спасибо! Ваш отзыв опубликован.' : 'Thank you! Your review has been published.');
  });
</script>
</body>
</html>
