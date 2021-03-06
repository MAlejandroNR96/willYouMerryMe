from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from emoji import emojize
import os
from time import sleep
from random import random

CHAT_ID=0
PREGUNTA1 = 1
PREGUNTA2 = 2
PREGUNTA3 = 3
PREGUNTA4 = 4
PREGUNTA5 = 5
PREGUNTA6 = 6
PREGUNTA7 = 7
PREGUNTA8 = 8
PREGUNTA9 = 9
PREGUNTA10 = 10
PREGUNTA11 = 11
PREGUNTA12 = 12
PREGUNTA13 = 13
PREGUNTA14 = 14
CONTINUAR=15
FINAL=16

button1 = InlineKeyboardButton(
    text=emojize("1", use_aliases=True), callback_data='pregunta1')
button2 = InlineKeyboardButton(
    text=emojize("2", use_aliases=True), callback_data='pregunta2')
button3 = InlineKeyboardButton(
    text=emojize("3", use_aliases=True), callback_data='pregunta3')
button4 = InlineKeyboardButton(
    text=emojize("4", use_aliases=True), callback_data='pregunta4')
button5 = InlineKeyboardButton(
    text=emojize("5", use_aliases=True), callback_data='pregunta5')
button6 = InlineKeyboardButton(
    text=emojize("6", use_aliases=True), callback_data='pregunta6')
button7 = InlineKeyboardButton(
    text=emojize("7", use_aliases=True), callback_data='pregunta7')
button8 = InlineKeyboardButton(
    text=emojize("8", use_aliases=True), callback_data='pregunta8')
button9 = InlineKeyboardButton(
    text=emojize("9", use_aliases=True), callback_data='pregunta9')
button10 = InlineKeyboardButton(
    text=emojize("10", use_aliases=True), callback_data='pregunta10')
button11 = InlineKeyboardButton(
    text=emojize("11", use_aliases=True), callback_data='pregunta11')
button12 = InlineKeyboardButton(
    text=emojize("12", use_aliases=True), callback_data='pregunta12')
button13 = InlineKeyboardButton(
    text=emojize("13", use_aliases=True), callback_data='pregunta13')
button14 = InlineKeyboardButton(
    text=emojize("14", use_aliases=True), callback_data='pregunta14')

emoji_enamorado=text=emojize(":smiling_face_with_heart-eyes:")
emoji_matica=text=emojize(":deciduous_tree:")
emoji_boxeo=text=emojize(":boxing_glove:")
emoji_risa=text=emojize(":rolling_on_the_floor_laughing:")
emoji_vino=text=emojize(":wine_glass:")
emoji_botella=text=emojize(":bottle_with_popping_cork:")
emoji_carinoso=text=emojize(":smiling_face_with_hearts:")
emoji_regalo=text=emojize(":wrapped_gift:")
emoji_cita=text=emojize(":couple_with_heart_light_skin_tone:")
emoji_sabor=text=emojize(":man_cook_light_skin_tone:")
emoji_libro=text=emojize(":open_book:")
emoji_calendar=text=emojize(":tear-off_calendar:")
emoji_cama=text=emojize(":person_in_bed_light_skin_tone:")
emoji_dormir=text=emojize(":zzz:")
emoji_girl=text=emojize(":girl_light_skin_tone:")
emoji_phone=text=emojize(":mobile_phone:")
emoji_pullover=text=emojize(":t-shirt:")
emoji_mano=text=emojize(":backhand_index_pointing_down_light_skin_tone:")
emoji_star=text=emojize(":star:")
emoji_heart=text=emojize(":beating_heart:")
emoji_amanecer=text=emojize(":sunrise_over_mountains:")
emoji_hands=text=emojize(":open_hands_light_skin_tone:")
emoji_hug=text=emojize(":hugging_face:")
emoji_miedo=text=emojize(":anxious_face_with_sweat:")
emoji_mundo=text=emojize(":globe_showing_Americas:")
emoji_sun=text=emojize(":sun_with_face:")
emoji_otro=text=emojize(":kiss_woman_man_light_skin_tone:")
emoji_nose=text=emojize(":man_shrugging_light_skin_tone:")
emoji_pensar=text=emojize(":thinking_face:")
emoji_sonreir=text=emojize(":beaming_face_with_smiling_eyes:")
emoji_beso=text=emojize(":face_blowing_a_kiss:")
emoji_medalla=text=emojize(":1st_place_medal:")
emoji_pregunta=text=emojize(":white_question_mark:")


