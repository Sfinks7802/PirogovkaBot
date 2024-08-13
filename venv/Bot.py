from aiogram import Bot
import os
from aiogram.client.default import DefaultBotProperties


bot = Bot(token=os.environ.get('BotToken'),
          default=DefaultBotProperties(
              parse_mode='HTML'
          ))