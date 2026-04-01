import os
import logging
from telegram.ext import (
    Updater, CommandHandler, ConversationHandler, CallbackQueryHandler,
    MessageHandler, Filters, PicklePersistence
)

from constants import STATE_ANSWERING, STATE_CONTINUE_PROMPT
from handlers import (
    start_handler, ask_question_handler, check_answer_handler,
    list_updated_handler, prompt_continue_handler, send_gift_handler
)

# Setup basic logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def main() -> None:
    """Entrypoint string for the telegram bot logic"""
    # Fetch token from environment variables
    token = os.environ.get('TOKEN')
    
    if not token:
        logger.warning("No TOKEN environment variable provided! The bot might fail to start.")

    persistence = PicklePersistence(filename='boda_bot_memory.pickle')
    updater = Updater(token=token, use_context=True, persistence=persistence)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start_handler),
            CallbackQueryHandler(start_handler, pattern='^start_cb$') 
        ],
        states={
            STATE_ANSWERING: [
                CallbackQueryHandler(list_updated_handler, pattern='^completado$'),
                CallbackQueryHandler(send_gift_handler, pattern='^regalo$'),
                CallbackQueryHandler(ask_question_handler, pattern='^pregunta_[0-9]+$'),
                MessageHandler(Filters.text & ~Filters.command, check_answer_handler)
            ],
            STATE_CONTINUE_PROMPT: [
                MessageHandler(Filters.text & ~Filters.command, prompt_continue_handler)
            ]
        },
        fallbacks=[CommandHandler('start', start_handler)],
        name='boda_conversation',
        persistent=True
    )

    dp.add_handler(conv_handler)
    
    logger.info("Bot starting polling...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