sticker_corazon_rojo='CAACAgEAAxkBAALHjmEekwydqEkZmdKwUQYZ6UqZVgEkAALJBwAC43gEAAGESQ6JsVOaWyAE'
sticker_varios_corazones_rosas='CAACAgEAAxkBAALHkmEeoGkmtvjIRh6LnfQ87rbyDBIcAAInCQAC43gEAAHtphXLedZInyAE'
sticker_toruga_corazon='CAACAgIAAxkBAALHlmEeoG-z22z7CJFxLUv0sX1vtGKHAAIDAgACFkJrCnFL-7u_zLo2IAQ'
sticker_golbo_corazon_rojo='CAACAgIAAxkBAALHmmEeoH6cXiX5_ZHmt9rjtIdZfMeXAAIXAwACVp29CueGLsTGVMUbIAQ'
sticker_perro_corazon='CAACAgEAAxkBAALHnmEeoIkRR6ESm2Oa8eCVEPaunanJAAL6AQACOA6CEZdviQ02NivYIAQ'
sticker_mapache_telefono='CAACAgIAAxkBAALHomEeoKCoCDtgst9KbD3jVXXa28zUAAJqAAPANk8T_puXe-wcB9ogBA'
sticker_regalo_globos='CAACAgIAAxkBAALHpmEeoMiOGyhe-CqMZKNyrv4m_PLlAAIdAwACVp29CsUyMGTteQ8TIAQ'
sticker_fantasmas_girando='CAACAgIAAxkBAALHqmEeoNYm-YlfNA7GyHO-JiqrZCBYAAK_AAMw1J0RKfyKvCWU6UEgBA'
sticker_enamorado='CAACAgEAAxkBAALHrmEeoVimoshlyT2PJMto5tQKqTLbAAISCAAC43gEAAEbQgNRSx5bhCAE'
sticker_coronavirus='CAACAgIAAxkBAALHsmEeoWuID97o8x9nCQmX24qGXXvKAALRAQACVp29CqqFfrYqby7MIAQ'
sticker_fantasmas_corazon='CAACAgIAAxkBAALHtmEeoanqGvF-3En2xqLzsUibk-EyAAK9AAMw1J0RnMLcRDVhgXsgBA'
sticker_gusano_beso='CAACAgIAAxkBAALHumEeobjVYn-IQSkRqPk1VadLIHRqAAJCAAMNttIZq3aSQSOvRu4gBA'
sticker_vino='CAACAgIAAxkBAALHwmEeoiVNwkPObSlTgcyWCNlXm0nfAAJDAQACMNSdEbGHK0mSHehHIAQ'
sticker_chocolate='CAACAgIAAxkBAALHxmEeokdSnMEwB93y8557efZ2AAGuwAACYQMAArrAlQWtCQpcpHMj6yAE'
sticker_flores='CAACAgIAAxkBAALHymEeolgEv6n47ySaKYG_VxDD5772AAJRAAMNttIZKsJ4HLTe1FogBA'
sticker_breakingbad='CAACAgIAAxkBAALHzmEeoqEBpVK3wnParUM95oR1vZ9AAAJyAwACz1-LB5acJjQXFy8HIAQ'
sticker_gato_corazon='CAACAgIAAxkBAALH0mEeot9Ee_rXxmYsuIWGRQMcAAEz-QACMgADKA9qFGUiobSLpOJLIAQ'
sticker_globo_flechazo='CAACAgIAAxkBAALH1mEeovAmGKLhwbsq7gSrso-OeqJHAAIPAwACVp29CrL872DCyKzBIAQ'
sticker_musica='CAACAgIAAxkBAALH5mEewnz-0LvrJ0a5QQP8gPMj92wRAAJfXQACns4LAAGAft4dlnm2biAE'

