from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def keyboard_for_leaf_vertex() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = "Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
