"""
Тексты всех сообщений
Файл могут редактировать неайтишники, все должно быть антивандально. Все функции по обработке пихаем в `handlers.py`
"""
import config


class Messages:
    """
    Тексты сообщений, отправляемые ботом
    """

    def __init__(self):
        # не лезь, оно сожрет тебя
        self.foo = 'bar'
        self.admin_id = config.ADMIN_CHAT
        self.start_polling = '🔔 Бот запущен'
        self.stop_polling = '🔔 Бот остановлен'

        self.not_command = '''Я ничего не понял. Чтобы посмотреть список команд бота, введи /help'''
        self.help = '''<b>Что тебя интересует?</b>
    /stop - остановить бота и удалить данные о себе

🎅 <b>Тайный санта</b>
    /santa - начать участие
    /end - удалить заявку

<i>Бот-помощник актива ПБ2 работает на открытом исходном коде, который размещён на портале "Github". За подробностями отправляйся по <a href="https://github.com/dan-sazonov/sspb2">ссылке</a>.</i>

По всем вопросам - @dan_sazonov'''

        self.subscribe = '''<b>Привет, дорогой друг!</b> Это телеграм-бот актива ПБ2.

Чтобы начать играть в Тайного Санту, отправь боту команду /santa

<i>Если возникнут какие-то вопросы, ты всегда можешь написать @dan_sazonov</i>'''
        self.do_unsubscribe = '''Чтобы отписаться, напишите в этот чат «/stop» или «/unsubscribe»'''

        self.unsubscribe = '''Очень жаль, что ты нас покидаешь! Возвращайся скорее!'''
        self.do_subscribe = '''Для повторной подписки введите «/start» или «/subscribe»'''

    class Santa:
        def __init__(self):
            self.on_start = '''<b>Привет и добро пожаловать в меню "Тайного Санты"!</b>
Это анонимная игра, в которой каждый может стать Сантой (или, если хотите, Дедом Морозом) для случайного человека. Конечно же, он будет из актива ПБ2!

<b>План такой:</b>
1️⃣. напиши, что ты хочешь получить в подарок;
2️⃣. напиши, что ты точно НЕ хочешь получить в подарок (например, если на что-нибудь у тебя аллергия);
3️⃣. реши, сможешь ли ты приехать на встречу актива 18 декабря;
4️⃣. укажи, как тебя зовут и в каком из офисов тебе будет удобно забрать подарок;
5️⃣. затем через несколько дней наша система подберёт для тебя человека, которому ты сделаешь подарок!


P. S. Продолжая диалог с ботом, ты соглашаешься с нашей <a href="https://github.com/dan-sazonov/sspb2/blob/main/legal_info/PRIVACY.md">Политикой конфиденциальности.</a>
'''
            self.ask_wishes = '''<b>Шаг 1.</b> Напиши в ответ на это сообщение свои пожелания по подарку. Что ты хочешь получить от своего Санты? А что точно не хочешь?'''
            self.ask_meeting = '''<b>Шаг 2.</b> Приедешь ли ты на встречу актива 18 декабря? Нажми кнопку, которая соответствует твоему решению.

(За более подробной информацией обратись к @dan_sazonov)'''
            self.ask_address = '''<b>Шаг 3.</b> Если у тебя не получится прийти на встречу, в каком из офисов профкома тебе было бы удобно забрать подарок и оставить свой? Нажми кнопку, которая соответствует твоему решению.'''
            self.ask_name = '''<b>Шаг 4.</b> Укажи в ответном сообщении свои фамилию, имя и отчество в именительном падеже.

Это не будет знать никто, кроме твоего Тайного Санты. Ему это понадобится, для того чтобы знать, кому отправить подарок.'''
            self.on_end = '''<b>Шаг 5.</b> Отлично! Наша система зарегистрировала тебя для участия в "Тайном Санте".
Если ты захочешь отказаться от участия, отправь команду /end.

Мы напишем, кому ты будешь делать подарок, позже. Следи за сообщениями бота!'''
            self.end = '''Очень жаль, что ты покидаешь игру! Для повторного участия отправь команду /santa'''