PREGUNTAS = [
    {'nombre': 'pregunta1', 'pregunta': "??A qu?? lugar fuimos el d??a que nos hicimos novios?"+emoji_enamorado, 'completado': False},
    {'nombre': 'pregunta2', 'pregunta': "Lo siento por tus megas, pero quiero dedicarte esta canci??n "+emoji_mano+". Despu??s de escucharla dime qu?? plantaremos?"+emoji_matica, 'completado': False},
    {'nombre': 'pregunta3', 'pregunta': "??Cu??ndo jugamos de mano "+emoji_boxeo+", qu?? no te gusta que te haga?"+emoji_risa, 'completado': False},
    {'nombre': 'pregunta4', 'pregunta': "La respuesta est?? en el fondo de la botella"+emoji_botella+emoji_vino, 'completado': False},
    {'nombre': 'pregunta5', 'pregunta': "??C??mo te digo cari??osamente?(en 1 palabra)"+emoji_carinoso, 'completado': False},
    {'nombre': 'pregunta6', 'pregunta': "Respuesta escondida en tu regalo"+emoji_regalo, 'completado': False},
    {'nombre': 'pregunta7', 'pregunta': "??D??nde fue nuestra primera cita solos?"+emoji_cita, 'completado': False},
    {'nombre': 'pregunta8', 'pregunta': "??Cu??l es tu sabor preferido?"+emoji_sabor, 'completado': False},
    {'nombre': 'pregunta9', 'pregunta': "??Cu??l es tu libro favorito?"+emoji_libro, 'completado': False},
    {'nombre': 'pregunta10', 'pregunta': "Nos botaron del ingles por..."+emoji_risa, 'completado': False},
    {'nombre': 'pregunta11', 'pregunta': "??Qu?? d??a de la semana empezamos?"+emoji_calendar, 'completado': False},
    {'nombre': 'pregunta12', 'pregunta': "??De qu?? lado de la cama duermes casi siempre?"+emoji_cama+emoji_dormir, 'completado': False},
    {'nombre': 'pregunta13', 'pregunta': "Tendr??s que llamar a mi hermana, ella tiene la respuesta"+emoji_girl+emoji_phone, 'completado': False},
    {'nombre': 'pregunta14', 'pregunta': "??De qu?? color era mi pullover en nuestra salida de los 2 meses?(En ingl??s, l??cete)"+emoji_pullover, 'completado': False},
]

RESPUESTAS_CORRECTAS = [
    'todo en 1',
    'estrellas',
    'cosquillas',
    'adicto',
    'sol',
    'amor',
    'studio',
    'chocolate',
    'orgullo y prejuicio',
    'no pagar',
    'mi??rcoles',
    'izquierdo',
    'gigante',
    'orange',
]

