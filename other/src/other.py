import discord
import os
import asyncio
from discord.ext import commands
from utils import randomorg, functions

class OtherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        channel = message.channel
        author = str(message.author)
        cantent = str(message.content)


        #if (str(message.author) == "Гошасс#8787" and str(message.content) == "СУЙ" or str(message.author) == "ΤχεΑμμιΡ#6109"and message.content == "СУЙ"):
        if (str(message.content) == "СУЙ"):
              if (author[len(author) - 4 : len(author)] in ["8787", "6109"]):
                  async with channel.typing():
                      await channel.send(file = discord.File('a1.jpg'))
        elif (cantent.lower().startswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi')) or cantent.lower().endswith(('ъуъ', 'ъyъ', 'ъγъ', 'iyi', 'iуi', 'iγi'))):
            await channel.send(file = discord.File('a2.jpg'))

        elif (str(message.content) in ["цвет пакажы", 'gimmie the color']):
            while (1 == 1):
                await message.author.roles[len(message.author.roles) - 1].edit(colour = discord.Colour.from_rgb(randomorg.integer(0, 255), randomorg.integer(0, 255), randomorg.integer(0, 255)), reason = None)
                await asyncio.sleep(5)

        elif (message.content.startswith(';')):
            cantent = cantent[1:]
            async def evaluate(ctn, _message = message):
                _bot = self.bot
                return eval(ctn)
            try:
                await channel.send(await evaluate(cantent))
            except Exception as e:
                functions.log(e, 'r', 'EVL')
        elif (message.content in ('<@!672115782439927840>', '<@!670692900593598530>')):
            ctx = await self.bot.get_context(message)
            await ctx.send('**Есть, сэр!**')
            if (message.author != self.bot.get_user(343001477133893632)):
                helpcog = self.bot.get_cog('HelpCommandCog')
                await helpcog.help(ctx)


def setup(bot):
    bot.add_cog(OtherCog(bot))
