import logging
import asyncio
from random import random
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode, ChatAction
from telegram.ext import ContextTypes, ConversationHandler

from constants import (
    QUESTIONS_DATA, EMOJI_QUESTION, EMOJI_GIFT, EMOJI_STAR,
    EMOJI_CHECK, EMOJI_ERROR, EMOJI_SUN_FACE, EMOJI_DRUM, EMOJI_ANGRY,
    STICKER_GIFT_BALLOONS, STICKER_CORONAVIRUS, STICKER_RACCOON_PHONE,
    STATE_ANSWERING, STATE_CONTINUE_PROMPT,
    GIFT_IMAGE_PATH, WELCOME_PHRASE, get_acrostic_html
)

logger = logging.getLogger(__name__)

async def perform_typing_sleep(chat, extra_time: float = 0.0) -> None:
    """Helper function to simulate human typing delays asynchronously."""
    await chat.send_action(action=ChatAction.TYPING)
    await asyncio.sleep(random() + extra_time)

def generate_inline_keyboard(user_data: dict) -> InlineKeyboardMarkup:
    """Creates the inline keyboard dynamically based on completed questions."""
    completed = user_data.get('completed', set())
    keyboard = []
    row = []
    for i in range(14):
        button_text = EMOJI_CHECK if i in completed else str(i + 1)
        callback_data = 'completado' if i in completed else f'pregunta_{i}'
        row.append(InlineKeyboardButton(text=button_text, callback_data=callback_data))
        
        if len(row) == 5 or (len(row) == 4 and i >= 10):
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

def has_won_game(user_data: dict) -> bool:
    """Checks if the user has answered all questions."""
    return len(user_data.get('completed', set())) == 14

async def send_winning_message(chat) -> None:
    """Sends the grand prize message and button."""
    await perform_typing_sleep(chat, 2.0)
    btn_final = InlineKeyboardButton(text=f"Abrir regalo{EMOJI_GIFT}", callback_data='regalo')
    await chat.send_message(
        text=f"Mi sol {EMOJI_SUN_FACE}, has completado el juego. Pulsa en el siguiente botón para ver tus respuestas, juntas conforman el regalo final{EMOJI_DRUM}{EMOJI_DRUM}{EMOJI_DRUM}",
        reply_markup=InlineKeyboardMarkup([[btn_final]])
    )
    await perform_typing_sleep(chat, 0.0)
    await chat.send_sticker(sticker=STICKER_GIFT_BALLOONS)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Initializes the game and shows the dashboard."""
    chat = update.effective_chat
    user = update.effective_user

    # Verificación de Seguridad (Lista Blanca)
    from constants import ALLOWED_USERNAMES, ALLOWED_USER_IDS
    if user.username not in ALLOWED_USERNAMES and user.id not in ALLOWED_USER_IDS:
        logger.warning(f"Intruso detectado! UserID: {user.id}, Username: {user.username}")
        await chat.send_message(text="Lo siento, este bot contiene contenido sumamente privado y no estás autorizada(o) para interactuar con él.")
        return ConversationHandler.END

    context.user_data['completed'] = set()
    context.user_data['active_q'] = None

    await perform_typing_sleep(chat, 2.0)
    
    if update.message:
        await update.message.reply_text(text=WELCOME_PHRASE)
    else:
        await chat.send_message(text=WELCOME_PHRASE)
        
    await perform_typing_sleep(chat, 0.0)
    await chat.send_sticker(sticker=STICKER_CORONAVIRUS)
    
    await perform_typing_sleep(chat, 2.0)
    msg = f"Selecciona la pregunta que deseas contestar {EMOJI_QUESTION}, irás obteniendo premios {EMOJI_GIFT} a medida que avances, hasta lograr el PREMIO FINAL{EMOJI_STAR}"
    
    if update.message:
        await update.message.reply_text(text=msg, reply_markup=generate_inline_keyboard(context.user_data))
    else:
        await chat.send_message(text=msg, reply_markup=generate_inline_keyboard(context.user_data))
        
    return STATE_ANSWERING

async def restart_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Explicitly resets the progress and restarts the application."""
    chat = update.effective_chat
    user = update.effective_user
    
    # Verificación de Seguridad (Lista Blanca)
    from constants import ALLOWED_USERNAMES, ALLOWED_USER_IDS
    if user.username not in ALLOWED_USERNAMES and user.id not in ALLOWED_USER_IDS:
        return ConversationHandler.END

    await chat.send_message(text="🔄 Borrando toda la memoria y reiniciando el bot...")
    
    # Clear persistence data
    context.user_data['completed'] = set()
    context.user_data['active_q'] = None
    
    return await start_handler(update, context)

