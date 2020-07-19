import config
import telebot
import types
import links, vili

#from contact import User

token = config.TOKEN

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def an_msg(message):
    #user_id = message.from_user.id
    bot.send_message(message.chat.id, '**Здравствуйте, я помошник Визового центра "Либерти"\n'
                                      'Я всегда помогу вам:\n'
                                      '1. Узнать актуальный список документов для оформления визы\n'
                                      '2. Узнать срок оформления и стоимость\n'
                                      '3. Скачать опросник, чтобы уже сегодня начать оформление визы\n'
                                      '4. Если у вас будут вопросы, соединю вас с нашимими специалистами\n'
                                      'и многое другое\n'
                                      'Давайте уже начнем, просто нажмите на /menu\n'                                   
                                      'и вам откроются главные фунции!')


@bot.message_handler(commands=["menu"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    callback_button_1 = types.InlineKeyboardButton(text="Список документов", callback_data="doki")
    callback_button_2 = types.InlineKeyboardButton(text="Стоимость визы", callback_data="cena")
    callback_button_3 = types.InlineKeyboardButton(text="Оформить онлайн визу", callback_data="online")
    callback_button_4 = types.InlineKeyboardButton(text="Наш инстаграм", callback_data="insta",
                                                   url=links.url_ins_che)
    callback_button_5 = types.InlineKeyboardButton(text="Мы ВКонтакте", callback_data="vk",
                                                   url=links.url_vk_che)
    callback_button_6 = types.InlineKeyboardButton(text="Связаться  с нами", callback_data="contact")
    keyboard.add(callback_button_1, callback_button_2, callback_button_3, callback_button_4, callback_button_5,
                 callback_button_6)
    bot.send_message(message.chat.id, "Выберите что вы хотели бы узнать?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "doki":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_evropa = types.InlineKeyboardButton(text="Европа", callback_data="evropa")
        call_button_usa = types.InlineKeyboardButton(text="США.Канада", callback_data="usa")
        call_button_azia = types.InlineKeyboardButton(text="Азия", callback_data="azia")
        call_button_other = types.InlineKeyboardButton(text="Другие страны", callback_data="other")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_evropa, call_button_azia, call_button_usa, call_button_other)
        comproxy_keyboard.add(call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите континент:",
                              reply_markup=comproxy_keyboard)

    elif call.data == "cena":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_evropa = types.InlineKeyboardButton(text="Европа", callback_data="evropa")
        call_button_usa = types.InlineKeyboardButton(text="США.Канада", callback_data="usa")
        call_button_britania = types.InlineKeyboardButton(text="Великобритания", callback_data="britania")
        call_button_azia = types.InlineKeyboardButton(text="Азия", callback_data="azia")
        call_button_other = types.InlineKeyboardButton(text="Другие страны", callback_data="other")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_evropa, call_button_usa, call_button_britania,
                              call_button_azia, call_button_other)
        comproxy_keyboard.add(call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите континент:",
                              reply_markup=comproxy_keyboard)

    if call.data == "online":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_oprosnik = types.InlineKeyboardButton(text="Скачать опросник", callback_data="dowopr")
        call_button_send = types.InlineKeyboardButton(text="Отправить документы", callback_data="sendopr")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_oprosnik, call_button_send)
        comproxy_keyboard.add(call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Если вы не заполняли опросник, выберите 'Скачать опросник'\n"
                                   "Если вы уже заполнили опросник и подготовили документы\n"
                                   "нажмите на 'Отправить документв'",
                              reply_markup=comproxy_keyboard)

    elif call.data == "dowopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_evopr = types.InlineKeyboardButton(text="Опросник для визы в Европу", callback_data="evoopr")
        call_button_usaopr = types.InlineKeyboardButton(text="Опросник для визы в США", callback_data="usaopr")
        call_button_britanopr = types.InlineKeyboardButton(text="Опросник для визы в Англию", callback_data="bropr")
        call_button_chinaopr = types.InlineKeyboardButton(text="Опросник для визы в Китай", callback_data="chinaopr")
        call_button_austopr = types.InlineKeyboardButton(text="Опросник для визы в Австралию", callback_data="austopr")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_evopr, call_button_usaopr, call_button_britanopr, call_button_chinaopr,
                              call_button_austopr,call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Что то написать ",
                              reply_markup=comproxy_keyboard)

    elif call.data == "evoopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Можете сразу узнать список документов\n "
                                   "или вернуться назад",
                              reply_markup=comproxy_keyboard)
        bot.send_document(chat_id=call.message.chat.id, data = open("/home/archi/vc/oprosniki/Опросник Шенген.pdf", "rb"))

    elif call.data == "usaopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Можете сразу узнать список документов\n "
                                   "или вернуться назад",
                              reply_markup=comproxy_keyboard)
        bot.send_document(chat_id=call.message.chat.id, data = open("/home/archi/vc/oprosniki/США Опросник-Word.docx", "rb"))

    elif call.data == "bropr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Можете сразу узнать список документов\n "
                                   "или вернуться назад",
                              reply_markup=comproxy_keyboard)
        bot.send_document(chat_id=call.message.chat.id, data = open("/home/archi/vc/oprosniki/Опросник Англия.pdf", "rb"))

    elif call.data == "chinaopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Можете сразу узнать список документов\n "
                                   "или вернуться назад",
                              reply_markup=comproxy_keyboard)
        bot.send_document(chat_id=call.message.chat.id, data = open("/home/archi/vc/oprosniki/Опросник Китай.docx", "rb"))

    elif call.data == "austopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Можете сразу узнать список документов\n "
                                   "или вернуться назад",
                              reply_markup=comproxy_keyboard)
        bot.send_document(chat_id=call.message.chat.id, data = open("/home/archi/vc/oprosniki/Опросник Австралия.doc", "rb"))

    if call.data == "sendopr":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Узнать список документов", callback_data="doki")
        callback_button_4 = types.InlineKeyboardButton(text="Наш инстаграм", callback_data="insta",
                                                       url=links.url_ins_che)
        callback_button_5 = types.InlineKeyboardButton(text="Мы ВКонтакте", callback_data="vk",
                                                       url=links.url_vk_che)
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(callback_button_1, callback_button_4, callback_button_5, call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Sooryy! Уже совсем скоро мы запустим этот раздел",
                              reply_markup=comproxy_keyboard)



    if call.data == "evropa":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=2)
        call_button_austria = types.InlineKeyboardButton(text="Австрия", callback_data="austria",
                                                         url=vili.austria)
        call_button_belgium = types.InlineKeyboardButton(text="Бельгия", callback_data="belgiun",
                                                         url=vili.belgiun)
        call_button_bulgary = types.InlineKeyboardButton(text="Болгария", callback_data="bulgary",
                                                         url=vili.bulgary)
        call_button_hungary = types.InlineKeyboardButton(text="Венгрия", callback_data="hungary",
                                                         url=vili.hungary)
        call_button_greece = types.InlineKeyboardButton(text="Греция", callback_data="greece",
                                                        url=vili.greece)
        call_button_germany = types.InlineKeyboardButton(text="Германия", callback_data="germany",
                                                         url=vili.germany)
        call_button_denmark = types.InlineKeyboardButton(text="Дания", callback_data="denmark",
                                                         url=vili.denmark)
        call_button_spain = types.InlineKeyboardButton(text="Испания", callback_data="spain",
                                                       url=vili.spain)
        call_button_italy = types.InlineKeyboardButton(text="Италия", callback_data="italy",
                                                       url=vili.italy)
        call_button_cyprus = types.InlineKeyboardButton(text="Кипр", callback_data="cyprus",
                                                        url=vili.cyprus)
        call_button_litva = types.InlineKeyboardButton(text="Литва", callback_data="litva",
                                                       url=vili.litva)
        call_button_lithua = types.InlineKeyboardButton(text="Латвия", callback_data="lithua",
                                                        url=vili.lithua)
        call_button_malta = types.InlineKeyboardButton(text="Мальта", callback_data="malta",
                                                       url=vili.malta)
        call_button_niderland = types.InlineKeyboardButton(text="Нидерланды", callback_data="niderland",
                                                           url=vili.niderland)
        call_button_poland = types.InlineKeyboardButton(text="Польша", callback_data="poland",
                                                        url=vili.poland)
        call_button_portugal = types.InlineKeyboardButton(text="Португалия", callback_data="portugal",
                                                          url=vili.portugal)
        call_button_romania = types.InlineKeyboardButton(text="Румыния", callback_data="romania",
                                                         url=vili.romania)
        call_button_finland = types.InlineKeyboardButton(text="Финляндия", callback_data="finland",
                                                         url=vili.finland)
        call_button_france = types.InlineKeyboardButton(text="Франция", callback_data="france",
                                                        url=vili.france)
        call_button_slovakia = types.InlineKeyboardButton(text="Словакия", callback_data="slovakia",
                                                          url=vili.slovakia)
        call_button_slovenia = types.InlineKeyboardButton(text="Словения", callback_data="slovenia",
                                                          url=vili.slovenia)
        call_button_croatia = types.InlineKeyboardButton(text="Хорватия", callback_data="croatia",
                                                         url=vili.croatia)
        call_button_czech = types.InlineKeyboardButton(text="Чехия", callback_data="czech",
                                                       url=vili.czech)
        call_button_switzerland = types.InlineKeyboardButton(text="Швейцария", callback_data="switzerland",
                                                             url=vili.switzerland)
        call_button_sweden = types.InlineKeyboardButton(text="Швеция", callback_data="sweden",
                                                        url=vili.sweden)
        call_button_estonia = types.InlineKeyboardButton(text="Эстония", callback_data="estonia",
                                                         url=vili.estonia)
        call_button_comeback = types.InlineKeyboardButton(text="Вернуться назад", callback_data="comeback")
        comproxy_keyboard.add(call_button_austria, call_button_belgium, call_button_bulgary, call_button_hungary, call_button_greece,\
                              call_button_germany, call_button_denmark, call_button_spain, call_button_italy,\
                              call_button_cyprus, call_button_litva, call_button_lithua, call_button_malta,\
                              call_button_niderland, call_button_poland, call_button_portugal, call_button_romania,\
                              call_button_finland, call_button_france, call_button_slovakia, call_button_slovenia,\
                              call_button_croatia, call_button_czech, call_button_switzerland, call_button_sweden,\
                              call_button_estonia,call_button_comeback)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите страну и вы получите список документов?:",
                              reply_markup=comproxy_keyboard)

    elif call.data == "usa":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_usa = types.InlineKeyboardButton(text="США", callback_data="usa1",
                                                     url=vili.usa1)
        call_button_canada = types.InlineKeyboardButton(text="Канада", callback_data="canada",
                                                        url=vili.canada)
        call_button_comeback = types.InlineKeyboardButton(text="Вернуться назад", callback_data="comeback")
        comproxy_keyboard.add(call_button_usa, call_button_canada, call_button_comeback)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите страну и вы узнаете список документов",
                              reply_markup=comproxy_keyboard)

    elif call.data == "azia":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_vietnam = types.InlineKeyboardButton(text="Вьетнам", callback_data="vietnam",
                                                         url=vili.vietnam)
        call_button_indiya = types.InlineKeyboardButton(text="Индия", callback_data="indiya",
                                                        url=vili.indiya)
        call_button_china = types.InlineKeyboardButton(text="Китай", callback_data="china",
                                                       url=vili.china)
        call_button_thailand = types.InlineKeyboardButton(text="Таиланд", callback_data="thailand",
                                                          url=vili.thailand)
        call_button_singapore = types.InlineKeyboardButton(text="Сингапур", callback_data="singapore",
                                                           url=vili.singapore)
        call_button_japan = types.InlineKeyboardButton(text="Япония", callback_data="japan",
                                                       url=vili.japan)
        call_button_korea = types.InlineKeyboardButton(text="Южная Корея", callback_data="korea",
                                                       url=vili.korea)
        call_button_comeback = types.InlineKeyboardButton(text="Вернуться назад", callback_data="comeback")
        comproxy_keyboard.add(call_button_vietnam, call_button_indiya, call_button_china, call_button_thailand, call_button_singapore,\
                              call_button_japan, call_button_korea, call_button_comeback)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите страну и вы узнате список документов",
                              reply_markup=comproxy_keyboard)

    elif call.data =="britania":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_britan = types.InlineKeyboardButton(text="Англия", callback_data="britan",
                                                        url=vili.britan)
        call_button_ireland = types.InlineKeyboardButton(text="Ирландия", callback_data="ireland",
                                                         url=vili.ireland)
        call_button_comeback = types.InlineKeyboardButton(text="Вернуться назад", callback_data="comeback")
        comproxy_keyboard.add(call_button_britan, call_button_ireland, call_button_comeback)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите страну и вы узнате список документов",
                              reply_markup=comproxy_keyboard)

    elif call.data == "other":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_australia = types.InlineKeyboardButton(text="Австралия", callback_data="australia",
                                                           url=vili.australia)
        call_button_mexico = types.InlineKeyboardButton(text="Мексика", callback_data="mexico",
                                                        url=vili.mexico)
        call_button_comeback = types.InlineKeyboardButton(text="Вернуться назад", callback_data="comeback")
        comproxy_keyboard.add(call_button_australia, call_button_mexico, call_button_comeback)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите страну и вы узнате список документов",
                              reply_markup=comproxy_keyboard)

    elif call.data == "back":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button_1 = types.InlineKeyboardButton(text="Список документов", callback_data="doki")
        callback_button_2 = types.InlineKeyboardButton(text="Стоимость визы", callback_data="cena")
        callback_button_3 = types.InlineKeyboardButton(text="Оформить онлайн визу", callback_data="online")
        callback_button_4 = types.InlineKeyboardButton(text="Наш инстаграм", callback_data="insta", url="https://www.instagram.com/liberty_visa/?hl=ru")
        callback_button_5 = types.InlineKeyboardButton(text="Мы ВКонтакте", callback_data="vk", url="https://vk.com/libertyviza")
        callback_button_6 = types.InlineKeyboardButton(text="Связаться  с нами", callback_data="contact")
        comproxy_keyboard.add(callback_button_1, callback_button_2, callback_button_3, callback_button_4,
                              callback_button_5, callback_button_6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите что вы хотели бы узнать?",
                              reply_markup=comproxy_keyboard)

    elif call.data == "comeback":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_evropa = types.InlineKeyboardButton(text="Европа", callback_data="evropa")
        call_button_usa = types.InlineKeyboardButton(text="США.Канада", callback_data="usa")
        call_button_britania = types.InlineKeyboardButton(text="Великобритания", callback_data="britania")
        call_button_azia = types.InlineKeyboardButton(text="Азия", callback_data="azia")
        call_button_other = types.InlineKeyboardButton(text="Другие страны", callback_data="other")
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_evropa, call_button_usa, call_button_britania,
                              call_button_azia, call_button_other)
        comproxy_keyboard.add(call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите континент:",
                              reply_markup=comproxy_keyboard)

    if call.data == "contact":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_telefon = types.InlineKeyboardButton(text="По номеру телефона", callback_data="telefon_number")
        #call_button_email = types.InlineKeyboardButton(text="Написать email", callback_data="email")
        #call_button_adress = types.InlineKeyboardButton(text="Узнать адрес", callback_data="adress")
        callback_button_4 = types.InlineKeyboardButton(text="Написать в Instagram", callback_data="insta",
                                                       url=links.url_ins_che)
        callback_button_5 = types.InlineKeyboardButton(text="Написать в VK ", callback_data="vk",
                                                       url=links.url_vk_che)
        call_button_back = types.InlineKeyboardButton(text="Назад", callback_data="back")
        comproxy_keyboard.add(call_button_telefon,callback_button_4,
                              callback_button_5)
        comproxy_keyboard.add(call_button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите, способ связи с нами:",
                              reply_markup=comproxy_keyboard)

    elif call.data == "telefon_number":
        comproxy_keyboard = types.InlineKeyboardMarkup(row_width=1)
        call_button_chelyabinsk = types.InlineKeyboardButton(text='Челябинск', callback_data="chelyabinsk")
        call_button_krasnoyarsk = types.InlineKeyboardButton(text='Красноярск', callback_data="krasnoyarsk")
        call_button_surgut= types.InlineKeyboardButton(text='Сургут', callback_data="surgut")
        comproxy_keyboard.add(call_button_chelyabinsk, call_button_krasnoyarsk, call_button_surgut)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите город нашего офиса",
                              reply_markup=comproxy_keyboard)

    elif call.data == "chelyabinsk":
        bot.send_contact(chat_id=call.message.chat.id, first_name=links.name_che, last_name='Челябинск',
                         phone_number=links.telefon_che)
        bot.send_message(chat_id=call.message.chat.id, text=links.adres_che)
    elif call.data =="krasnoyarsk":
        bot.send_contact(chat_id=call.message.chat.id, first_name='Визовый центр "Либерти"',last_name='Челябинск',
                        phone_number="+73912630345")
        bot.send_message(chat_id=call.message.chat.id, text="Адрес ВЦ 'Либерти' Красноярск:\n"
                                                            "улица Маерчака 18, офис 409, Красноярск")





#if __name__ == '__main__':
bot.polling(none_stop=True)