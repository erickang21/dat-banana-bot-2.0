import discord
import sys
import os
import io
import clashroyale
from discord.ext import commands


class cr:
    def __init__(self, bot):
        self.bot = bot
        self.client = clashroyale.Client("607d4e53a8b643f1bbb7837bacb7ec3c4706bc9420b34377a869d8048500f998", is_async=True)
        

    @commands.command()
    async def crprofile(self, ctx, crtag:str):
        """Shows CR stats for you! Usage: *crprofile [tag]"""
        if crtag is None:
            await ctx.send('Please enter your tag. Usage: *crprofile [tag].') # Bot hosts on Heroku, which means there is no save tag feature (Heroku deletes data every day.)
        else:
            profile = await self.client.get_player(crtag)
            clan = await profile.get_clan()
            color = discord.Color(value=0xf1f442)
            em = discord.Embed(color=color, title=f'{profile.name}')
            em.description = f'#{profile.tag}'
            if profile.clan.role:
                em.set_author(name=f'{clan.name}')
            else:
                em.set_author(name='No Clan')
            em.add_field(name='Trophies', value=f'{profile.trophies}')
            em.add_field(name='Personal Best', value=f'{profile.stats.max_trophies}')
            em.add_field(name='XP Level', value=f'{profile.stats.level}')
            em.add_field(name='Arena', value=f'{profile.arena.name}')
            em.add_field(name='Wins/Losses/Draws', value=f'{profile.games.wins}/{profile.games.draws}/{profile.games.losses}')
            em.add_field(name='Win Rate', value=f'{(profile.games.wins / (profile.games.wins + profile.games.losses) * 100):.3f}%')
            em.set_thumbnail(url=f'https://cr-api.github.io/cr-api-assets/arenas/arena{profile.arena.arenaID}.png')
            await ctx.send(embed=em)
        

def setup(bot): 
    bot.add_cog(cr(bot)) 
