from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def generate_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    button = [KeyboardButton(text='Цель бота')]
    markup.add(*button)

    return markup
