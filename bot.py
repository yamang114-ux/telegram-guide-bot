
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

with open(".env", "r") as f:
    for line in f:
        if line.startswith("BOT_TOKEN="):
            os.environ["BOT_TOKEN"] = line.strip().split("=", 1)[1]

TOKEN = os.environ["BOT_TOKEN"]

keyboard = [
    ["📌 이용 안내", "❓ 자주 묻는 질문"],
    ["💬 문의하기"],
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "안녕하세요! 안내 봇입니다.\n\n"
        "아래 메뉴에서 원하는 항목을 선택해 주세요.",
        reply_markup=reply_markup,
    )


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    message = update.message.text

    if message == "📌 이용 안내":
        answer = (
            "📌 이용 안내\n\n"
            "이곳에 서비스 이용 안내를 추가할 수 있습니다."
        )
    elif message == "❓ 자주 묻는 질문":
        answer = (
            "❓ 자주 묻는 질문\n\n"
            "자주 묻는 질문과 답변을 이곳에 추가할 수 있습니다."
        )
    elif message == "💬 문의하기":
        answer = (
            "💬 문의하기\n\n"
            "문의 방법이나 담당자 연락처를 이곳에 추가할 수 있습니다."
        )
    else:
        answer = "아래 메뉴에서 원하는 항목을 선택해 주세요."

    await update.message.reply_text(
        answer,
        reply_markup=reply_markup,
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("안내 봇 실행 준비 완료!")
    app.run_polling()


if __name__ == "__main__":
    main()

