from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

import config.config as cfg
import kf_logging
import meravis
from handlers import freeTextHandler

updater = Updater(token=cfg.API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
queue = updater.job_queue


def registerHandlers():
    echo_handler = MessageHandler(Filters.text & (~Filters.command), freeTextHandler)
    dispatcher.add_handler(echo_handler)


def startUpdater():
    updater.start_polling(1)
    updater.idle()


def send_meravis_information(context):
    findings = meravis.scan_site()
    context.bot.send_message(chat_id=cfg.USER_ID,
                             text=findings)


meravis_daily_news = queue.run_repeating(send_meravis_information, interval=24 * 60 * 60, first=1)

kf_logging.start_logging()
registerHandlers()
startUpdater()
