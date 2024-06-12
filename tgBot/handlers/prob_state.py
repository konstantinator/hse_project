from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start_state import router
from bot_graph import BotStates
from keyboards.keyboard_for_leaf_vertex import keyboard_for_leaf_vertex


# Хэндлеры для обработки запросов уверенности
# handlers/lr_prob.py
@router.message(BotStates.lr_prob_state,
                F.text.lower() == "покажи процент уверенности модели")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=user_data['predict_probabilities'],
        reply_markup=keyboard_for_leaf_vertex()
    )


# handlers/rf_prob.py
@router.message(BotStates.rf_prob_state,
                F.text.lower() == "покажи процент уверенности модели")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=user_data['predict_probabilities'],
        reply_markup=keyboard_for_leaf_vertex()
    )
