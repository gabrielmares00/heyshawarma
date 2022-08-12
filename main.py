import asyncio
import logging
import os

from dotenv import load_dotenv

from classes.heyshawarma import HeyShawarma

bot = HeyShawarma()


async def main():
    load_dotenv()
    async with bot:

        await bot.start(os.getenv("DISCORD_KEY"))

if __name__ == "__main__":
    asyncio.run(main())
