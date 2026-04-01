import logging
from time import sleep
from random import random
from telegram import Update, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CallbackContext, ConversationHandler

from constants import (
    QUESTIONS_DATA, EMOJI_QUESTION, EMOJI_GIFT, EMOJI_STAR,
    EMOJI_CHECK, EMOJI_ERROR, EMOJI_SUN_FACE, EMOJI_DRUM, EMOJI_ANGRY,
    STICKER_GIFT_BALLOONS, STICKER_CORONAVIRUS, STICKER_RACCOON_PHONE,
    STATE_ANSWERING, STATE_CONTINUE_PROMPT,
    GIFT_IMAGE_PATH, WELCOME_PHRASE, get_acrostic_html
)

logger = logging.getLogger(__name__)

def perform_typing_sleep(chat, extra_time: float = 0.0) -> None:
    """Helper function to simulate human typing delays."""
    chat.send_action(action=ChatAction.TYPING)
    sleep(random() + extra_time)

def generate_inline_keyboard(user_data: dict) -> InlineKeyboardMarkup:
    """Creates the inline keyboard dynamically based on completed questions."""
    completed = user_data.get('completed', set())
    keyboard = []
    row = []
    for i in range(14):
        button_text = EMOJI_CHECK if i in completed else str(i + 1)
        callback_data = 'completado' if i in completed else f'pregunta_{i}'
        row.append(InlineKeyboardButton(text=button_text, callback_data=callback_data))
        
        # Format keyboard into rows of 5, then 5, then 4.
        if len(row) == 5 or (len(row) == 4 and i >= 10):
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

def has_won_game(user_data: dict) -> bool:
    """Checks if the user has answered all questions."""
    return len(user_data.get('completed', set())) == 14

def send_winning_message(chat) -> None:
    """Sends the grand prize message and button."""
    perform_typing_sleep(chat, 2.0)
    btn_final = InlineKeyboardButton(text=f"Abrir regalo{EMOJI_GIFT}", callback_data='regalo')
    chat.send_message(
        f"Mi sol {EMOJI_SUN_FACE}, has completado el juego. Pulsa en el siguiente botón para ver tus respuestas, juntas conforman el regalo final{EMOJI_DRUM}{EMOJI_DRUM}{EMOJI_DRUM}",
        reply_markup=InlineKeyboardMarkup([[btn_final]])
    )
    perform_typing_sleep(chat, 0.0)
    chat.send_sticker(STICKER_GIFT_BALLOONS)

def start_handler(update: Update, context: CallbackContext) -> int:
    """Initializes the game and shows the dashboard."""
    chat = update.effective_chat
    user = update.effective_user

    # Verificación de Seguridad (Lista Blanca)
    from constants import ALLOWED_USERNAMES, ALLOWED_USER_IDS
    if user.username not in ALLOWED_USERNAMES and user.id not in ALLOWED_USER_IDS:
        logger.warning(f"Intruso detectado! UserID: {user.id}, Username: {user.username}")
        chat.send_message("Lo siento, este bot contiene contenido sumamente privado y no estás autorizada(o) para interactuar con él.")
        return ConversationHandler.END

    context.user_data['completed'] = set()
    context.user_data['active_q'] = None

    perform_typing_sleep(chat, 2.0)
    update.message.reply_text(WELCOME_PHRASE)
    perform_typing_sleep(chat, 0.0)
    chat.send_sticker(STICKER_CORONAVIRUS)
    
    perform_typing_sleep(chat, 2.0)
    update.message.reply_text(
        f"Selecciona la pregunta que deseas contestar {EMOJI_QUESTION}, irás obteniendo premios {EMOJI_GIFT} a medida que avances, hasta lograr el PREMIO FINAL{EMOJI_STAR}",
        reply_markup=generate_inline_keyboard(context.user_data)
    )
    return STATE_ANSWERING

def restart_handler(update: Update, context: CallbackContext) -> int:
    """Explicitly resets the progress and restarts the application."""
    chat = update.effective_chat
    user = update.effective_user
    
    # Verificación de Seguridad (Lista Blanca)
    from constants import ALLOWED_USERNAMES, ALLOWED_USER_IDS
    if user.username not in ALLOWED_USERNAMES and user.id not in ALLOWED_USER_IDS:
        return ConversationHandler.END

    chat.send_message("🔄 Borrando toda la memoria y reiniciando el bot...")
    
    # Clear persistence data simply by clearing our user_data components
    context.user_data['completed'] = set()
    context.user_data['active_q'] = None
    
    return start_handler(update, context)

