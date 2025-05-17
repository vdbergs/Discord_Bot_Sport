import unittest
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

class TestBot(unittest.TestCase):
    def test_bot_initialization(self):
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')
        self.assertIsNotNone(token, "DISCORD_TOKEN not set in .env")
        
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix='/', intents=intents)
        self.assertIsInstance(bot, commands.Bot)

if __name__ == '__main__':
    unittest.main()