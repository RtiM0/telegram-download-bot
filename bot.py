import logging
from shutil import move

from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "BOT-TOKEN"
BASE_URL = "http://localhost:8081/bot"
OUTPUT_DIR = "/home/potato/tgdownloadbot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!"
    )

async def downloader(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Downloading!")
    document = update.message.document
    file = await context.bot.get_file(document)
    await update.message.reply_text(f"File {document.file_name} downloaded.\nNow moving.")
    move(file.file_path.lstrip(TOKEN),f"{OUTPUT_DIR}{document.file_name}")
    await update.message.reply_text(f"File moved.\nLocation: {OUTPUT_DIR}{document.file_name}")


def main() -> None:
    application = Application.builder().token(TOKEN).base_url(BASE_URL).base_file_url("").read_timeout(864000).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, downloader))
    application.run_polling()



if __name__ == "__main__":
    main()
