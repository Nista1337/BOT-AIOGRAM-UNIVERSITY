from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_menu():
    kb = [
        [KeyboardButton(text='Процесс поступления'), KeyboardButton(text="Направления подготовки")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard




def choice_naprav():
    kb = [
        [
            KeyboardButton(text="Радиоэлектронные системы и комплексы"),
            KeyboardButton(text="Информационные системы организаций и предприятий"),
            KeyboardButton(text="Учитель физики и математики"),
        ],
        [
            KeyboardButton(text="Учитель математики и информатики"),
            KeyboardButton(text="Математическое и информационное моделирование"),
        ],
        [KeyboardButton(text="Отмена")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def progress_post():
    kb = [
        [KeyboardButton(text='Вступительные экзамены'), KeyboardButton(text="Перечень документов для поступления")],
        [KeyboardButton(text="В каком формате нужно предоставить в приемную комиссию")],
        [KeyboardButton(text="Отмена")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard





def programma_keyboard():
    kb = [
        [KeyboardButton(text="Минимальный балл для поступления на бюджет 2023")],
        [KeyboardButton(text="Описание направления"), KeyboardButton(text="Программа подготовки"), KeyboardButton(text="Количество бюджетных мест")],
        [KeyboardButton(text="Назад")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

