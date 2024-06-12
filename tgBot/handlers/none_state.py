from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from handlers.start_state import router


# Роутер для помощи со стартом
@router.message(StateFilter(None))
async def help_with_start(message: Message):
    await message.answer(
        text="Этот бот помогает обрабатывать новости, для начала работы пропишите /start",
        reply_markup=ReplyKeyboardRemove()
    )


# Роутер для обработки некорректных вводов
@router.message()
async def incorrect_imput(message: Message):
    await message.answer(
        text="Некорректный ввод.\n"
             "Пожалуйста, выберите одно из списка ниже:"
    )
