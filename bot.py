from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = 'ТОКЕН'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("test", 
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test", 
web_app=WebAppInfo(url="https://senpay701.github.io/webapp/"))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)