# Хэндлеры для обработки запросов уверенности
# handlers/lr_prob.py
@router.message(BotStates.lr_prob_state,
                F.text.lower() == "покажи процент уверенности модели")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text = user_data['predict_probabilities'],
        reply_markup = keyboard_for_leaf_vertex()
    )

# handlers/rf_prob.py
@router.message(BotStates.rf_prob_state,
                F.text.lower() == "покажи процент уверенности модели")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text = user_data['predict_probabilities'],
        reply_markup = keyboard_for_leaf_vertex()
    )