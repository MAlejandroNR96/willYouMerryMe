import os
import logging
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, CallbackQueryHandler,
    MessageHandler, filters, PicklePersistence
)

from constants import STATE_ANSWERING, STATE_CONTINUE_PROMPT
from handlers import (
    start_handler, ask_question_handler, check_answer_handler,
    list_updated_handler, prompt_continue_handler, send_gift_handler,
    restart_handler
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
    """Entrypoint string for the telegram bot logic using ApplicationBuilder (v20+)"""
    # Fetch token from environment variables
    token = os.environ.get('TOKEN')
    
    if not token:
        logger.warning("No TOKEN environment variable provided! The bot might fail to start.")
        return

    persistence = PicklePersistence(filepath='boda_bot_memory.pickle')
    
    # Build asynchronous application
    application = ApplicationBuilder().token(token).persistence(persistence).build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start_handler),
            CommandHandler('restart', restart_handler),
            CallbackQueryHandler(start_handler, pattern='^start_cb$') 
        ],
        states={
            STATE_ANSWERING: [
                CallbackQueryHandler(list_updated_handler, pattern='^completado$'),
                CallbackQueryHandler(send_gift_handler, pattern='^regalo$'),
                CallbackQueryHandler(ask_question_handler, pattern='^pregunta_[0-9]+$'),
                MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer_handler)
            ],
            STATE_CONTINUE_PROMPT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, prompt_continue_handler)
            ]
        },
        fallbacks=[
            CommandHandler('start', start_handler),
            CommandHandler('restart', restart_handler)
        ],
        name='boda_conversation',
        persistent=True
    )

    application.add_handler(conv_handler)
    
    logger.info("Bot starting polling asymmetrically...")
    application.run_polling()

if __name__ == '__main__':
    main()
