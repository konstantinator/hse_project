@router.message(F.text.lower() == "назад")
async def back_to_menue(message: Message, state: FSMContext):
    user_data = await state.get_data()
    current_state_name = user_data['navigator']
    graph_navigator = GraphNavigator(G, current_state_name)
    parent_state_name = graph_navigator.get_parent()
    parent_state = node_to_state[parent_state_name]
    if parent_state_name == "Регистрация":
        await message.answer(text="Введите свое имя",
                             reply_markup=ReplyKeyboardRemove())
    if parent_state_name == "Главное меню":
        await message.answer(text="Главное меню",
                             reply_markup = keyboard_for_main_menu())
    if parent_state_name == "Подбери заголовок":
        await message.answer(text="Попробуйте выбрать другую модель",
                             reply_markup = keyboard_for_choosing_models())
    if parent_state_name == "LogReg":
        await message.answer(text="Введите другую новость.\nВыбранная модель: LogReg",
                             reply_markup=keyboard_for_leaf_vertex())
    if parent_state_name == "RandomForest":
        await message.answer(text="Введите другую новость.\nВыбранная модель: LogReg (randomForest в разработке)",
                             reply_markup=keyboard_for_leaf_vertex())
    await state.update_data(navigator = parent_state_name)
    await state.set_state(state = parent_state)