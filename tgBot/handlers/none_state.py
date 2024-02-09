# Роутер для помощи со стартом
@router.message(StateFilter(None))
async def help_with_start(message: Message, state: FSMContext):
    await message.answer(
        text = "Этот бот помогает обрабатывать новости, для начала работы пропишите /start",
        reply_markup = ReplyKeyboardRemove()
    )

# Роутер для обработки некорректных вводов
@router.message()
async def incorrect_imput(message: Message, state: FSMContext):
    await message.answer(
        text = "Некорректный ввод.\n"
             "Пожалуйста, выберите одно из списка ниже:"
    )