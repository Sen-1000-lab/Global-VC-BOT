import disnake
from disnake.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name="ping",
        description="Botの応答速度を確認します"
    )
    async def ping(self, inter):

        latency = round(
            self.bot.latency * 1000
        )

        embed = disnake.Embed(
            title="🏓 Pong!",
            description=f"Latency: {latency}ms",
            color=disnake.Color.green()
        )

        await inter.response.send_message(
            embed=embed
        )


def setup(bot):
    bot.add_cog(
        Ping(bot)
    )
