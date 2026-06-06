import os
import json
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from agent import AssetRequestAgent
from database import (
    init_db,
    save_request,
    get_all_requests,
    
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Store one agent per user
user_sessions = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    agent = AssetRequestAgent()
    user_sessions[user_id] = agent

    await update.message.reply_text(
        "🤖 Asset Request Bot\n\n" + agent.start_conversation()
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text

    if user_id not in user_sessions:
        agent = AssetRequestAgent()
        user_sessions[user_id] = agent
        await update.message.reply_text(agent.start_conversation())
        return

    agent = user_sessions[user_id]

    result = agent.process_input(message)

    if isinstance(result, dict):
        
        save_request(result)
        await update.message.reply_text(
        f"""
✅ Request Saved to SQLite

Request ID: {result['request_id']}
Employee ID: {result['employee_id']}
Asset Type: {result['asset_type']}
Asset Name: {result['asset_name']}
Status: {result['status']}
"""
    )
        del user_sessions[user_id]

    else:
        await update.message.reply_text(result)

async def requests_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rows = get_all_requests()

    if not rows:
        await update.message.reply_text("No requests found.")
        return

    message = "📋 Asset Requests\n\n"

    for row in rows:
        message += (
            f"ID: {row[1]}\n"
            f"Employee: {row[2]}\n"
            f"Asset: {row[3]}\n"
            f"Status: {row[6]}\n\n"
        )

    await update.message.reply_text(message)



def main():
    init_db()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("requests", requests_cmd))
    

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🚀 Asset Request Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()