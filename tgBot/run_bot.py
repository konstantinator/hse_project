import logging
import asyncio
import warnings
from aiogram import Bot, Dispatcher
from loader_for_models import load_models
from loader_for_data import prepare_dataset
from handlers.start_state import router
from handlers import back, choosing_models_state, main_menu_state, none_state, prob_state
from handlers import rating_state, start_state, text_analyse_state, registration_state

warnings.filterwarnings("ignore")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

lr, stopwords_ru, enc_full, dec = load_models()
df_base, vectors = prepare_dataset(enc_full)

print("Данные в моделе загружены")


# Запуск бота
async def main():
    bot = Bot(token="6708563519:AAHaTh5VfMYpkCUu8gHsBkCxIBGaY8mfOLo")
    dp = Dispatcher()
    dp.include_router(router)
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# await main()

# Если код запускакется не в колабе или юпитере
if __name__ == "__main__":
    asyncio.run(main())
