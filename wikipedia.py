import wikipediaapi
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

wiki = wikipediaapi.Wikipedia('en')


bot = Bot(token='6194013269:AAE5lMRfu4mZgmZNihSKboCs6lxjSdhMBNk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	await message.reply('Wikipediadan qidirish 🔎\n\nMisol uchun\n\n<code>/wikiuz salom</code>  🇺🇿\n\n<code>/wikiru привет</code> 🇷🇺\n\n<code>/wikien Helo</code> 🇺🇸',parse_mode='HTML')
	
	@dp.message_handler(commands=['wikien'])
	async def send_wikipedia_en(message: types.Message):
		en=await message.reply('Searching wikipedia 🇺🇸...')
		search_term = message.text.split('/wikien')[1].strip()
		page = wiki.page(search_term)
		if page.exists():
			await message.answer(page.summary)
			await en.delete()
		else:
			await message.reply('Sorry, I could not find any information on Wikipedia. 😔')
			await en.delete()

@dp.message_handler(commands=['wikiru'])
async def send_wikipedia_ru(message: types.Message):
	ru=await message.reply('Searching wikipedia 🇷🇺...')
	search_term = message.text.split('/wikiru')[1].strip()
	wiki_ru = wikipediaapi.Wikipedia('ru')
	page = wiki_ru.page(search_term)
	if page.exists():
		await message.answer(page.summary)
		await ru.delete()
	else:
		await message.reply('Извините, я не смог найти информацию на Википедии 😔')
		await ru.delete()
		
@dp.message_handler(commands=['wikiuz'])
async def send_wikipedia_uz(message: types.Message):
	uz=await message.reply('Searching wikipedia 🇺🇿 ...')
	search_term = message.text.split('/wikiuz')[1].strip()
	wiki_uz = wikipediaapi.Wikipedia('uz')
	page = wiki_uz.page(search_term)
	if page.exists():
		await message.reply(page.summary)
		await uz.delete()
	else:
		await message.reply('Kechirasiz, Wikipedia da malumot topilmadi. 😔')
		await uz.delete()


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)

