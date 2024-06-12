from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def keyBoard_for_prob() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Покажи процент уверенности модели")
    kb.button(text="Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
