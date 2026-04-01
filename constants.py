from emoji import emojize

def e(code: str) -> str:
    """Helper to convert emoji aliases to actual emojis."""
    return emojize(code, language='alias')

# EMOJIS
EMOJI_HEART_EYES = e(":smiling_face_with_heart-eyes:")
EMOJI_TREE = e(":deciduous_tree:")
EMOJI_BOXING = e(":boxing_glove:")
EMOJI_LAUGH = e(":rolling_on_the_floor_laughing:")
EMOJI_WINE = e(":wine_glass:")
EMOJI_BOTTLE = e(":bottle_with_popping_cork:")
EMOJI_HEARTS = e(":smiling_face_with_hearts:")
EMOJI_GIFT = e(":wrapped_gift:")
EMOJI_COUPLE = e(":couple_with_heart_light_skin_tone:")
EMOJI_COOK = e(":man_cook_light_skin_tone:")
EMOJI_BOOK = e(":open_book:")
EMOJI_CALENDAR = e(":tear-off_calendar:")
EMOJI_BED = e(":person_in_bed_light_skin_tone:")
EMOJI_SLEEP = e(":zzz:")
EMOJI_GIRL = e(":girl_light_skin_tone:")
EMOJI_PHONE = e(":mobile_phone:")
EMOJI_TSHIRT = e(":t-shirt:")
EMOJI_HAND_DOWN = e(":backhand_index_pointing_down_light_skin_tone:")
EMOJI_STAR = e(":star:")
EMOJI_HEART = e(":beating_heart:")
EMOJI_SUNRISE = e(":sunrise_over_mountains:")
EMOJI_HANDS_OPEN = e(":open_hands_light_skin_tone:")
EMOJI_HUG = e(":hugging_face:")
EMOJI_ANXIOUS = e(":anxious_face_with_sweat:")
EMOJI_GLOBE = e(":globe_showing_Americas:")
EMOJI_SUN_FACE = e(":sun_with_face:")
EMOJI_KISS = e(":kiss_woman_man_light_skin_tone:")
EMOJI_SHRUG = e(":man_shrugging_light_skin_tone:")
EMOJI_THINKING = e(":thinking_face:")
EMOJI_SMILE = e(":beaming_face_with_smiling_eyes:")
EMOJI_BLOW_KISS = e(":face_blowing_a_kiss:")
EMOJI_MEDAL = e(":1st_place_medal:")
EMOJI_QUESTION = e(":white_question_mark:")
EMOJI_CHECK = e(":check_mark_button:")
EMOJI_ERROR = e(":red_exclamation_mark:")
EMOJI_DRUM = e(":drum:")
EMOJI_PLEAD = e(":pleading_face:")
EMOJI_ANGRY = e(":angry_face:")
EMOJI_STARS = e(":star-struck:")