async def ask_question_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Sends the selected question to the user."""
    query = update.callback_query
    chat = query.message.chat
    
    question_idx = int(query.data.split('_')[1])
    context.user_data['active_q'] = question_idx
    
    await query.answer()
    try:
        await context.bot.delete_message(chat_id=chat.id, message_id=query.message.message_id)
    except Exception:
        pass

    question_data = QUESTIONS_DATA[question_idx]

    await perform_typing_sleep(chat, 2.0)
    await chat.send_message(text=question_data['question_text'])

    if 'pre_sticker' in question_data:
        await perform_typing_sleep(chat, 0.0)
        await chat.send_sticker(sticker=question_data['pre_sticker'])
    
    if 'audio_file' in question_data:
        await chat.send_action(action=ChatAction.UPLOAD_AUDIO)
        await asyncio.sleep(random() + 2.0)
        try:
            with open(question_data['audio_file'], 'rb') as audio:
                await chat.send_audio(audio=audio)
        except Exception as e:
            logger.error(f"Failed to send audio: {e}")
            await chat.send_message(text="_(No pude cargar el audio en el servidor)_", parse_mode=ParseMode.MARKDOWN)

    return STATE_ANSWERING

async def check_answer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Checks the user's answer against the active question's dictionary."""
    text = update.message.text.lower()
    chat = update.effective_chat
    question_idx = context.user_data.get('active_q')

    if question_idx is None:
        await chat.send_message(text=f"{EMOJI_ERROR} Selecciona una pregunta primero!")
        return STATE_ANSWERING
    
    question_data = QUESTIONS_DATA[question_idx]
    custom_hints = question_data.get('custom_hints', {})
    
    if text in custom_hints and text not in question_data['valid_answers']:
        await perform_typing_sleep(chat, 2.0)
        await chat.send_message(text=custom_hints[text])
        return STATE_ANSWERING
    
    if text in question_data['valid_answers'] or text in custom_hints: 
        context.user_data.setdefault('completed', set()).add(question_idx)

        await perform_typing_sleep(chat, 2.0)
        if text in custom_hints:
            await chat.send_message(text=custom_hints[text])
            await perform_typing_sleep(chat, 2.0)

        await chat.send_message(text=question_data['reward_phrase'])

        await perform_typing_sleep(chat, 0.0)
        await chat.send_sticker(sticker=question_data['reward_sticker'])

        if has_won_game(context.user_data):
            await send_winning_message(chat)
            return STATE_ANSWERING
        else:
            await perform_typing_sleep(chat, 2.0)
            await chat.send_message(
                text=f"Mi sol {EMOJI_SUN_FACE}, selecciona la pregunta que deseas contestar {EMOJI_QUESTION} o presiona sobre una ya respondida {EMOJI_CHECK} para ver tu estadística.",
                reply_markup=generate_inline_keyboard(context.user_data)
            )
            context.user_data['active_q'] = None
            return STATE_ANSWERING
    else:
        await perform_typing_sleep(chat, 2.0)
        await chat.send_message(text=f"{EMOJI_ERROR} Mi sol, fallaste. No pasa nada, vuelve a intentarlo")
        return STATE_ANSWERING

async def list_updated_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Shows current progress if user clicks an already completed question."""
    query = update.callback_query
    chat = query.message.chat
    
    await query.answer()
    try:
        await context.bot.delete_message(chat_id=chat.id, message_id=query.message.message_id)
    except Exception:
        pass
    
    if has_won_game(context.user_data):
        await perform_typing_sleep(chat, 2.0)
        await chat.send_message(text=get_acrostic_html(), parse_mode=ParseMode.HTML)
        return ConversationHandler.END

    completed_count = len(context.user_data.get('completed', set()))

    await perform_typing_sleep(chat, 2.0)
    await chat.send_message(text=f'Llevas {completed_count} respondida(s) de 14\n Para continuar escribe: Te amo')
    
    await perform_typing_sleep(chat, 0.0)
    await chat.send_sticker(sticker=STICKER_RACCOON_PHONE)
    
    return STATE_CONTINUE_PROMPT

async def prompt_continue_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Demands 'Te amo' to continue interacting."""
    text = update.message.text
    chat = update.effective_chat

    await perform_typing_sleep(chat, 1.0)

    if text.lower() == 'te amo':
        await chat.send_message(
            text=f"Mi sol {EMOJI_SUN_FACE}, selecciona la pregunta que deseas contestar {EMOJI_QUESTION} o presiona sobre una ya respondida {EMOJI_CHECK} para ver tu estadística.",
            reply_markup=generate_inline_keyboard(context.user_data)
        )
        context.user_data['active_q'] = None
        return STATE_ANSWERING
    else:
        await chat.send_message(text=f'Te dije que escribas *Te amo* {EMOJI_ANGRY}', parse_mode=ParseMode.MARKDOWN)
        return STATE_CONTINUE_PROMPT

async def send_gift_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Final callback to emit the gift and conclude the interaction."""
    query = update.callback_query
    chat = query.message.chat
    
    await query.answer()
    
    await chat.send_action(action=ChatAction.UPLOAD_PHOTO)
    await asyncio.sleep(random() + 1.0)
    try:
        with open(GIFT_IMAGE_PATH, 'rb') as photo:
            await chat.send_photo(photo=photo)
    except Exception as e:
        logger.error(f"Failed to send gift picture: {e}")

    await perform_typing_sleep(chat, 2.0)
    await chat.send_message(text=get_acrostic_html(), parse_mode=ParseMode.HTML)
    
    return ConversationHandler.END
