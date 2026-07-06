import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
from google import genai
from google.genai import types as genai_types


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not BOT_TOKEN or not GEMINI_API_KEY:
    exit("Ошибка: Проверьте, заполнен ли файл .env! Не найден BOT_TOKEN или GEMINI_API_KEY.")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


client = genai.Client(api_key=GEMINI_API_KEY)


user_chats = {}



SYSTEM_INSTRUCTION = (
    "Ты — профессиональный переводчик и лингвистический ассистент, владеющий русским, английским и испанским языками. "
    "Твоя задача — автоматически и точно переводить тексты и надписи на изображениях, которые присылает пользователь. "
    "Правила перевода:\n"
    "1. Если текст прислан на русском языке — переведи его на английский и испанский языки (сделай два варианта).\n"
    "2. Если текст прислан на английском или испанском языке — переведи его на русский язык.\n"
    "3. Если пользователь прямо просит перевести на конкретный язык (например, 'переведи на испанский: привет'), "
    "выполни именно его просьбу.\n"
    "Помогай исправлять ошибки, объясняй сложные фразы и идиомы, если тебя об этом попросят."
)


def get_or_create_chat(user_id: int):
    if user_id not in user_chats:
        user_chats[user_id] = client.chats.create(
            model="gemini-2.5-flash",
            config=genai_types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
    return user_chats[user_id]




@dp.message(Command("start"))
async def start_cmd(message: types.Message):

    user_chats[message.from_user.id] = client.chats.create(
        model="gemini-2.5-flash",
        config=genai_types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        )
    )
    await message.answer(
        "Привет! Я твой персональный ИИ-переводчик на базе Gemini.\n\n"
        "• Я помню контекст нашей беседы.\n"
        "• Ты можешь прислать мне текст для перевода.\n"
        "• Ты можешь отправить мне фото с текстом, и я его переведу.\n\n"
        "Чтобы очистить мою память, используй команду /clear"
    )


@dp.message(Command("clear"))
async def clear_history(message: types.Message):

    if message.from_user.id in user_chats:
        del user_chats[message.from_user.id]
    await message.answer("🧹 История нашего диалога успешно очищена! Я готов к новым переводам.")


@dp.message(F.photo)
async def handle_photo(message: types.Message):

    photo = message.photo[-1]

    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:

        file_in_io = await bot.download(photo.file_id)
        photo_bytes = file_in_io.read()


        chat = get_or_create_chat(message.from_user.id)


        caption = message.caption or "Внимательно посмотри на это изображение, найди здесь весь текст и переведи его."


        response = chat.send_message(
            message=[
                genai_types.Part.from_bytes(
                    data=photo_bytes,
                    mime_type="image/jpeg",
                ),
                caption
            ]
        )
        await message.reply(response.text)

    except Exception as e:
        await message.reply(f"❌ Произошла ошибка при обработке фото: {e}")

@dp.message(F.text)
async def handle_text(message: types.Message):


    chat = get_or_create_chat(message.from_user.id)

    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:

        response = chat.send_message(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.reply(f"❌ Произошла ошибка: {e}")



async def main():
    print("Бот запущен и готов к работе...")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен пользователем.")