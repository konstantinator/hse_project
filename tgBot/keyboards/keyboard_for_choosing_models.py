from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def keyboard_for_choosing_models() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Логистическая регрессия")
    kb.button(text="Random Forest в разработке")
    kb.button(text="Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
