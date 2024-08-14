from aiogram import Bot
import os
from aiogram.client.default import DefaultBotProperties


bot = Bot(token=os.environ.get('BotToken'),
          default=DefaultBotProperties(
              parse_mode='HTML'
          ))
all_media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_media')