# STICKERS
STICKER_RED_HEART = 'CAACAgEAAxkBAALHjmEekwydqEkZmdKwUQYZ6UqZVgEkAALJBwAC43gEAAGESQ6JsVOaWyAE'
STICKER_PINK_HEARTS = 'CAACAgEAAxkBAALHkmEeoGkmtvjIRh6LnfQ87rbyDBIcAAInCQAC43gEAAHtphXLedZInyAE'
STICKER_TURTLE_HEART = 'CAACAgIAAxkBAALHlmEeoG-z22z7CJFxLUv0sX1vtGKHAAIDAgACFkJrCnFL-7u_zLo2IAQ'
STICKER_BALLOON_HEART = 'CAACAgIAAxkBAALHmmEeoH6cXiX5_ZHmt9rjtIdZfMeXAAIXAwACVp29CueGLsTGVMUbIAQ'
STICKER_DOG_HEART = 'CAACAgEAAxkBAALHnmEeoIkRR6ESm2Oa8eCVEPaunanJAAL6AQACOA6CEZdviQ02NivYIAQ'
STICKER_RACCOON_PHONE = 'CAACAgIAAxkBAALHomEeoKCoCDtgst9KbD3jVXXa28zUAAJqAAPANk8T_puXe-wcB9ogBA'
STICKER_GIFT_BALLOONS = 'CAACAgIAAxkBAALHpmEeoMiOGyhe-CqMZKNyrv4m_PLlAAIdAwACVp29CsUyMGTteQ8TIAQ'
STICKER_SPINNING_GHOSTS = 'CAACAgIAAxkBAALHqmEeoNYm-YlfNA7GyHO-JiqrZCBYAAK_AAMw1J0RKfyKvCWU6UEgBA'
STICKER_IN_LOVE = 'CAACAgEAAxkBAALHrmEeoVimoshlyT2PJMto5tQKqTLbAAISCAAC43gEAAEbQgNRSx5bhCAE'
STICKER_CORONAVIRUS = 'CAACAgIAAxkBAALHsmEeoWuID97o8x9nCQmX24qGXXvKAALRAQACVp29CqqFfrYqby7MIAQ'
STICKER_GHOSTS_HEART = 'CAACAgIAAxkBAALHtmEeoanqGvF-3En2xqLzsUibk-EyAAK9AAMw1J0RnMLcRDVhgXsgBA'
STICKER_WORM_KISS = 'CAACAgIAAxkBAALHumEeobjVYn-IQSkRqPk1VadLIHRqAAJCAAMNttIZq3aSQSOvRu4gBA'
STICKER_WINE = 'CAACAgIAAxkBAALHwmEeoiVNwkPObSlTgcyWCNlXm0nfAAJDAQACMNSdEbGHK0mSHehHIAQ'
STICKER_CHOCOLATE = 'CAACAgIAAxkBAALHxmEeokdSnMEwB93y8557efZ2AAGuwAACYQMAArrAlQWtCQpcpHMj6yAE'
STICKER_FLOWERS = 'CAACAgIAAxkBAALHymEeolgEv6n47ySaKYG_VxDD5772AAJRAAMNttIZKsJ4HLTe1FogBA'
STICKER_BREAKINGBAD = 'CAACAgIAAxkBAALHzmEeoqEBpVK3wnParUM95oR1vZ9AAAJyAwACz1-LB5acJjQXFy8HIAQ'
STICKER_CAT_HEART = 'CAACAgIAAxkBAALH0mEeot9Ee_rXxmYsuIWGRQMcAAEz-QACMgADKA9qFGUiobSLpOJLIAQ'
STICKER_BALLOON_ARROW = 'CAACAgIAAxkBAALH1mEeovAmGKLhwbsq7gSrso-OeqJHAAIPAwACVp29CrL872DCyKzBIAQ'
STICKER_MUSIC = 'CAACAgIAAxkBAALH5mEewnz-0LvrJ0a5QQP8gPMj92wRAAJfXQACns4LAAGAft4dlnm2biAE'

