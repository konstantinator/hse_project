from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import aiofiles
from handlers.start_state import router
from bot_graph import BotStates
from keyboards.keyboard_for_main_menu import keyboard_for_main_menu


# Хэндлеры для оценки работы бота
@router.message(BotStates.rate_state,
                F.text.lower() == "плохо 🤬")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Жаль, что Вам не понравилось, {user_data['user_name']}"
             f"( Мы постараемся доработать бота",
        reply_markup=keyboard_for_main_menu()
    )
    async with aiofiles.open("rating", mode='a') as file:
        await file.write(f"{user_data['user_name']}: плохо\n")
    await state.update_data(navigator="Главное меню")
    await state.set_state(BotStates.main_menu_state)


# Хэндлеры для оценки работы бота
@router.message(BotStates.rate_state,
                F.text.lower() == "хорошо 🙂")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Спасибо за оценку, {user_data['user_name']}!"
             f" Скоро выйдет обновление и бот станет еще лучше!",
        reply_markup=keyboard_for_main_menu()
    )
    async with aiofiles.open("rating", mode='a') as file:
        await file.write(f"{user_data['user_name']}: хорошо\n")
    await state.update_data(navigator="Главное меню")
    await state.set_state(BotStates.main_menu_state)


# Хэндлеры для оценки работы бота
@router.message(BotStates.rate_state,
                F.text.lower() == "отлично 😀")
async def task_chosen_incorrectly(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(text="🎉")
    await message.answer(
        text=f"Мы рады, что Вам понравилось, {user_data['user_name']}!",
        reply_markup=keyboard_for_main_menu()
    )
    async with aiofiles.open("rating", mode='a') as file:
        await file.write(f"{user_data['user_name']}: отлично\n")
    await state.update_data(navigator="Главное меню")
    await state.set_state(BotStates.main_menu_state)
