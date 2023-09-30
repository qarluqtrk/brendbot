from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def phone_num():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Telefon raqamni ulashish', request_contact=True)
    button0 = KeyboardButton(text='bekor qilish')
    rkm.add(button, button0)
    return rkm


def cancel_key():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='bekor qilish')
    rkm.add(button)
    return rkm


def loc():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Manzilimni ulashish', request_location=True)
    button0 = KeyboardButton(text='bekor qilish')
    rkm.add(button, button0)
    return rkm


def back_to_main():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='Asosiy Menyu'))