FRASES = [
    'No somos perfectos, pero juntos hacemos un gran equipo.'+emoji_cita,
    'Todas las estrellas '+emoji_star+' de la galaxia nunca podr??an eclipsar mi amor '+emoji_heart+' por ti. Una vida de amaneceres '+emoji_amanecer+' no podr??an compararse con la luz que traes a mi vida.'+emoji_carinoso,
    'Arriba las manos, '+emoji_hands+' esto es un abrazo.'+emoji_hug,
    'Mis temores '+emoji_miedo+' se marchan cada vez que me abrazas.'+emoji_hug,
    'T?? eres la luz que ilumina mi mundo'+emoji_mundo+', todo gira alrededor de ti.'+emoji_sun,
    'Amor de verdad '+emoji_heart+' significa crecer juntos a trav??s de las dificultades, aprender del otro y nunca renunciar al amor que nos uni??.'+emoji_cita,
    'Te amo '+emoji_heart+', puedes leerlo hoy, ma??ana o el resto de la vida.'+emoji_calendar,
    'No s?? '+emoji_nose+' hacia d??nde vamos, pero s?? que quiero ir contigo.'+emoji_otro,
    'Pensar en ti '+emoji_pensar+' me hace sonreir.'+emoji_sonreir,
    'Tus ??xitos ser??n mis ??xitos '+emoji_medalla+', tus derrotas ser??n m??as tambi??n.'+emoji_miedo,
    'Y poco a poco te fuiste convirtiendo en la persona que quiero para el resto de mis d??as.'+emoji_beso,
    'Gracias por llenar mi coraz??n '+emoji_heart+' de alegr??a.'+emoji_sonreir,
    'Haces que mi mundo '+emoji_mundo+' est?? lleno de d??as inolvidables.'+emoji_calendar,
    'Eres y  ser??s t??!'+emoji_girl,
    'Amor que rico cumplir un maravilloso mes m??s '+emoji_calendar+' a tu lado '+emoji_cita+'. Gracias por llegar a mi vida, por hacerla cada d??a mejor '+emoji_sonreir+', gracias por apoyarme y escucharme, gracias por ser esa persona que necesito '+emoji_hug+', por estar conmigo siempre. Solo hazme un favor: No te vayas nunca.'+emoji_beso,
    ]


def start(update, context):
    chat = update.message.chat
    for pregunta in PREGUNTAS:
        pregunta['completado'] = False
    global CHAT_ID
    CHAT_ID=update.message.chat
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    button1 = InlineKeyboardButton(text=emojize("1", use_aliases=True), callback_data='pregunta1')
    button2 = InlineKeyboardButton(text=emojize("2", use_aliases=True), callback_data='pregunta2')
    button3 = InlineKeyboardButton(text=emojize("3", use_aliases=True), callback_data='pregunta3')
    button4 = InlineKeyboardButton(text=emojize("4", use_aliases=True), callback_data='pregunta4')
    button5 = InlineKeyboardButton(text=emojize("5", use_aliases=True), callback_data='pregunta5')
    button6 = InlineKeyboardButton(text=emojize("6", use_aliases=True), callback_data='pregunta6')
    button7 = InlineKeyboardButton(text=emojize("7", use_aliases=True), callback_data='pregunta7')
    button8 = InlineKeyboardButton(text=emojize("8", use_aliases=True), callback_data='pregunta8')
    button9 = InlineKeyboardButton(text=emojize("9", use_aliases=True), callback_data='pregunta9')
    button10 = InlineKeyboardButton(text=emojize("10", use_aliases=True), callback_data='pregunta10')
    button11 = InlineKeyboardButton(text=emojize("11", use_aliases=True), callback_data='pregunta11')
    button12 = InlineKeyboardButton(text=emojize("12", use_aliases=True), callback_data='pregunta12')
    button13 = InlineKeyboardButton(text=emojize("13", use_aliases=True), callback_data='pregunta13')
    button14 = InlineKeyboardButton(text=emojize("14", use_aliases=True), callback_data='pregunta14') 
    update.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    update.message.reply_text(FRASES[14])
    update.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random())
    chat.send_sticker(sticker_coronavirus)
    update.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    update.message.reply_text('Selecciona la pregunta que deseas contestar '+emoji_pregunta+', ir??s obteniendo premios '+emoji_regalo+' a medida que avances, hasta lograr el PREMIO FINAL'+emojize(":star-struck:", use_aliases=True), reply_markup=InlineKeyboardMarkup([
        [button1, button2, button3, button4, button5],
        [button6, button7, button8, button9, button10],
        [button11, button12, button13, button14],
    ])
    )
    
def pregunta1(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[0]['pregunta'])
    return PREGUNTA1

def responder1(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[0] or text.lower() == 'todo en uno' or text.lower() == 'todo en 1' or text.lower() == 'todo por uno' or text.lower() == 'todo por 1':
        PREGUNTAS[0]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[0])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_corazon_rojo)
        global button1
        button1 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA1


