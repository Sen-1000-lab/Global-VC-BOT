import os
import asyncio

import disnake
from disnake.ext import commands

from config import TOKEN
from database import (
    connect_db,
    create_tables
)

intents = disnake.Intents.all()

bot = commands.InteractionBot(
    intents=intents
)


@bot.event
async def on_ready():

    print("=" * 50)
    print(f"Logged in as {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")
    print("=" * 50)


async def load_cogs():

    if not os.path.exists("./cogs"):
        os.makedirs("./cogs")

    for file in os.listdir("./cogs"):

        if file.endswith(".py"):

            try:

                bot.load_extension(
                    f"cogs.{file[:-3]}"
                )

                print(
                    f"✅ Loaded {file}"
                )

            except Exception as e:

                print(
                    f"❌ Failed {file}"
                )

                print(e)


async def startup():

    await connect_db()

    await create_tables()

    await load_cogs()


if __name__ == "__main__":

    asyncio.run(
        startup()
    )

    bot.run(
        TOKEN,
        reconnect=True
    )
