from datebase import get_token, db_history_write, db_history_read
from keyboards import generate_button
from parser import parser

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

TOKEN = get_token()
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Questions(StatesGroup):
    button = State()
    metcast = State()


@dp.message_handler(commands=['start', 'history'])
async def command_start(message: Message):
    if message.text == '/start':
        await message.answer('Здравствуйте!')
        await start_questions(message)
    elif message.text == '/history':
        await get_history(message)


async def get_history(message: Message):
    chat_id = message.chat.id
    stories = db_history_read(chat_id)
    for city_name, metcast_text in stories[:5]:
        await message.answer(f'''
Вы запрашивали погоду города: {city_name}
Бот ответил: {metcast_text}''')


async def start_questions(message: Message):
    await Questions.button.set()
    await message.answer('Нажмите кнопку', reply_markup=generate_button())


@dp.message_handler(content_types=['text'], state=Questions.button)
async def confirm_button(message: Message, state: FSMContext):
    if message.text in ['/start', '/history']:
        await state.finish()
        await command_start(message)
    else:
        async with state.proxy() as data:
            data['button'] = message.text

        await Questions.next()
        await message.answer(
            'Данный бот создан, чтобы узнать погоду в любом городе.'
            '\nВведите город', reply_markup=ReplyKeyboardRemove()
        )


@dp.message_handler(content_types=['text'], state=Questions.metcast)
async def confirm_city_name_metcast(massage: Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = massage.text

    city_name = data['text']
    metcast_text = parser(city_name)
    chat_id = massage.chat.id
    db_history_write(chat_id, city_name, metcast_text)
    await massage.answer(metcast_text)
    await state.finish()
    await start_questions(massage)


executor.start_polling(dp)
