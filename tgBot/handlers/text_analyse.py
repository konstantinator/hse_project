# Хэндлеры для обработки текстов новостей

# Вывод результата Лог рег
@router.message(BotStates.logreg_state)
async def log_reg_answer(message: Message, state: FSMContext):
    await state.update_data(predict_probabilities = format_predictions(predict_proba(message.text.lower()))) # запоминаем вероятности для следующего шага
    await message.answer(
        text = predict_lr(message.text.lower()),
        reply_markup = keyBoard_for_prob()
    )
    await state.update_data(navigator = "Уверенность logReg")
    await state.set_state(BotStates.lr_prob_state)

# Вывод результата Random Forest
# handlers/text_analysis_by_randomForesr.py
@router.message(BotStates.randomforest_state)
async def log_reg_answer(message: Message, state: FSMContext):
    await state.update_data(predict_probabilities = format_predictions(predict_proba(message.text.lower()))) # запоминаем вероятности для следующего шага
    await message.answer(
        text = predict_lr(message.text.lower()),
        reply_markup = keyBoard_for_prob()
    )
    await state.update_data(navigator = "Уверенность randomForest")
    await state.set_state(BotStates.lr_prob_state)

# Вывод результата Similar_text
# handlers/similar_search.py
@router.message(BotStates.sim_state)
async def raandom_forest_answer(message: Message, state: FSMContext):
    await message.answer(
        text = get_sim_text(message.text.lower()),
        reply_markup = keyboard_for_leaf_vertex()
    )