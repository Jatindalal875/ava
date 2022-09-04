import html
import random
import time

import legendRobot.modules.fun_strings as fun_strings
from legendRobot import dispatcher
from legendRobot.modules.disable import DisableAbleCommandHandler
from legendRobot.modules.helper_funcs.chat_status import is_user_admin
from legendRobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

def gbam(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "This person has been succesfully banned in 1800 chats. Took 3.9 sec to gban",
    )
    
    
GBAM_HANDLER = DisableAbleCommandHandler("gbam", gbam, run_async=True)

dispatcher.add_handler(GBAM_HANDLER)
