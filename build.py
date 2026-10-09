#!/usr/bin/env python3
"""Generates the multilingual landing pages (fa, en, ar, tr, ru) + sitemap.xml.
Run: python3 build.py"""
import json, os, html, sys

BASE = "https://hamedshahi5.github.io/venice-ai/"
REF = os.environ.get("VENICE_REF") or sys.exit("Usage: VENICE_REF=<your referral url> python3 build.py")
NS = "vnc-hs5-4f9a7c21"  # counter namespace (Abacus)
from texts_extra import X
ROOT = os.path.dirname(os.path.abspath(__file__))
PATHS = {"fa": "", "en": "en/", "ar": "ar/", "tr": "tr/", "ru": "ru/"}
META = {"fa": ("فارسی", "rtl", "fa_IR"), "en": ("English", "ltr", "en_US"),
        "ar": ("العربية", "rtl", "ar_AR"), "tr": ("Türkçe", "ltr", "tr_TR"),
        "ru": ("Русский", "ltr", "ru_RU")}

# keys: title, desc, badge, h1 (with {hl}), lead, cta, note, why, f1..f4 (title|text), how, s1..s3,
#       faq, q1..q3 (question|answer), cta2t, cta2d, disc
T = {
"en": dict(
 title="Venice AI — Private, Uncensored AI Chat & Image Generator (Free to Start)",
 desc="Venice AI is a privacy-focused AI platform for chat, image generation and coding, built on open-source models. Learn what it offers and try it free.",
 badge="Private · Open-source models · Free tier",
 h1="Venice AI: AI chat that takes your {hl} seriously", hl="privacy",
 lead="Venice is a generative AI platform for chat, image generation and coding. It runs open-source models and says your conversations stay on your device instead of being stored on its servers.",
 cta="Try Venice free →", note="Free tier available — no credit card needed to start.",
 why="Why people use Venice",
 f1="Privacy-first|The company states conversations aren't stored on its servers; chat history stays in your browser.",
 f2="Fewer restrictions|Open-source models with lighter content filtering than typical mainstream assistants — use it responsibly.",
 f3="Chat, images & code|Write, research, generate images and get coding help in one place, with web search and system prompts.",
 f4="Web, mobile & API|Works in the browser with nothing to install, has a mobile app, and offers an API for developers.",
 how="Get started in 3 steps",
 s1="Click the button to open Venice.", s2="Start chatting right away, or sign up for more features.",
 s3="Hit the free limits? The paid Pro plan raises them — check Venice's official site for current pricing.",
 faq="FAQ",
 q1="What is Venice AI?|A privacy-focused generative AI platform with fewer content restrictions, for text, images and code, built on open-source models.",
 q2="Is Venice AI free?|Yes, there is a free tier with daily limits. A paid Pro plan raises the limits and unlocks extra features; see the official site for current details.",
 q3="Is this the official Venice website?|No. This is an independent, unofficial intro page and is not affiliated with Venice.",
 cta2t="Ready to try it?", cta2d="It takes a minute to see if it fits your needs.",
 disc="Disclosure: links on this page are referral links. If you sign up through them, I may receive a reward at no extra cost to you. This page is independent and not affiliated with Venice."),
"fa": dict(
 title="Venice AI — چت هوش مصنوعی خصوصی و بدون سانسور | شروع رایگان",
 desc="معرفی Venice AI؛ پلتفرم هوش مصنوعی با تمرکز روی حریم خصوصی برای چت، ساخت تصویر و کدنویسی با مدل‌های متن‌باز. بدون هزینه شروع کن.",
 badge="خصوصی · مدل‌های متن‌باز · نسخهٔ رایگان",
 h1="Venice AI؛ هوش مصنوعی‌ای که {hl} رو جدی می‌گیره", hl="حریم خصوصی",
 lead="Venice یه پلتفرم هوش مصنوعیه برای چت، ساخت تصویر و کدنویسی. با مدل‌های متن‌باز کار می‌کنه و طبق ادعای خودش، گفتگوهات به‌جای سرورهای شرکت، پیش خودت می‌مونه.",
 cta="شروع رایگان در Venice ←", note="نسخهٔ رایگان داره؛ برای شروع کارت بانکی لازم نیست.",
 why="چرا Venice؟",
 f1="تمرکز روی حریم خصوصی|طبق اعلام شرکت، گفتگوها روی سرورهاش ذخیره نمی‌شن و تاریخچهٔ چت تو مرورگر خودت می‌مونه.",
 f2="محدودیت کمتر|مدل‌های متن‌باز با فیلتر ملایم‌تر نسبت به دستیارهای رایج؛ مسئولانه ازش استفاده کن.",
 f3="چت، تصویر و کد|نوشتن، تحقیق، ساخت تصویر و کمک کدنویسی در یک جا، همراه با جستجوی وب و System Prompt.",
 f4="وب، موبایل و API|بدون نصب تو مرورگر کار می‌کنه، اپ موبایل داره و برای توسعه‌دهنده‌ها API هم ارائه می‌ده.",
 how="در ۳ قدم شروع کن",
 s1="روی دکمه بزن و Venice رو باز کن.", s2="همون لحظه می‌تونی چت کنی یا برای امکانات بیشتر ثبت‌نام کنی.",
 s3="به سقف رایگان خوردی؟ پلن Pro محدودیت‌ها رو بالا می‌بره؛ قیمت روز رو تو سایت رسمی ببین.",
 faq="سؤالات متداول",
 q1="Venice AI چیه؟|یه پلتفرم هوش مصنوعی با تمرکز روی حریم خصوصی و محدودیت کمتر برای متن، تصویر و کد که روی مدل‌های متن‌باز ساخته شده.",
 q2="Venice AI رایگانه؟|بله، نسخهٔ رایگان با سقف روزانه داره. پلن پولی Pro سقف‌ها رو بالا می‌بره و امکانات بیشتری باز می‌کنه؛ جزئیات روز رو تو سایت رسمی ببین.",
 q3="این سایت رسمی Venice هست؟|نه. این یه صفحهٔ معرفی مستقل و غیررسمیه و وابسته به Venice نیست.",
 cta2t="آمادهٔ امتحان کردنی؟", cta2d="یه دقیقه وقت بذار ببین به کارت میاد یا نه.",
 disc="شفاف‌سازی: لینک‌های این صفحه رفرال هستن. اگه از طریقشون ثبت‌نام کنی، ممکنه بدون هزینهٔ اضافه برای تو، پاداشی به من برسه. این صفحه مستقله و ربطی به Venice نداره."),
"ar": dict(
 title="Venice AI — دردشة ذكاء اصطناعي خاصة وبقيود أقل | ابدأ مجاناً",
 desc="تعرّف على Venice AI: منصة ذكاء اصطناعي تركّز على الخصوصية للدردشة وتوليد الصور والبرمجة عبر نماذج مفتوحة المصدر. جرّبها مجاناً.",
 badge="خصوصية · نماذج مفتوحة المصدر · خطة مجانية",
 h1="Venice AI: ذكاء اصطناعي يأخذ {hl} على محمل الجد", hl="خصوصيتك",
 lead="Venice منصة ذكاء اصطناعي توليدي للدردشة وتوليد الصور والبرمجة. تعمل بنماذج مفتوحة المصدر، وتذكر الشركة أن محادثاتك تبقى على جهازك بدل تخزينها على خوادمها.",
 cta="جرّب Venice مجاناً ←", note="تتوفر خطة مجانية — لا حاجة لبطاقة مصرفية للبدء.",
 why="لماذا يستخدم الناس Venice؟",
 f1="الخصوصية أولاً|تقول الشركة إن المحادثات لا تُخزَّن على خوادمها، وسجل الدردشة يبقى في متصفحك.",
 f2="قيود أقل|نماذج مفتوحة المصدر بفلترة أخف من المساعدات الشائعة — استخدمها بمسؤولية.",
 f3="دردشة وصور وبرمجة|اكتب وابحث وولّد الصور واحصل على مساعدة برمجية في مكان واحد، مع البحث في الويب وSystem Prompt.",
 f4="ويب وجوال وAPI|تعمل من المتصفح دون تثبيت، ولها تطبيق جوال، وتوفّر API للمطورين.",
 how="ابدأ في 3 خطوات",
 s1="اضغط الزر لفتح Venice.", s2="ابدأ الدردشة فوراً أو أنشئ حساباً لمزيد من الميزات.",
 s3="وصلت إلى حد الخطة المجانية؟ خطة Pro ترفع الحدود؛ راجع الموقع الرسمي للأسعار الحالية.",
 faq="الأسئلة الشائعة",
 q1="ما هو Venice AI؟|منصة ذكاء اصطناعي توليدي تركّز على الخصوصية وبقيود أقل للنصوص والصور والبرمجة، مبنية على نماذج مفتوحة المصدر.",
 q2="هل Venice AI مجاني؟|نعم، توجد خطة مجانية بحدود يومية. خطة Pro المدفوعة ترفع الحدود وتتيح ميزات إضافية؛ راجع الموقع الرسمي للتفاصيل الحالية.",
 q3="هل هذا الموقع الرسمي لـ Venice؟|لا. هذه صفحة تعريفية مستقلة وغير رسمية ولا تتبع Venice.",
 cta2t="مستعد للتجربة؟", cta2d="دقيقة واحدة تكفي لتعرف إن كانت مناسبة لك.",
 disc="إفصاح: الروابط في هذه الصفحة روابط إحالة. إذا سجّلت عبرها فقد أحصل على مكافأة دون أي تكلفة إضافية عليك. الصفحة مستقلة ولا تتبع Venice."),
"tr": dict(
 title="Venice AI — Gizlilik Odaklı, Daha Az Kısıtlamalı Yapay Zekâ Sohbeti | Ücretsiz Başla",
 desc="Venice AI'yi tanıyın: açık kaynak modellerle sohbet, görsel üretimi ve kodlama sunan, gizliliğe odaklı bir yapay zekâ platformu. Ücretsiz deneyin.",
 badge="Gizlilik · Açık kaynak modeller · Ücretsiz plan",
 h1="Venice AI: {hl} ciddiye alan yapay zekâ", hl="Gizliliğinizi",
 lead="Venice; sohbet, görsel üretimi ve kodlama için üretken bir yapay zekâ platformu. Açık kaynak modeller kullanır ve şirketin belirttiğine göre sohbetleriniz sunucularında değil, cihazınızda kalır.",
 cta="Venice'i ücretsiz dene →", note="Ücretsiz plan var — başlamak için kredi kartı gerekmez.",
 why="İnsanlar neden Venice kullanıyor?",
 f1="Önce gizlilik|Şirket, sohbetlerin sunucularında saklanmadığını belirtiyor; sohbet geçmişi tarayıcınızda kalır.",
 f2="Daha az kısıtlama|Yaygın asistanlara göre daha hafif filtreli açık kaynak modeller — sorumlu kullanın.",
 f3="Sohbet, görsel ve kod|Yazın, araştırın, görsel üretin ve kod yardımı alın; web araması ve System Prompt desteğiyle.",
 f4="Web, mobil ve API|Kurulum gerektirmeden tarayıcıda çalışır, mobil uygulaması vardır ve geliştiriciler için API sunar.",
 how="3 adımda başla",
 s1="Düğmeye tıklayıp Venice'i aç.", s2="Hemen sohbet etmeye başla ya da daha fazla özellik için kaydol.",
 s3="Ücretsiz limite mi takıldın? Pro plan limitleri yükseltir; güncel fiyatlar için resmî siteye bak.",
 faq="Sık sorulan sorular",
 q1="Venice AI nedir?|Açık kaynak modeller üzerine kurulu; metin, görsel ve kod için gizlilik odaklı, daha az kısıtlamalı bir üretken yapay zekâ platformu.",
 q2="Venice AI ücretsiz mi?|Evet, günlük limitli ücretsiz bir plan var. Ücretli Pro plan limitleri artırır ve ek özellikler açar; güncel ayrıntılar için resmî siteye bakın.",
 q3="Bu, Venice'in resmî sitesi mi?|Hayır. Bu bağımsız ve resmî olmayan bir tanıtım sayfasıdır; Venice ile bağlantısı yoktur.",
 cta2t="Denemeye hazır mısın?", cta2d="Sana uyup uymadığını görmek bir dakikanı alır.",
 disc="Açıklama: Bu sayfadaki bağlantılar referans bağlantısıdır. Bunlarla kaydolursanız, size ek maliyeti olmadan bir ödül alabilirim. Sayfa bağımsızdır ve Venice ile bağlantılı değildir."),
"ru": dict(
 title="Venice AI — приватный ИИ-чат с меньшими ограничениями | Начать бесплатно",
 desc="Обзор Venice AI: платформа ИИ с упором на приватность для чата, генерации изображений и программирования на открытых моделях. Попробуйте бесплатно.",
 badge="Приватность · Открытые модели · Бесплатный тариф",
 h1="Venice AI: ИИ, который всерьёз относится к вашей {hl}", hl="приватности",
 lead="Venice — платформа генеративного ИИ для чата, создания изображений и программирования. Работает на открытых моделях, и, по заявлению компании, ваши диалоги остаются на устройстве, а не хранятся на её серверах.",
 cta="Попробовать Venice бесплатно →", note="Есть бесплатный тариф — банковская карта для старта не нужна.",
 why="Почему выбирают Venice",
 f1="Приватность прежде всего|Компания заявляет, что диалоги не хранятся на её серверах; история чата остаётся в вашем браузере.",
 f2="Меньше ограничений|Открытые модели с более мягкой фильтрацией, чем у популярных ассистентов — пользуйтесь ответственно.",
 f3="Чат, изображения и код|Пишите, исследуйте, создавайте изображения и получайте помощь с кодом в одном месте, с веб-поиском и System Prompt.",
 f4="Веб, приложение и API|Работает в браузере без установки, есть мобильное приложение и API для разработчиков.",
 how="Начните за 3 шага",
 s1="Нажмите кнопку и откройте Venice.", s2="Сразу начните чат или зарегистрируйтесь ради дополнительных функций.",
 s3="Упёрлись в лимит бесплатного тарифа? Тариф Pro поднимает лимиты; актуальные цены смотрите на официальном сайте.",
 faq="Частые вопросы",
 q1="Что такое Venice AI?|Платформа генеративного ИИ с упором на приватность и меньшими ограничениями для текста, изображений и кода на открытых моделях.",
 q2="Venice AI бесплатный?|Да, есть бесплатный тариф с дневными лимитами. Платный Pro повышает лимиты и открывает доп. функции; подробности — на официальном сайте.",
 q3="Это официальный сайт Venice?|Нет. Это независимая неофициальная страница-обзор, не связанная с Venice.",
 cta2t="Готовы попробовать?", cta2d="Одной минуты достаточно, чтобы понять, подходит ли вам.",
 disc="Раскрытие: ссылки на этой странице реферальные. Если вы зарегистрируетесь по ним, я могу получить вознаграждение без дополнительных расходов для вас. Страница независима и не связана с Venice."),
}

