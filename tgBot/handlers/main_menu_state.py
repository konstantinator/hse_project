from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from handlers.start_state import router
from aiogram import F
from bot_graph import BotStates
from keyboards.keyboard_for_choosing_models import keyboard_for_choosing_models
from keyboards.keyboard_for_leaf_vertex import keyboard_for_leaf_vertex
from keyboards.keyboard_for_rating import keyboard_for_rating
import aiofiles


# если в главном меню выбрали "отнеси мою новость к нужной теме"
@router.message(
    BotStates.main_menu_state,
    F.text.lower() == "отнеси мою новость к нужной теме"
)
async def task_chosen_topic(message: Message, state: FSMContext):
    await message.answer(
        text="Теперь, пожалуйста, выберите модель",
        reply_markup=keyboard_for_choosing_models()
    )
    await state.update_data(navigator="Подбери заголовок")
    await state.set_state(BotStates.choosing_model_state)


# если в главном меню выбрали "найди новость похожую на мою"
@router.message(
    BotStates.main_menu_state,
    F.text.lower() == "найди новость похожую на мою"
)
async def task_chosen_sim(message: Message, state: FSMContext):
    await message.answer(
        text="Вы выбрали поиск похожей новости!\nТеперь вставьте сюда текст Вашей новости",
        reply_markup=keyboard_for_leaf_vertex()
    )
    await state.update_data(navigator="Поиск похожего")
    await state.set_state(BotStates.sim_state)


# если в главном меню выбрали "Оценить юота"
@router.message(
    BotStates.main_menu_state,
    F.text.lower() == "оценить бота"
)
async def task_chosen_rate(message: Message, state: FSMContext):
    # Проверяем, оставлял ли пользователь оценку ранее
    user_data = await state.get_data()
    user_name = user_data['user_name']
    users = []
    try:
        async with aiofiles.open("rating", 'r') as file:
            async for line in file:
                users.append(line.split(':')[0].strip())
    except FileNotFoundError:
        users = []
    if user_name in users:
        await message.answer(
            text="Пользователь с таким именем уже оценил бота❗"
                 "\nЧтобы изменить оценку нажмите на кнопку из списка ниже",
            reply_markup=keyboard_for_rating())
    else:
        await message.answer(
            text="Спасибо, что решили оценить бота!\nВыберите оценку из списка ниже",
            reply_markup=keyboard_for_rating()
        )
    await state.update_data(navigator="Оценка бота")
    await state.set_state(BotStates.rate_state)
