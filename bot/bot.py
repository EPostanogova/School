import logging
import asyncio

from keybord.keybord_button import reply_keyboard, reply_keyboard_gender
from questions import questions

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('LogTag')

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from congig.config import TOKEN
from stickers import stickers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Это бот предсказатель! Тут будет описание.")

@dp.message_handler(commands=["help"])
async def cmd_start(message: types.Message):
    await message.reply("start - краткая информация о боте \n" \
                        " help - список команд с описанием \n" \
                        "begin - начать опрос \n")

@dp.message_handler(commands=["begin"])
async def cmd_start(message: types.Message):
    for i in range(len(questions)):
        if i == 0:
            await message.answer(f'1:{questions[i]}?',reply_markup=reply_keyboard_gender)
        elif i==1:
            await message.answer('Введите ваш возраст')
        else:
            await message.answer(f'{i+1}:{questions[i]}?', reply_markup=reply_keyboard)

@dp.message_handler()
async def hello_response(msg:types.Message):
    if 'привет' in msg.text.lower():
        await bot.send_message(msg.from_user.id,f'Здравствуй,{msg.from_user.first_name}!')
        await bot.send_sticker(msg.from_user.id,sticker=stickers['Puppy'])

@dp.message_handler(content_types=["sticker"])
async def st(msg:types.Message):
    print(msg.sticker)
    await msg.reply("Круть!")
    await bot.send_sticker(msg.from_user.id, sticker=stickers['Like'])




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

