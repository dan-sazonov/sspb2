from dispatcher import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from messages import Messages
from db import Santa, Main


def init():
    # костыль, чтобы импорт в handlers.py не был пустым
    pass


messages = Messages()
mes_santa = Messages.Santa()
db = Santa()
db_main = Main()


class Poll(StatesGroup):
    Wishes = State()
    OnMeeting = State()
    Address = State()
    Name = State()


@dp.message_handler(commands=['santa'], state=None)
async def start_polling(message: types.Message):
    await message.answer(mes_santa.on_start, disable_web_page_preview=True)
    await message.answer(mes_santa.ask_wishes)
    db_main.update_counter(message.from_user.id, 'santa')

    await Poll.Wishes.set()


@dp.message_handler(state=Poll.Wishes)
async def answer_q1(message: types.Message, state: FSMContext):
    mes_kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_1 = types.KeyboardButton('Да!')
    btn_2 = types.KeyboardButton('Нет')
    mes_kb.row(btn_1, btn_2)

    answer = message.text
    await state.update_data(wishes=answer)

    await message.answer(mes_santa.ask_meeting, reply_markup=mes_kb)
    await Poll.OnMeeting.set()


@dp.message_handler(state=Poll.OnMeeting)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    if answer not in ['Да!', 'Нет']:
        await message.reply('Я тебя не понял. Пожалуйста, используй кнопки для ответа')
        return
    answer = {'Да!': True, 'Нет': False}[answer]
    await state.update_data(on_meeting=answer)

    await message.answer(mes_santa.ask_address, reply_markup=types.ReplyKeyboardRemove())
    await Poll.Address.set()


@dp.message_handler(state=Poll.Address)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(address=answer)

    await message.answer(mes_santa.ask_name)
    await Poll.Name.set()


@dp.message_handler(state=Poll.Name)
async def answer_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    form = {'wishes': data.get("wishes"), 'on_meeting': data.get("on_meeting"), 'address': data.get("address"),
            'name': message.text}

    db.add_user(int(message.from_user.id), form)

    await message.answer(mes_santa.on_end)
    await state.finish()


@dp.message_handler(commands=['end'])
async def team_mes(message: types.Message):
    db.del_user(int(message.from_user.id))
    db_main.update_counter(message.from_user.id, 'end')
    await message.answer(mes_santa.end)
