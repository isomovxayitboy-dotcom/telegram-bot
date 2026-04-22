import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8721724117:AAHHI50naOiPAkHtXMyUrwrgAD8DKxKipPM"

papka = "kitoblar"

# /start komandasi
from telegram import ReplyKeyboardMarkup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []

    for fayl in os.listdir(papka):
        if fayl.endswith(".pdf"):
            nom = fayl.replace(".pdf", "")
            keyboard.append([nom])

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "📚 Kitobni tanlang:",
        reply_markup=markup
    )


# xabarni qabul qilish
async def qidir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    savol = update.message.text.lower()

    for fayl in os.listdir(papka):
        if fayl.endswith(".pdf"):
            nom = fayl.replace(".pdf", "").lower()

            if savol in nom:
                file_path = os.path.join(papka, fayl)

                await update.message.reply_document(document=open(file_path, "rb"))
                return

    await update.message.reply_text("❌ Bunday kitob topilmadi")

# botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, qidir))

app.run_polling()
import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

papka = "kitoblar"

# 📚 Kitoblar (nom : fayl)
books = {
    "Dunyoning ishlari": "23_-Dunyoning-ishlari.pdf",
    "O‘tkan kunlar": "a_qodiriyt_utgan_kunlar_namdu_uz.pdf",
    "Molxona": "%40KutubxonaN1Jorj-Oruell-Molxona.pdf"
}

# 🔘 Tugmalar
keyboard = [[name] for name in books.keys()]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ▶️ start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 Kitobni tanlang:", reply_markup=markup)

# 📩 Tugma bosilganda
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text in books:
        file_path = os.path.join(papka, books[text])

        try:
            await update.message.reply_document(open(file_path, "rb"))
        except:
            await update.message.reply_text("❌ Fayl topilmadi")
    else:
        await update.message.reply_text("❌ Bunday kitob yo‘q")

# 🚀 Botni ishga tushirish (TOKENNI O‘ZING QO‘SHASAN)
app = ApplicationBuilder().token("8721724117:AAHHI50naOiPAkHtXMyUrwrgAD8DKxKipPM").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handler))

app.run_polling()
