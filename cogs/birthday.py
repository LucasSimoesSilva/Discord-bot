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

    @commands.command(description='Description: Add the person and his birthday in the database\n'
                                  'Example:.add_date Lucas 21-12'
                                  'Return:Lucas birthday was added to the database')
    async def add_date(self, ctx, name, date):
        add_birthday(name, date)
        await ctx.send(f'{name} birthday was added to the database')


async def setup(bot):
    await bot.add_cog(Birthday(bot))


def get_all_birthdays():
    file_birthdays = open(f"./files/birthdays.txt", "r")
    birthdays = {}
    for line in file_birthdays:
        name = line.find('=')
        birthdays[line[:name - 1]] = line[name + 2:].replace('\n', '')
    return birthdays


def add_birthday(name, date):
    file_birthdays = open(f"./files/birthdays.txt", "a")
    file_birthdays.write(f'\n{name} = {date}')
    file_birthdays.close()
    print('Birthday registered')
