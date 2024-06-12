from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start_state import router
from bot_graph import BotStates
from keyboards.keyboard_for_main_menu import keyboard_for_main_menu


@router.message(BotStates.registration_state)
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        text=f"Добро пожаловать, {message.text}!\nВыберите одну из опций",
        reply_markup=keyboard_for_main_menu()
    )
    # Устанавливаем пользователю состояние "Главное меню"
    await state.update_data(user_name=message.text)
    await state.update_data(navigator="Главное меню")
    await state.set_state(BotStates.main_menu_state)
