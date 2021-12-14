from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import config.config as cfg

updater = Updater(token=cfg.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, welcome  to your knightfight bot!\n"
                                                                    "/level to show your current level\n"
                                                                    "/gold to show your amount of gold\n"
                                                                    "/unspent to show your unspent skill points"
                             )

def handleLevel(update: Update, context: CallbackContext):
    level = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your current level is {level}')

def handleGold(update: Update, context: CallbackContext):
        gold = None
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your current gold amount is {gold}')

def handleUnspent(update: Update, context: CallbackContext):
        unspent = 0
        if unspent > 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'You currently have {unspent} skill points')
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

registerHandlers()
startUpdater()
