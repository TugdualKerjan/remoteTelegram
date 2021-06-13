# -*- coding: utf-8 -*-

import pyautogui
import time
import telegram
import dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultVideo, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, CallbackQueryHandler, InlineQueryHandler, ChosenInlineResultHandler
from telegram.error import NetworkError, Unauthorized

token = 
updater = Updater(token=token, use_context=True)


def main():
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
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

def start(update, context):
    print("A")
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""Hey! Press any buttons to simulate a keyboard on your computer running this program!""",
                             reply_markup=reply_keyboard
                             )


if __name__ == '__main__':
    main()