QUESTIONS_DATA = [
    {
        'question_text': f"¿A qué lugar fuimos el día que nos hicimos novios?{EMOJI_HEART_EYES}",
        'valid_answers': ['todo en 1', 'todo en uno', 'todo por uno', 'todo por 1'],
        'reward_phrase': f"No somos perfectos, pero juntos hacemos un gran equipo.{EMOJI_COUPLE}",
        'reward_sticker': STICKER_RED_HEART
    },
    {
        'question_text': f"Lo siento por tus megas, pero quiero dedicarte esta canción {EMOJI_HAND_DOWN}. Después de escucharla dime qué plantaremos?{EMOJI_TREE}",
        'valid_answers': ['estrellas', 'estrella'],
        'reward_phrase': f"Todas las estrellas {EMOJI_STAR} de la galaxia nunca podrían eclipsar mi amor {EMOJI_HEART} por ti. Una vida de amaneceres {EMOJI_SUNRISE} no podrían compararse con la luz que traes a mi vida.{EMOJI_HEARTS}",
        'reward_sticker': STICKER_TURTLE_HEART,
        'audio_file': 'assets/romantic_song.mp3',
        'pre_sticker': STICKER_MUSIC
    },
    {
        'question_text': f"¿Cuándo jugamos de mano {EMOJI_BOXING}, qué no te gusta que te haga?{EMOJI_LAUGH}",
        'valid_answers': ['cosquillas', 'cosquilla'],
        'reward_phrase': f"Arriba las manos, {EMOJI_HANDS_OPEN} esto es un abrazo.{EMOJI_HUG}",
        'reward_sticker': STICKER_GHOSTS_HEART
    },
    {
        'question_text': f"La respuesta está en el fondo de la botella{EMOJI_BOTTLE}{EMOJI_WINE}",
        'valid_answers': ['adicto'],
        'reward_phrase': f"Mis temores {EMOJI_ANXIOUS} se marchan cada vez que me abrazas.{EMOJI_HUG}",
        'reward_sticker': STICKER_WINE
    },
    {
        'question_text': f"¿Cómo te digo cariñosamente?(en 1 palabra){EMOJI_HEARTS}",
        'valid_answers': ['sol', 'mi sol'],
        'reward_phrase': f"Tú eres la luz que ilumina mi mundo{EMOJI_GLOBE}, todo gira alrededor de ti.{EMOJI_SUN_FACE}",
        'reward_sticker': STICKER_PINK_HEARTS,
        'custom_hints': {
            'mi sol': "Respuesta correcta!!! Peeeero te dije que en una palabra, nos quedaremos sólo con 'Sol'. Seguimos",
            'amor': f"{EMOJI_ERROR} Es verdad que te digo así, pero hay otra forma que utilizo más. Vuélvelo a intentar\n PISTA: Te digo así porque mi mundo gira alrededor de ti, eres mi ...?",
            'mi amor': f"{EMOJI_ERROR} Es verdad que te digo así, pero hay otra forma que utilizo más. Vuélvelo a intentar\n PISTA: Te digo así porque mi mundo gira alrededor de ti, eres mi ...?"
        }
    },
    {
        'question_text': f"Respuesta escondida en tu regalo{EMOJI_GIFT}",
        'valid_answers': ['amor'],
        'reward_phrase': f"Amor de verdad {EMOJI_HEART} significa crecer juntos a través de las dificultades, aprender del otro y nunca renunciar al amor que nos unió.{EMOJI_COUPLE}",
        'reward_sticker': STICKER_BALLOON_HEART,
        'pre_sticker': STICKER_FLOWERS
    },
    {
        'question_text': f"¿Dónde fue nuestra primera cita solos?{EMOJI_COUPLE}",
        'valid_answers': ['studio', 'estudio', 'studio 55', 'estudio 55'],
        'reward_phrase': f"Te amo {EMOJI_HEART}, puedes leerlo hoy, mañana o el resto de la vida.{EMOJI_CALENDAR}",
        'reward_sticker': STICKER_SPINNING_GHOSTS,
        'custom_hints': {
            'estudio': "Respuesta correcta!!! Solo un detalle, el bar llama 'Studio 55', así lo dejaremos. Seguimos",
            'estudio 55': "Respuesta correcta!!! Solo un detalle, el bar llama 'Studio 55', así lo dejaremos. Seguimos"
        }
    },
    {
        'question_text': f"¿Cuál es tu sabor preferido?{EMOJI_COOK}",
        'valid_answers': ['chocolate', 'el chocolate'],
        'reward_phrase': f"No sé {EMOJI_SHRUG} hacia dónde vamos, pero sé que quiero ir contigo.{EMOJI_KISS}",
        'reward_sticker': STICKER_CHOCOLATE,
        'custom_hints': {
            'el chocolate': "Respuesta correcta!!! Solo un detalle, nos quedaremos con 'Chocolate'. Seguimos"
        }
    },
    {
        'question_text': f"¿Cuál es tu libro favorito?{EMOJI_BOOK}",
        'valid_answers': ['orgullo y prejuicio', 'orgullo y prejuicios'],
        'reward_phrase': f"Pensar en ti {EMOJI_THINKING} me hace sonreir.{EMOJI_SMILE}",
        'reward_sticker': STICKER_DOG_HEART
    },
    {
        'question_text': f"Nos botaron del ingles por...{EMOJI_LAUGH}",
        'valid_answers': ['no pagar', 'tacaños'],
        'reward_phrase': f"Tus éxitos serán mis éxitos {EMOJI_MEDAL}, tus derrotas serán mías también.{EMOJI_ANXIOUS}",
        'reward_sticker': STICKER_WORM_KISS,
        'custom_hints': {
            'tacaños': "Un poco feo eso no? Mejor digamos que por 'No pagar'. Suena mejor, seguimos"
        }
    },
    {
        'question_text': f"¿Qué día de la semana empezamos?{EMOJI_CALENDAR}",
        'valid_answers': ['miércoles', 'miercoles'],
        'reward_phrase': f"Y poco a poco te fuiste convirtiendo en la persona que quiero para el resto de mis días.{EMOJI_BLOW_KISS}",
        'reward_sticker': STICKER_IN_LOVE
    },
    {
        'question_text': f"¿De qué lado de la cama duermes casi siempre?{EMOJI_BED}{EMOJI_SLEEP}",
        'valid_answers': ['izquierdo', 'izquierda'],
        'reward_phrase': f"Gracias por llenar mi corazón {EMOJI_HEART} de alegría.{EMOJI_SMILE}",
        'reward_sticker': STICKER_BREAKINGBAD
    },
    {
        'question_text': f"Tendrás que llamar a mi hermana, ella tiene la respuesta{EMOJI_GIRL}{EMOJI_PHONE}",
        'valid_answers': ['gigante'],
        'reward_phrase': f"Haces que mi mundo {EMOJI_GLOBE} esté lleno de días inolvidables.{EMOJI_CALENDAR}",
        'reward_sticker': STICKER_BALLOON_ARROW
    },
    {
        'question_text': f"¿De qué color era mi pullover en nuestra salida de los 2 meses?(En inglés, lúcete){EMOJI_TSHIRT}",
        'valid_answers': ['orange'],
        'reward_phrase': f"Eres y  serás tú!{EMOJI_GIRL}",
        'reward_sticker': STICKER_CAT_HEART
    }
]

