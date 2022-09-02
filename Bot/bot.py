from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

# Made by @Your_senpay

API_TOKEN = 'YOUR_TOKEN'
URL = 'YOUR_LINK'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="WebApp", web_app=WebAppInfo(url=URL))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)