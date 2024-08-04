import asyncio
import contextlib
from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging

BOT_TOKEN = "7221014149:AAEoUo1LxEfmCE6C1meZoVMfkZeLduCKgbg"
CHANNEL_ID = -1001996706005
ADMIN_ID = 6286994381


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = ("Olá beleza 👋🏻👸🏻 Estou aqui para te mostrar uma maneira legal de ganhar comigo.\n"
           "\nSou o bot da Samira e posso te enviar as melhores ofertas se você me escrever agora mesmo 🤖\n"
           "\nMe escreve 👉🏻@Samira_Rod_vip")
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as exc:
        logging.error(f'[Exception] - {exc}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
