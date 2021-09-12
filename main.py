# -*- coding: utf-8 -*-

import pyautogui
import time
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler


#after obtaining your token from https://telegram.me/botfather,
#paste it right here
token = "secret_here"
updater = Updater(token=token, use_context=True)


def main():
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', help))

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('exit', kill))

    dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    print('Running!')

    updater.start_polling()


def callback_handler(update, context):
    data = update.callback_query.data
    if data == "left":
        pyautogui.press('left')
    if data == "right":
        pyautogui.press('right')
    if data == "space":
        pyautogui.press('space')

    context.bot.answerCallbackQuery(
        callback_query_id=update.callback_query.id, text="Pressed!")


reply_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️", None, "left"),
     InlineKeyboardButton("▶️", None, "right")],
    [InlineKeyboardButton("⏯️", None, "space")]])

def kill(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""Closing bot.""",
                             reply_markup=None
                             )
    exit()
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="/exit to close the bot,\n/start to start the remote control fun",
                             reply_markup=None
                             )
    exit()
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hey! Press any buttons to simulate a keyboard on your computer running this program!\n /help \n exit",
                             reply_markup=reply_keyboard
                             )


if __name__ == '__main__':
    main()
