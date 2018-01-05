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
            try:
                profile = await self.client.get_player(crtag)
            except (clashroyale.errors.NotResponding, clashroyale.errors.ServerError) as e:
                color = discord.Color(value=0xf44242)
                em = discord.Embed(color=color, title='An error occured.')
                em.description = 'Error code **{e.code}**: {e.error}'
                return await ctx.send(embed=em)
            color = discord.Color(value=0xf1f442)
            em = discord.Embed(color=color, title=f'{profile.name}')
            em.add_field(name='Trophies', value=f'{profile.trophies}')
            em.add_field(name='Personal Best', value=f'{profile.stats.max_trophies}')
            em.add_field(name='XP Level', value=f'{profile.stats.level}')
            em.add_field(name='Arena', value=f'{profile.arena.name}')
            em.add_field(name='Wins/Losses/Draws', value=f'{profile.games.wins}/{profile.games.draws}/{profile.games.losses}')
            em.add_field(name='Win Rate', value=f'{(profile.games.wins / (profile.games.wins + profile.games.losses) * 100):.3f}%')
            em.add_field(name='Favorite Card', value=f'{profile.stats.favorite_card.name})                                                                                                                                                 
            em.set_author(name='Stats')
            em.set_thumbnail(url=f'https://cr-api.github.io/cr-api-assets/arenas/arena{profile.arena.arenaID}.png') # This allows thumbnail to match your arena! Maybe it IS possible after all...
            em.set_footer(text='API: cr-api.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
            await ctx.send(embed=em)
            profile = await self.client.get_player(crtag)
            try:
                clan = await profile.get_clan()
            except:
                pass
            color = discord.Color(value=0xf1f442)
            if profile.clan.role:
                em = discord.Embed(color=color)
                em.description = f'{clan.name} (#{clan.tag})'
                em.add_field(name='Role', value=f'{profile.clan.role})                                                                                                                                                                      
                em.add_field(name='Clan Score', value=f'{clan.score}')
                em.add_field(name='Members', value=f'{len(clan.members)}/50')
                em.set_thumbnail(url=clan.badge.image)
                em.set_footer(text='API: cr-api.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
                await ctx.send(embed=em)
            else:
                em.description = 'No Clan'
                em.set_thumbnail(url='http://i1253.photobucket.com/albums/hh599/bananaboy21/maxresdefault_zpseuid4jln.jpg') # This is the url for the No Clan symbol.
                em.set_footer(text='API: cr-api.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
                await ctx.send(embed=em)
            profile = await self.client.get_player(crtag)
            color = discord.Color(value=0xf1f442)
            em = discord.Embed(color=color)
            em.add_field(name='Challenge Max Wins'), value=f'{profile.stats.challenge_max_wins}')
            em.add_field(name='Challenge Cards Won', value=f'{profile.stats.challenge_cards_won}')
            em.add_field(name='Tourney Cards Won', value=f'{profile.stats.tournament_cards_won}')
            em.set_author(name='Challenge/Tourney Stats')
            em.set_thumbnail(url=http://vignette4.wikia.nocookie.net/clashroyale/images/a/a7/TournamentIcon.png/revision/latest?cb=20160704151823)
            await ctx.send(embed=em)



                         
            
        

def setup(bot): 
    bot.add_cog(cr(bot)) 