def pregunta2(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[1]['pregunta'])
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random())
    CHAT_ID.send_sticker(sticker_musica)    
    update.callback_query.message.chat.send_action(action=ChatAction.UPLOAD_AUDIO)
    sleep(random()+2)
    CHAT_ID.send_audio(audio = open('audio.mp3','rb'))
    return PREGUNTA2

def responder2(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[1] or text.lower() == 'estrella':
        PREGUNTAS[1]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[1])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_toruga_corazon)
        global button2
        button2 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA2


def pregunta3(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[2]['pregunta'])
    return PREGUNTA3

def responder3(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[2] or text.lower() == 'cosquilla':
        PREGUNTAS[2]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[2])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_fantasmas_corazon)
        global button3
        button3 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA3


def pregunta4(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[3]['pregunta'])
    return PREGUNTA4

def responder4(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[3]:
        PREGUNTAS[3]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[3])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_vino)
        global button4
        button4 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA4


def pregunta5(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[4]['pregunta'])
    return PREGUNTA5

def responder5(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[4]:
        PREGUNTAS[4]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[4])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_varios_corazones_rosas)
        global button5
        button5 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    
    elif text.lower() == 'mi sol':
        PREGUNTAS[4]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message('Respuesta correcta!!! Peeeero te dije que en una palabra, nos quedaremos s??lo con \'Sol\'. Seguimos')
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[4])
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_varios_corazones_rosas)
        button5 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)            
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END

    elif text.lower() =='amor' or text.lower() == 'mi amor':
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Es verdad que te digo as??, pero hay otra forma que utilizo m??s. Vu??lvelo a intentar\n PISTA: Te digo as?? porque mi mundo gira alrededor de ti, eres mi ...?')
        return PREGUNTA5

    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA5


def pregunta6(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[5]['pregunta'])
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random())
    CHAT_ID.send_sticker(sticker_flores)
    return PREGUNTA6

def responder6(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[5]:
        PREGUNTAS[5]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[5])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_golbo_corazon_rojo)
        global button6
        button6 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA6


def pregunta7(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[6]['pregunta'])
    return PREGUNTA7

def responder7(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[6] or text.lower() == 'studio 55':
        PREGUNTAS[6]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[6])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_fantasmas_girando)
        global button7
        button7 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    
    elif text.lower() == 'estudio' or text.lower() == 'estudio 55':
        PREGUNTAS[6]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message('Respuesta correcta!!! Solo un detalle, el bar llama \'Studio 55\', as?? lo dejaremos. Seguimos')
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[6])
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_fantasmas_girando)
        button7 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA7


def pregunta8(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[7]['pregunta'])
    return PREGUNTA8

def responder8(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[7]:
        PREGUNTAS[7]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[7])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_chocolate)
        global button8
        button8 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END

    elif text.lower() == 'el chocolate':
        PREGUNTAS[7]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message('Respuesta correcta!!! Solo un detalle, nos quedaremos con \'Chocolate\'. Seguimos')
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[7])
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_chocolate)
        button8 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END

    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA8


def pregunta9(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[8]['pregunta'])
    return PREGUNTA9

def responder9(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[8] or text.lower() == 'orgullo y prejuicios':
        PREGUNTAS[8]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[8])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_perro_corazon)
        global button9
        button9 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA9


def pregunta10(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[9]['pregunta'])
    return PREGUNTA10

def responder10(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[9]:
        PREGUNTAS[9]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[9])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_gusano_beso)
        global button10
        button10 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END

    elif text.lower() == 'taca??os':
        PREGUNTAS[9]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text='Un poco feo eso no? Mejor digamos que por \'No pagar\'. Suena mejor, seguimos')
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[9])
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_gusano_beso)
        button10 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END

    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA10


def pregunta11(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[10]['pregunta'])
    return PREGUNTA11

def responder11(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[10] or text.lower() == 'miercoles':
        PREGUNTAS[10]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[10])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_enamorado)
        global button11
        button11 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA11


