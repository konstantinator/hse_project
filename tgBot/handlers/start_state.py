from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardRemove
from bot_graph import BotStates
from aiogram.fsm.context import FSMContext


router = Router()

# @router.message(StateFilter(None), Command("start"))
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    # Очищаем сохраненные данные
    await state.clear()
    await state.update_data(navigator = "Регистрация")
    await message.answer(text="Для продолжения введите свое имя",
                         reply_markup = ReplyKeyboardRemove())
    # Устанавливаем пользователю состояние "Регистрация"
    await state.set_state(BotStates.registration_state)