import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = os.environ.get('WEBAPP_URL')


def app_button(label: str, path: str = '') -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(label, url=f'{WEBAPP_URL}{path}')]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Welcome to EarnFlow!\n\nComplete tasks, answer surveys, play games and invite friends to earn rewards.\n\nYour earning journey starts here.',
        reply_markup=app_button('Open EarnFlow'),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('EarnFlow demo features:\n\nComplete tasks\nTake surveys\nPlay games\nRefer friends\nEarn coins\nRequest withdrawals')

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Your demo balance is available inside the EarnFlow app.', reply_markup=app_button('Open EarnFlow'))

async def tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Choose from app, survey, and game tasks in the demo marketplace.', reply_markup=app_button('Open Tasks', '#tasks'))

async def refer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Invite friends and explore the demo referral center.', reply_markup=app_button('Open Referral Center', '#referrals'))

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Demo withdrawals are available from the wallet inside EarnFlow.', reply_markup=app_button('Open Wallet', '#wallet'))


def main() -> None:
    if not TOKEN or not WEBAPP_URL:
        raise RuntimeError('BOT_TOKEN and WEBAPP_URL environment variables are required.')
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('balance', balance))
    application.add_handler(CommandHandler('tasks', tasks))
    application.add_handler(CommandHandler('refer', refer))
    application.add_handler(CommandHandler('withdraw', withdraw))
    application.run_polling()

if __name__ == '__main__':
    main()
