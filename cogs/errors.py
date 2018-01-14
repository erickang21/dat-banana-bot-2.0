import discord
from discord.ext import commands
import os
import io
import traceback
import sys
import time
import traceback
import asyncio
import random
import aiohttp
import pip
import sys
from discord.ext import commands


class errors:
	def __init__(self, bot):
		self.bot = bot


	async def on_command_error(self, ctx, error):
		if isinstance (error, commands.CommandNotFound):
			color = discord.Color(value=0xf44242)
			em = discord.Embed(color=color, title = "Error: Command not found")
			em.description = "Command not found. \n To see what I can do for you, type *help."
			em.add_field(name="Command Used: ", value = ctx.message.content)
			em.set_footer(text=f"Error caused by: {ctx.author.name}")
			await ctx.send(embed=em)


		elif isinstance(error, commands.CommandOnCooldown):
			color = discord.Color(value=0xf44242)
			em = discord.Embed(color=color, title = "Error: Command spam!")
			em.description = "You are using my commands too quickly! \n Enter the chill zone, please."
			em.set_footer(text=f"Error caused by: {ctx.author.name}")
			await ctx.send(embed=em)



		elif isinstance (error, commands.MissingPermissions):
			color = discord.Color(value=0xf44242)
			em = discord.Embed(color=color, title = "Error: You have missing permissions")
			em.description = "You don't have enough permissions to use this command."
			em.set_footer(text=f"Error caused by: {ctx.author.name}")
			await ctx.send(embed=em)
		

		elif isinstance(error, commands.NotOwner):
			color = discord.Color(value=0xf44242)
			em = discord.Embed(color=color, title = "Error: Not Owner")
			em.description = "You ain't my owner, so back off on these commands. :smirk:"
			em.set_footer(text=f"Error caused by: {ctx.author.name}")
			await ctx.send(embed=em)


		elif isinstance(error, commands.discord.Forbidden):
			color = discord.Color(value=0xf44242)
			em = discord.Embed(color=color, title = "Error: Bot has missing permissions")
			em.description = "I have missing permissions. I cannot perform this command. \n Administrator permission is recommended for full bot functionality."
			em.set_footer(text=f"Error caused by: {ctx.author.name}")
			await ctx.send(embed=em)







		else:
			print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
			traceback.print_exception(type(error),error,error.__traceback__, file=sys.stderr)





def setup(bot):
	bot.add_cog(errors(bot))
