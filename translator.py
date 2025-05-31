'''from telegram.ext.updater import Updater
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(f"You have entered {user_input}")
    
    
def main():
    api = open("api.txt", "r")
    updater = Updater(api.read(), use_context=True) 
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters.text, reply))
    updater.start_polling()
    updater.idle()
    
main()



from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# --------------  handler: /start  -----------------
async def select_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="en"),
            InlineKeyboardButton("Español", callback_data="es"),
        ],
        [
            InlineKeyboardButton("Français", callback_data="fr"),
            InlineKeyboardButton("Deutsch", callback_data="de"),
        ],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose target language:", reply_markup=markup)


# --------------  handler: button press ------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data            # "en" / "es" ...
    context.user_data["lang"] = lang
    await query.edit_message_text(f"✅ Language set to {lang.upper()}.\nSend me any text:")


# --------------  handler: free text ---------------
from deep_translator import GoogleTranslator

def lang_translator(text: str, dest_lang: str) -> str:
    return GoogleTranslator(source='auto', target=dest_lang).translate(text)

from googletrans import Translator
_gt = Translator()


def lang_translator(text: str, dest_lang: str) -> str:
    res = _gt.translate(text, dest=dest_lang)
    return res.text


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    target = context.user_data.get("lang", "en")
    translated = lang_translator(user_input, target)
    await update.message.reply_text(translated)


# --------------  main() ---------------------------
def main() -> None:
    # 1. read the bot token
    with open("api.txt", "r", encoding="utf-8") as api_file:
        api_key = api_file.read().strip()


    # 2. build the application
    application = ApplicationBuilder().token("7777797590:AAHsjGaCbP_xyEWDWlCpySLHoXgfNDpWASc").build()

    # 3. register handlers
    application.add_handler(CommandHandler("start", select_lang))
    application.add_handler(CommandHandler("select_lang", select_lang))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    # 4. run the bot
    application.run_polling()


if __name__ == "__main__":
    main()'''
    
    
    
    
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from deep_translator import GoogleTranslator

async def select_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("English", callback_data="en")],
        [InlineKeyboardButton("Spanish", callback_data="es")],
        # Add more languages as needed
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose target language:", reply_markup=markup)  # Fixed typo here (was reply_markup-markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data  # "en" / "es" etc.
    context.user_data["lang"] = lang
    await query.edit_message_text(f"Language set to {lang.upper()}.\nSend me any text")  # Fixed typo here (was .lnSend)

def lang_translator(text: str, dest_lang: str) -> str:
    return GoogleTranslator(source='auto', target=dest_lang).translate(text)

def main():
    application = Application.builder().token("7777797590:AAHsjGaCbP_xyEWDWlCpySLHoXgfNDpWASc").build()
    
    application.add_handler(CommandHandler('start', select_lang))
    application.add_handler(CallbackQueryHandler(button))
    
    application.run_polling()

if __name__ == '__main__':
    main()