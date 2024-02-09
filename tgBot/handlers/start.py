from keyboards/keyboard_for_start.py import get_keyBoard_for_start


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