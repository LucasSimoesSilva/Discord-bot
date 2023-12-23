from discord.ext import commands
from util import time_until
import datetime as datetime


class Birthday(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    @commands.command(aliases=['birth'], description='Description: Shows the name of all registered birthday people and'
                                                     ' how far until their birthday\n'
                                                     'Return: Lucas: 128 days until your birthday')
    async def birthday(self, ctx):
        for key, value in get_all_birthdays().items():
            value += f'-{str(datetime.datetime.now().year)}'
            await ctx.send(f'{key}: {time_until(value)}')


async def setup(bot):
    await bot.add_cog(Birthday(bot))


def get_all_birthdays():
    file_birthdays = open(f"./files/birthdays.txt", "r")
    birthdays = {}
    for line in file_birthdays:
        name = line.find('=')
        birthdays[line[:name - 1]] = line[name + 2:].replace('\n', '')
    return birthdays
