import logging

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

import config.config as cfg

curr_level = "Your current level is "
curr_gold = "Your current gold amount is "
curr_unspent = "You currently have "

updater = Updater(token=cfg.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, welcome  to your knightfight bot!\n"
                                                                    "/level to show your current level\n"
                                                                    "/gold to show your amount of gold\n"
                                                                    "/unspent to show your unspent skill points"
                             )


def handleLevel(update: Update, context: CallbackContext):
    logging.info(curr_level)
    level = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{curr_level} {level}')


def handleGold(update: Update, context: CallbackContext):
    logging.info(curr_gold)
    gold = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{curr_gold} {gold}')


def handleUnspent(update: Update, context: CallbackContext):
    logging.info(curr_unspent)
    unspent = 0
    if unspent > 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{curr_unspent} {unspent} skill points')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"You don't have any unspent skill points")


def freeTextHandler(update: Update, context: CallbackContext):
    incoming_message_lower = update.message.text.lower()
    if 'level' in incoming_message_lower:
        handleLevel(update, context)
    elif 'gold' in incoming_message_lower:
        handleGold(update, context)
    elif 'unspent' in incoming_message_lower:
        handleUnspent(update, context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry bro, didn't get that")


def registerHandlers():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    level_handler = CommandHandler('level', handleLevel)
    dispatcher.add_handler(level_handler)

    gold_handler = CommandHandler('gold', handleGold)
    dispatcher.add_handler(gold_handler)

    unspent_handler = CommandHandler('unspent', handleUnspent)
    dispatcher.add_handler(unspent_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), freeTextHandler)
    dispatcher.add_handler(echo_handler)


def startUpdater():
    updater.start_polling(1)
    updater.idle()


import argparse

parser = argparse.ArgumentParser(description='Create Configuration')
parser.add_argument('--log', type=str, help='Loglevel',
                    default="WARNING")

args = parser.parse_args()
getattr(logging, args.log.upper())
numeric_level = getattr(logging, args.log.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % args.log)
logging.basicConfig(level=numeric_level)
logging.info("Starting application")
registerHandlers()
startUpdater()