# States for ConversationHandler
STATE_ANSWERING = 1
STATE_CONTINUE_PROMPT = 2

# Final Gift Text Variables
GIFT_IMAGE_PATH = 'assets/gift_image.jpg'
WELCOME_PHRASE = f"Amor que rico cumplir un maravilloso mes más {EMOJI_CALENDAR} a tu lado {EMOJI_COUPLE}. Gracias por llegar a mi vida, por hacerla cada día mejor {EMOJI_SMILE}, gracias por apoyarme y escucharme, gracias por ser esa persona que necesito {EMOJI_HUG}, por estar conmigo siempre. Solo hazme un favor: No te vayas nunca.{EMOJI_BLOW_KISS}"

def get_acrostic_html() -> str:
    """Returns the formatted acrostic message directly embedded with emojis."""
    return (f"<b>T</b> <del>odo en 1</del>\n"
            f"<b>E</b> <del>strellas</del>\n\n"
            f"<b>C</b> <del>osquillas</del>\n"
            f"<b>A</b> <del>dicto</del>\n"
            f"<b>S</b> <del>ol</del>\n"
            f"<b>A</b> <del>mor</del>\n"
            f"<b>S</b> <del>tudio 55</del>\n\n"
            f"<b>C</b> <del>hocolate</del>\n"
            f"<b>O</b> <del>rgullo y prejuicio</del>\n"
            f"<b>N</b> <del>o pagar</del>\n"
            f"<b>M</b> <del>iércoles</del>\n"
            f"<b> I</b>  <del>zquierdo</del>\n"
            f"<b>G</b> <del>igante</del>\n"
            f"<b>O</b> <del>range</del>\n"
            f"<b>?</b> Di que si {EMOJI_PLEAD}")

import os

# Security Whitelist Configurations.
# We pull these from the environment natively. If they don't exist, they fallback to your defaults.
_names_raw = os.environ.get('ALLOWED_USERNAMES', 'malen1996')
ALLOWED_USERNAMES = [name.strip() for name in _names_raw.split(',') if name.strip()]  

_ids_raw = os.environ.get('ALLOWED_USER_IDS', '954029741,631792877')
ALLOWED_USER_IDS = [int(idx.strip()) for idx in _ids_raw.split(',') if idx.strip()]