def pregunta12(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[11]['pregunta'])
    return PREGUNTA12

def responder12(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[11] or text.lower() == 'izquierda':
        PREGUNTAS[11]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[11])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_breakingbad)
        global button12
        button12 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA12

def pregunta13(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[12]['pregunta'])
    return PREGUNTA13

def responder13(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[12]:
        PREGUNTAS[12]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[12])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_globo_flechazo)
        global button13
        button13 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA13


def pregunta14(update, context):
    context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message(text=PREGUNTAS[13]['pregunta'])
    return PREGUNTA14

def responder14(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == RESPUESTAS_CORRECTAS[13]:
        PREGUNTAS[13]['completado'] = True
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        chat.send_message(text=FRASES[13])
        chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        chat.send_sticker(sticker_gato_corazon)
        global button14
        button14 = InlineKeyboardButton(text=emojize(
            ":check_mark_button:", use_aliases=True), callback_data='completado')
        if comprobar_final()==True:
            buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
            chat.send_action(action=ChatAction.TYPING)
            sleep(random())
            CHAT_ID.send_sticker(sticker_regalo_globos)
            return ConversationHandler.END
        else:
            chat.send_action(action=ChatAction.TYPING)
            sleep(random()+2)
            chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
                [button1, button2, button3, button4, button5],
                [button6, button7, button8, button9, button10],
                [button11, button12, button13, button14],
                ])
            )
            return ConversationHandler.END
    else:
        chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)    
        chat.send_message(text=emojize(":red_exclamation_mark:", use_aliases=True)+' Mi sol, fallaste. No pasa nada, vuelve a intentarlo')
        return PREGUNTA14


def final(update, context):
    buttonFinal=InlineKeyboardButton(text='Abrir regalo'+emoji_regalo, callback_data='regalo')
    chat = update.message.chat
    chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    chat.send_message('Mi sol '+emoji_sun+', has completado el juego. Pulsa en el siguiente bot??n para ver tus respuestas, juntas conforman el regalo final'+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True)+emojize(":drum:", use_aliases=True), reply_markup=InlineKeyboardMarkup([[buttonFinal]]))
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random())
    chat.send_sticker(sticker_regalo_globos)

def comprobar_final():
    aux=True
    for pregunta in PREGUNTAS:
        if pregunta['completado'] == False:
            aux= False
            break
    return aux


def list_update(update, context):
    cont=0
    if comprobar_final()==False:
        for pregunta in PREGUNTAS:
            if pregunta['completado'] == True:
                cont+=1
        context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        CHAT_ID.send_message(text='LLevas '+str(cont)+' respondida(s) de 14\n Para continuar escribe: Te amo')
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random())
        CHAT_ID.send_sticker(sticker_mapache_telefono)
        return CONTINUAR
    else:
        text=emojize(":pleading_face:")
        update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random()+2)
        CHAT_ID.send_message('<b>T</b> <del>odo en 1</del>\n<b>E</b> <del>strellas</del>\n\n<b>C</b> <del>osquillas</del>\n<b>A</b> <del>dicto</del>\n<b>S</b> <del>ol</del>\n<b>A</b> <del>mor</del>\n<b>S</b> <del>tudio 55</del>\n\n<b>C</b> <del>hocolate</del>\n<b>O</b> <del>rgullo y prejucio</del>\n<b>N</b> <del>o pagar</del>\n<b>M</b> <del>i??rcoles</del>\n<b> I</b>  <del>zquierdo</del>\n<b>G</b> <del>igante</del>\n<b>O</b> <del>range</del>\n<b>?</b> Di que si '+text, parse_mode=ParseMode.HTML)
        return ConversationHandler.END

