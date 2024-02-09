def keyboard_for_rating() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Плохо " + emoji.emojize(":face_with_symbols_on_mouth:"))
    kb.button(text="Хорошо 🙂")
    kb.button(text="Отлично 😀")
    kb.button(text="Назад")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)