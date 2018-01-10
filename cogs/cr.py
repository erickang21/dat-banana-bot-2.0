import discord
import sys
import os
import io
import json
import clashroyale
from discord.ext import commands


class cr:
    def __init__(self, bot):
        self.bot = bot
        self.client = clashroyale.Client("607d4e53a8b643f1bbb7837bacb7ec3c4706bc9420b34377a869d8048500f998", is_async=True)
    

    @commands.command()
    async def crsave(self, ctx, tag:str):
        """Saves your CR tag to your account. Usage: *crsave [player tag]"""
        if tag is None:
            return await ctx.send("Please enter a tag to save. Usage: *crsave [tag]")
        else:
            try:
                tag = tag.strip("#")
                await self.client.get_player(tag)
                for char in tag:
                    if char.upper() not in '0289PYLQGRJCUV':
                        return await ctx.send("That must be an invalid tag. Please use a valid tag. :x:")
            except (clashroyale.errors.NotResponding, clashroyale.errors.ServerError) as e:
                color = discord.Color(value=0xf44242)
                em = discord.Embed(color=color, title='An error occured.')
                em.description = 'Error code **{e.code}**: {e.error}'
                return await ctx.send(embed=em)
            with open("data/crtags.json", "r+") as f:
                lol = json.load(f)
                lol[ctx.author.id] = tag
                f.write(json.dumps(lol, indent=4))
                f.close()
                return await ctx.send("Success. :white_check_mark: Your tag is now saved to your account.")


    @commands.command()
    async def crprofile(self, ctx, crtag:str):
        """Gets those sweet Stats for CR...Usage: *crprofile [tag]"""
        if crtag is None:
            with open("data/crtags.json") as f:
                lol = json.load(f)
                try:
                    crtag = lol[ctx.author.id]
                except:
                    return await ctx.send("Uh-oh, no tag found. Use *crsave [tag] to save your player tag first.")
                try:
                    profile = await self.client.get_player(crtag)
                except (clashroyale.errors.NotResponding, clashroyale.errors.ServerError) as e:
                    color = discord.Color(value=0xf44242)
                    em = discord.Embed(color=color, title='An error occured.')
                    em.description = 'Error code **{e.code}**: {e.error}'
                    return await ctx.send(embed=em)
                color = discord.Color(value=0xf1f442)
                em = discord.Embed(color=color, title=f'{profile.name} ({profile.tag})')
                em.add_field(name='Trophies', value=f'{profile.trophies}')
                em.add_field(name='Personal Best', value=f'{profile.stats.max_trophies}')
                em.add_field(name='XP Level', value=f'{profile.stats.level}')
                em.add_field(name='Arena', value=f'{profile.arena.name}')
                em.add_field(name='Wins/Losses/Draws', value=f'{profile.games.wins}/{profile.games.draws}/{profile.games.losses}')
                em.add_field(name='Win Rate', value=f'{(profile.games.wins / (profile.games.wins + profile.games.losses) * 100):.3f}%')
                em.add_field(name='Favorite Card', value=f'{profile.stats.favorite_card.name}')                                                                                                                                                 
                em.set_author(name=f'dat banana bot Stats')
                em.set_thumbnail(url=f'https://cr-api.github.io/cr-api-assets/arenas/arena{profile.arena.arenaID}.png') # This allows thumbnail to match your arena! Maybe it IS possible after all...
                await ctx.send(embed=em)
                profile = await self.client.get_player(crtag)
                try:
                    clan = await profile.get_clan()
                except:
                    pass
                if profile.clan.role:
                    color = discord.Color(value=0xf1f442)
                    em = discord.Embed(color=color, title='Clan')
                    em.description = f'{clan.name} (#{clan.tag})'
                    em.add_field(name='Role', value=f'{profile.clan.role}')                                                                                                                                                                      
                    em.add_field(name='Clan Score', value=f'{clan.score}')
                    em.add_field(name='Members', value=f'{len(clan.members)}/50')
                    em.set_thumbnail(url=clan.badge.image)
                    await ctx.send(embed=em)
                else:
                    color = discord.Color(value=0xf1f442)
                    em = discord.Embed(color=color, title='Clan')
                    em.description = 'No Clan'
                    em.set_thumbnail(url='http://i1253.photobucket.com/albums/hh599/bananaboy21/maxresdefault_zpseuid4jln.jpg') # This is the url for the No Clan symbol.   
                    await ctx.send(embed=em)
                profile = await self.client.get_player(crtag)
                color = discord.Color(value=0xf1f442)
                em = discord.Embed(color=color)
                em.add_field(name='Challenge Max Wins', value=f'{profile.stats.challenge_max_wins}')
                em.add_field(name='Challenge Cards Won', value=f'{profile.stats.challenge_cards_won}')
                em.add_field(name='Tourney Cards Won', value=f'{profile.stats.tournament_cards_won}')
                em.set_author(name='Challenge/Tourney Stats')
                em.set_thumbnail(url='http://vignette4.wikia.nocookie.net/clashroyale/images/a/a7/TournamentIcon.png/revision/latest?cb=20160704151823')
                em.set_footer(text='cr-api.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
                await ctx.send(embed=em)


    @commands.command()
    async def crclan(self, ctx, crtag:str):
        """Shows info for a clan. Usage: *crclan [CLAN TAG]"""
        if crtag is None:
            with open("data/crtags.json") as f:
                lol = json.load(f)
                try:
                    crtag = lol[ctx.author.id]
                except:
                    return await ctx.send("Uh-oh, no tag found. Use *crsave [tag] to save your player tag first.")
                try:
                    profile = await self.client.get_player(crtag)
                    clan = await profile.get_clan()
                except (clashroyale.errors.NotResponding, clashroyale.errors.ServerError) as e:
                    color = discord.Color(value=0xf44242)
                    em = discord.Embed(color=color, title='An error occured.')
                    em.description = 'Error code **{e.code}**: {e.error}'
                    return await ctx.send(embed=em)
                color = discord.Color(value=0xf1f442)
                em = discord.Embed(color=color, title=f'{clan.name}')
                em.description = f'{clan.description}'
                em.add_field(name='Clan Trophies', value=f'{clan.score}')
                em.add_field(name='Members', value=f'{clan.memberCount}/50')
                em.add_field(name='Type', value=f'{clan.type}')
                em.add_field(name='Weekly Donations', value=f'{clan.donations}')
                em.add_field(name='Location', value=f'{clan.location.name}')
                if clan.clan_chest.status == 'inactive':
                    tier = "Inactive"
                else:
                    crowns = 0
                    for m in clan.members:
                        crowns += m.clan_chest_crowns
                    if crowns < 70:
                        tier = "0/10"
                    if crowns > 70 and crowns < 160:
                        tier = "1/10"
                    if crowns > 160 and crowns < 270:
                        tier = "2/10"
                    if crowns > 270 and crowns < 400:
                        tier = "3/10"
                    if crowns > 400 and crowns < 550:
                        tier = "4/10"
                    if crowns > 550 and crowns < 720:
                        tier = "5/10"
                    if crowns > 720 and crowns < 910:
                        tier = "6/10"
                    if crowns > 910 and crowns < 1120:
                        tier = "7/10"
                    if crowns > 1120 and crowns < 1350:
                        tier = "8/10"
                    if crowns > 1350 and crowns < 1600:
                        tier = "9/10"
                    if crowns == 1600:
                        tier = "10/10"
                em.add_field(name='Clan Chest Tier', value=f'{tier}')
                em.add_field(name='Trophy Requirement', value=f'{clan.requiredScore}')
                em.set_author(name=f'#{clan.tag}')
                em.set_thumbnail(url=f'{clan.badge.image}')
                em.set_footer(text='cr-api.com', icon_url='http://cr-api.com/static/img/branding/cr-api-logo.png')
                await ctx.send(embed=em)



        

def setup(bot): 
    bot.add_cog(cr(bot)) 
