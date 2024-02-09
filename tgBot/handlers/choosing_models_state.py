from keyboards/keyboard_for_choosing_models.py import keyboard_for_choosing_models

# Роутер для обработка запроса "LogReg"
# handlers/logreg.py
@router.message(BotStates.choosing_model_state,
                F.text.lower() == "логистическая регрессия")
async def log_reg_chosen(message: Message, state: FSMContext):
    await message.answer(
        text = "Поздравляю, вы выбрали логистическую регрессию! Теперь отправте боту Вашу новость",
        reply_markup = keyboard_for_leaf_vertex()
    )
    await state.update_data(navigator = "LogReg")
    await state.set_state(BotStates.logreg_state)

# Роутер для обработка запроса "RandomForest"
# handlers/random_forest.py
@router.message(BotStates.choosing_model_state,
                F.text.lower() == "random forest")
async def random_forest_chosen(message: Message, state: FSMContext):
    await message.answer(
        text = "К сожалению random forest еще в разработке, поэтому используемая модель логистическая регрессия. Теперь отправте боту Вашу новость",
        reply_markup = keyboard_for_leaf_vertex()
    )
    await state.update_data(navigator = "RandomForest")
    await state.set_state(BotStates.randomforest_state)

# Роутер для обработки некорректных вводов
# handlers/incorrect model.py
@router.message(BotStates.choosing_model_state,
                F.text.lower() != "назад")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer(
        text = "Некорректный ввод.\n\n"
             "Пожалуйста, выберите модель из списка ниже:",
        reply_markup = keyboard_for_choosing_models()
    )