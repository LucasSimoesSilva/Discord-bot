from discord.ext import commands
from util import util


class Util(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    # This command is very 'dangerous'. You can delete messages you don't want. Be careful
    @commands.command(description='Clears the number of messages given as a parameter\nExample:.clear 2'
                                  '\nReturn:This will erase the last 2 messages')
    async def clear(self, ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command(
        description='Description: Returns the amount of time left until the given date(birthday) and if the date is '
                    'today, return the message "HAPPY BIRTHDAY"\nStandard that the date needs to be given:'
                    ' "day-month-year"\nExample: 14-03-2024')
    async def date(self, ctx, date):
        await ctx.send(f'{util.time_until(date)}')


async def setup(bot):
    await bot.add_cog(Util(bot))
