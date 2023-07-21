from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

import config.config as cfg
import kf_logging
from handlers import freeTextHandler

updater = Updater(token=cfg.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def registerHandlers():
    # Example usage of command handlers
    # start_handler = CommandHandler('start', start)
    # dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), freeTextHandler)
    dispatcher.add_handler(echo_handler)


def startUpdater():
    updater.start_polling(1)
    updater.idle()


kf_logging.start_logging()
registerHandlers()
startUpdater()
