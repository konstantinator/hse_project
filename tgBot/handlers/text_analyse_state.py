from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start_state import router
from bot_graph import BotStates
from keyboards.keyBoard_for_prob import keyBoard_for_prob
from keyboards.keyboard_for_leaf_vertex import keyboard_for_leaf_vertex
from text_preprocessing import get_sim_text
from models_functions import predict_lr, predict_proba, format_predictions


# Хэндлеры для обработки текстов новостей
# Вывод результата Лог рег
@router.message(BotStates.logreg_state)
async def log_reg_answer(message: Message, state: FSMContext):
    await state.update_data(predict_probabilities=format_predictions(
        predict_proba(message.text.lower())))  # запоминаем вероятности для следующего шага
    await message.answer(
        text=predict_lr(message.text.lower()),
        reply_markup=keyBoard_for_prob()
    )
    await state.update_data(navigator="Уверенность logReg")
    await state.set_state(BotStates.lr_prob_state)


# Вывод результата Random Forest
@router.message(BotStates.randomforest_state)
async def log_reg_answer(message: Message, state: FSMContext):
    await state.update_data(predict_probabilities=format_predictions(
        predict_proba(message.text.lower())))  # запоминаем вероятности для следующего шага
    await message.answer(
        text=predict_lr(message.text.lower()),
        reply_markup=keyBoard_for_prob()
    )
    await state.update_data(navigator="Уверенность randomForest")
    await state.set_state(BotStates.lr_prob_state)


# Вывод результата Similar_text
@router.message(BotStates.sim_state)
async def raandom_forest_answer(message: Message):
    await message.answer(
        text=get_sim_text(message.text.lower()),
        reply_markup=keyboard_for_leaf_vertex()
    )