for _l, _d in X.items():
    T[_l].update(_d)

e = html.escape
TRACKER = """<script>
(function(){var B="https://abacus.jasoncameron.dev/hit/__NS__/",L="__LANG__";
function hit(k){try{fetch(B+k,{keepalive:true}).catch(function(){})}catch(e){}}
hit("views");hit("views-"+L);
var d=new Date().toISOString().slice(0,10),s=0;
try{s=localStorage.getItem("vseen")===d;if(!s)localStorage.setItem("vseen",d)}catch(e){}
if(!s){hit("visitors");hit("visitors-"+L)}
document.addEventListener("click",function(ev){var a=ev.target.closest&&ev.target.closest("a.ref");
if(a){hit("clicks");hit("clicks-"+L)}},true);})();
</script>"""

STATS = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Stats</title><link rel="stylesheet" href="style.css"></head>
<body><div class="wrap"><h1 style="font-size:30px">📊 Stats</h1>
<p class="note">Counts via Abacus. Visitors = once per browser per day. Bots may inflate numbers.</p>
<div class="grid" id="g"></div><h2>By language</h2><div class="grid" id="l"></div>
<script>
var B="https://abacus.jasoncameron.dev/get/__NS__/";
function g(k){return fetch(B+k).then(function(r){return r.ok?r.json():{value:0}}).then(function(j){return j.value||0}).catch(function(){return 0})}
function card(t,v){return '<div class="card"><b>'+v+'</b><p>'+t+'</p></div>'}
function run(){Promise.all(["views","visitors","clicks"].map(g)).then(function(a){
var ctr=a[1]?Math.round(a[2]/a[1]*1000)/10+"%":"-";
document.getElementById("g").innerHTML=card("Page views",a[0])+card("Unique visitors (daily)",a[1])+card("Link clicks",a[2])+card("Click rate (clicks / visitors)",ctr)});
var L=["fa","en","ar","tr","ru"];
Promise.all(L.map(function(l){return Promise.all([g("visitors-"+l),g("clicks-"+l)])})).then(function(r){
document.getElementById("l").innerHTML=r.map(function(x,i){return card(L[i]+": visitors / clicks",x[0]+" / "+x[1])}).join("")})}
run();setInterval(run,30000);
</script></div></body></html>"""

def page(lang):
    t = T[lang]; name, d, loc = META[lang]
    pre = "" if lang == "fa" else "../"
    url = BASE + PATHS[lang]
    h1 = e(t["h1"]).replace("{hl}", f'<span>{e(t["hl"])}</span>')
    faq = [t[k].split("|", 1) for k in ("q1", "q2", "q3", "q4")]
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": t["title"], "description": t["desc"],
           "url": url, "inLanguage": lang, "isPartOf": {"@type": "WebSite", "name": "Venice AI — Intro", "url": BASE}},
          {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE + PATHS[l]}">\n' for l in PATHS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{BASE}en/">\n'
    sw = "".join(f'<a href="{pre + PATHS[l] if l != "fa" else pre or "./"}" hreflang="{l}" lang="{l}"'
                 f'{" class=on aria-current=page" if l == lang else ""}>{META[l][0]}</a>' for l in PATHS)
    feats = "".join(f'<div class=card><b>{e(t[k].split("|")[0])}</b><p>{e(t[k].split("|")[1])}</p></div>'
                    for k in ("f1", "f2", "f3", "f4", "f5", "f6"))
    steps = "".join(f"<li>{e(t[k])}</li>" for k in ("s1", "s2", "s3"))
    faqh = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq)
    font = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&display=swap" rel="stylesheet">') if d == "rtl" else ""
    link = f'class="btn ref" href="{REF}" target="_blank" rel="noopener sponsored nofollow"'
    TRK = TRACKER.replace("__NS__", NS).replace("__LANG__", lang)
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="canonical" href="{url}">
{alts}<meta property="og:type" content="website">
<meta property="og:site_name" content="Venice AI — Intro">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{loc}">
<meta property="og:image" content="{BASE}og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🔒%3C/text%3E%3C/svg%3E">
{font}<link rel="stylesheet" href="{pre}style.css">
<meta name="robots" content="index,follow,max-image-preview:large">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="{d}">
<div class="wrap">
<nav class="lang" aria-label="Language">{sw}</nav>
<header class="hero">
<span class="badge">{e(t["badge"])}</span>
<h1>{h1}</h1>
<p class="lead">{e(t["lead"])}</p>
<a {link}>{e(t["cta"])}</a>
<p class="note">{e(t["note"])}</p>
</header>
<main>
<h2>{e(t["why"])}</h2>
<div class="grid">{feats}</div>
<h2>{e(t["privh"])}</h2><p class="txt">{e(t["priv"])}</p>
<h2>{e(t["plansh"])}</h2><p class="txt">{e(t["plans"])}</p>
<div class="box"><b>{e(t["refh"])}</b> {e(t["ref"])}</div>
<h2>{e(t["how"])}</h2>
<ol>{steps}</ol>
<h2>{e(t["knowh"])}</h2><p class="txt">{e(t["know"])}</p>
<h2>{e(t["faq"])}</h2>
{faqh}
<section class="cta"><h2>{e(t["cta2t"])}</h2><p>{e(t["cta2d"])}</p><a {link}>{e(t["cta"])}</a></section>
</main>
<footer>{e(t["disc"])}</footer>
</div>
{TRK}
</body>
</html>
'''

for l in PATHS:
    os.makedirs(os.path.join(ROOT, PATHS[l]), exist_ok=True)
    with open(os.path.join(ROOT, PATHS[l], "index.html"), "w", encoding="utf-8") as f:
        f.write(page(l))

open(os.path.join(ROOT, "stats.html"), "w", encoding="utf-8").write(STATS.replace("__NS__", NS))

alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE + PATHS[l]}"/>' for l in PATHS)
urls = "".join(f"<url><loc>{BASE + PATHS[l]}</loc>{alts}</url>" for l in PATHS)
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            f'xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>')
print("built", list(PATHS))
