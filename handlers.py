import logging

from telegram import Update
from telegram.ext import CallbackContext

import data
import meravis
from data import curr_level, curr_gold, curr_unspent


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=data.help_text)


def handleLevel(update: Update, context: CallbackContext):
    logging.info(curr_level)
    level = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{curr_level} {level}')


def handleGold(update: Update, context: CallbackContext):
    logging.info(curr_gold)
    gold = None
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{curr_gold} {gold}')

def handleMeravis(update: Update, context: CallbackContext):
    logging.info("Meravis")
    findings = meravis.scan_site()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{findings}')

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
    elif 'meravis' in incoming_message_lower:
        handleMeravis(update, context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=data.error_text + "\n" + data.help_text)