def regalo(update, context):
    text=emojize(":pleading_face:")
    update.callback_query.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO)
    sleep(random()+1)
    CHAT_ID.send_photo(open('image.jpg','rb'))
    update.callback_query.message.chat.send_action(action=ChatAction.TYPING)
    sleep(random()+2)
    CHAT_ID.send_message('<b>T</b> <del>odo en 1</del>\n<b>E</b> <del>strellas</del>\n\n<b>C</b> <del>osquillas</del>\n<b>A</b> <del>dicto</del>\n<b>S</b> <del>ol</del>\n<b>A</b> <del>mor</del>\n<b>S</b> <del>tudio 55</del>\n\n<b>C</b> <del>hocolate</del>\n<b>O</b> <del>rgullo y prejucio</del>\n<b>N</b> <del>o pagar</del>\n<b>M</b> <del>i??rcoles</del>\n<b> I</b>  <del>zquierdo</del>\n<b>G</b> <del>igante</del>\n<b>O</b> <del>range</del>\n<b>?</b> Di que si '+text, parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def continuar(update, context):
    text = update.message.text
    chat = update.message.chat
    if text.lower() == 'te amo':
        update.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random()+1)
        chat.send_message('Mi sol '+emoji_sun+', selecciona la pregunta que deseas contestar '+emoji_pregunta+' o presiona sobre una ya respondida '+emojize(":check_mark_button:", use_aliases=True)+' para ver tu estad??stica.', reply_markup=InlineKeyboardMarkup([
            [button1, button2, button3, button4, button5],
            [button6, button7, button8, button9, button10],
            [button11, button12, button13, button14],
        ])
        )
        return ConversationHandler.END
    else:
        update.message.chat.send_action(action=ChatAction.TYPING)
        sleep(random()+1)
        chat.send_message(text='Te dije que escribas *Te amo* '+emojize(":angry_face:", use_aliases=True))
        return CONTINUAR

if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='completado', callback=list_update),
            CallbackQueryHandler(pattern='pregunta10', callback=pregunta10),
            CallbackQueryHandler(pattern='pregunta11', callback=pregunta11),
            CallbackQueryHandler(pattern='pregunta12', callback=pregunta12),
            CallbackQueryHandler(pattern='pregunta13', callback=pregunta13),
            CallbackQueryHandler(pattern='pregunta14', callback=pregunta14),
            CallbackQueryHandler(pattern='pregunta1', callback=pregunta1),
            CallbackQueryHandler(pattern='pregunta2', callback=pregunta2),
            CallbackQueryHandler(pattern='pregunta3', callback=pregunta3),
            CallbackQueryHandler(pattern='pregunta4', callback=pregunta4),
            CallbackQueryHandler(pattern='pregunta5', callback=pregunta5),
            CallbackQueryHandler(pattern='pregunta6', callback=pregunta6),
            CallbackQueryHandler(pattern='pregunta7', callback=pregunta7),
            CallbackQueryHandler(pattern='pregunta8', callback=pregunta8),
            CallbackQueryHandler(pattern='regalo', callback=regalo),
            CallbackQueryHandler(pattern='pregunta9', callback=pregunta9),
        ],
        states={
            CONTINUAR: [MessageHandler(Filters.text, continuar)],
            PREGUNTA1: [MessageHandler(Filters.text, responder1)],
            PREGUNTA2: [MessageHandler(Filters.text, responder2)],
            PREGUNTA3: [MessageHandler(Filters.text, responder3)],
            PREGUNTA4: [MessageHandler(Filters.text, responder4)],
            PREGUNTA5: [MessageHandler(Filters.text, responder5)],
            PREGUNTA6: [MessageHandler(Filters.text, responder6)],
            PREGUNTA7: [MessageHandler(Filters.text, responder7)],
            PREGUNTA8: [MessageHandler(Filters.text, responder8)],
            PREGUNTA9: [MessageHandler(Filters.text, responder9)],
            PREGUNTA10: [MessageHandler(Filters.text, responder10)],
            PREGUNTA11: [MessageHandler(Filters.text, responder11)],
            PREGUNTA12: [MessageHandler(Filters.text, responder12)],
            PREGUNTA13: [MessageHandler(Filters.text, responder13)],
            PREGUNTA14: [MessageHandler(Filters.text, responder14)],
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