def ask_question_handler(update: Update, context: CallbackContext) -> int:
    """Sends the selected question to the user."""
    query = update.callback_query
    chat = query.message.chat
    
    question_idx = int(query.data.split('_')[1])
    context.user_data['active_q'] = question_idx
    
    context.bot.delete_message(chat_id=chat.id, message_id=query.message.message_id)

    question_data = QUESTIONS_DATA[question_idx]

    perform_typing_sleep(chat, 2.0)
    chat.send_message(text=question_data['question_text'])

    if 'pre_sticker' in question_data:
        perform_typing_sleep(chat, 0.0)
        chat.send_sticker(question_data['pre_sticker'])
    
    if 'audio_file' in question_data:
        chat.send_action(action=ChatAction.UPLOAD_AUDIO)
        sleep(random() + 2.0)
        try:
            with open(question_data['audio_file'], 'rb') as audio:
                chat.send_audio(audio=audio)
        except Exception as e:
            logger.error(f"Failed to send audio: {e}")
            chat.send_message("_(No pude cargar el audio en el servidor)_", parse_mode=ParseMode.MARKDOWN)

    return STATE_ANSWERING

def check_answer_handler(update: Update, context: CallbackContext) -> int:
    """Checks the user's answer against the active question's dictionary."""
    text = update.message.text.lower()
    chat = update.effective_chat
    question_idx = context.user_data.get('active_q')

    if question_idx is None:
        chat.send_message(f"{EMOJI_ERROR} Selecciona una pregunta primero!")
        return STATE_ANSWERING
    
    question_data = QUESTIONS_DATA[question_idx]
    custom_hints = question_data.get('custom_hints', {})
    
    # Check if answer is a known "almost correct" hint
    if text in custom_hints and text not in question_data['valid_answers']:
        perform_typing_sleep(chat, 2.0)
        chat.send_message(text=custom_hints[text])
        return STATE_ANSWERING
    
    # If correct or triggers special valid response
    if text in question_data['valid_answers'] or text in custom_hints: 
        context.user_data.setdefault('completed', set()).add(question_idx)

        perform_typing_sleep(chat, 2.0)
        if text in custom_hints:
            chat.send_message(text=custom_hints[text])
            perform_typing_sleep(chat, 2.0)

        chat.send_message(text=question_data['reward_phrase'])

        perform_typing_sleep(chat, 0.0)
        chat.send_sticker(question_data['reward_sticker'])

        if has_won_game(context.user_data):
            send_winning_message(chat)
            return STATE_ANSWERING
        else:
            perform_typing_sleep(chat, 2.0)
            chat.send_message(
                f"Mi sol {EMOJI_SUN_FACE}, selecciona la pregunta que deseas contestar {EMOJI_QUESTION} o presiona sobre una ya respondida {EMOJI_CHECK} para ver tu estadística.",
                reply_markup=generate_inline_keyboard(context.user_data)
            )
            context.user_data['active_q'] = None
            return STATE_ANSWERING
    else:
        # Invalid response
        perform_typing_sleep(chat, 2.0)
        chat.send_message(text=f"{EMOJI_ERROR} Mi sol, fallaste. No pasa nada, vuelve a intentarlo")
        return STATE_ANSWERING

def list_updated_handler(update: Update, context: CallbackContext) -> int:
    """Shows current progress if user clicks an already completed question."""
    query = update.callback_query
    chat = query.message.chat
    context.bot.delete_message(chat_id=chat.id, message_id=query.message.message_id)
    
    if has_won_game(context.user_data):
        perform_typing_sleep(chat, 2.0)
        chat.send_message(get_acrostic_html(), parse_mode=ParseMode.HTML)
        return ConversationHandler.END

    completed_count = len(context.user_data.get('completed', set()))

    perform_typing_sleep(chat, 2.0)
    chat.send_message(text=f'Llevas {completed_count} respondida(s) de 14\n Para continuar escribe: Te amo')
    
    perform_typing_sleep(chat, 0.0)
    chat.send_sticker(STICKER_RACCOON_PHONE)
    
    return STATE_CONTINUE_PROMPT

def prompt_continue_handler(update: Update, context: CallbackContext) -> int:
    """Demands 'Te amo' to continue interacting."""
    text = update.message.text
    chat = update.effective_chat

    perform_typing_sleep(chat, 1.0)

    if text.lower() == 'te amo':
        chat.send_message(
            f"Mi sol {EMOJI_SUN_FACE}, selecciona la pregunta que deseas contestar {EMOJI_QUESTION} o presiona sobre una ya respondida {EMOJI_CHECK} para ver tu estadística.",
            reply_markup=generate_inline_keyboard(context.user_data)
        )
        context.user_data['active_q'] = None
        return STATE_ANSWERING
    else:
        chat.send_message(text=f'Te dije que escribas *Te amo* {EMOJI_ANGRY}', parse_mode=ParseMode.MARKDOWN)
        return STATE_CONTINUE_PROMPT

def send_gift_handler(update: Update, context: CallbackContext) -> int:
    """Final callback to emit the gift and conclude the interaction."""
    query = update.callback_query
    chat = query.message.chat
    
    chat.send_action(action=ChatAction.UPLOAD_PHOTO)
    sleep(random() + 1.0)
    try:
        with open(GIFT_IMAGE_PATH, 'rb') as photo:
            chat.send_photo(photo=photo)
    except Exception as e:
        logger.error(f"Failed to send gift picture: {e}")

    perform_typing_sleep(chat, 2.0)
    chat.send_message(get_acrostic_html(), parse_mode=ParseMode.HTML)
    
    return ConversationHandler.END
