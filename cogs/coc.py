import discord
import sys
import os
import io
import json
import aiohttp
from discord.ext import commands


class coc:
    def __init__(self, bot):
        self.bot = bot
        self.client = {'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM4MjA0NGYyLWQ1ZjEtNDNhMS05ZDBjLWI3ZDcxZTgzZTc0ZSIsImlhdCI6MTUxNjc0Mzc5MSwic3ViIjoiZGV2ZWxvcGVyLzRjZDgyZTdlLWYzNTEtYWEyMi0xYjZhLTU3MWUyZjhkNmM2NiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4LjIxNy4yMDUuNyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.NE-RwoECn6y3DpprAOQsIqD0BkKjbea4Qi_EqRw4pozRexogizofvj5bJBqZ97CpnCpCVs2ZenhuJXV1VqE71Q"}



    @commands.command()
    async def cocsave(self, ctx, coctag=None):
        '''Saves a Clash of Clans tag to your Discord account.'''
        if coctag is None:
            return await ctx.send('Oops! Enter a tag to save! Usage: *cocsave [tag]')
        coctag = coctag.strip('#')
        for char in coctag:
            if char.upper() not in '0289PYLQGRJCUV':
        		return await ctx.send(f'Oops again! Looks like your tag `#{coctag}` is not a valid tag!')
        with open("data/crtags.json", "r+") as f:
            lol = json.load(f)
            lol[ctx.author.id] = coctag
            json.dump(lol, f, indent=4)
            await ctx.send("Success. :white_check_mark: Your tag is now saved to your account.")



    @commands.command()
    async def cocprofile(self, ctx, coctag=None):
        '''Gets a Clash of Clans profile! Yay!'''
        if coctag is None:
            with open('data/coctags.json') as f:
                lol = json.load(f)
                coctag = lol[ctx.author.id]
                if coctag is None:
                    await ctx.send("Uh-oh, no tag found! Use *cocsave [tag] to save your tag to your Discord account. :x:")
                else:               
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.clashofclans.com/v1/players/%23{coctag}', headers=self.client) as resp:
                            resp = await resp.json()
                            color = discord.Color(value=0xe5f442)
                            em = discord.Embed(color=color, title=f"{resp['name']}, {resp['tag']}")
                            em.add_field(name='XP Level', value=resp['expLevel'])
                            em.add_field(name='Trophies', value=resp['trophies'])
                            try:
                                leaguename = resp['league']['name']
                            except KeyError:
                                leaguename = 'Unranked'
                            em.add_field(name='League', value=leaguename)
                            em.add_field(name='Best Trophies', value=resp['bestTrophies'])
                            em.add_field(name='Town Hall', value=resp['townHallLevel'])
                            em.add_field(name='Attack Wins', value=resp['attackWins'])
                            em.add_field(name='Defense Wins', value=resp['defenseWins'])
                            em.add_field(name='Donations', value=resp['donations'])
                            em.add_field(name='Donations Received', value=resp['donationsReceived'])
                            em.add_field(name='War Stars', value=resp['warStars'])
                            try:
                                em.set_thumbnail(url=resp['league']['iconUrls']['medium'])
                            except KeyError:
                                em.set_thumbnail(url='http://clash-wiki.com/images/progress/leagues/no_league.png')
                            em.set_author(name='Normal Base')
                            await ctx.send(embed=em)
                            try:
                                em = discord.Embed(color=discord.Color(value=0xe5f442))
                                em.add_field(name='Builder Hall', value=resp['builderHallLevel'])
                                em.add_field(name='Trophies', value=resp['versusTrophies'])
                                em.add_field(name='Personal Best', value=resp['bestVersusTrophies'])
                                em.add_field(name='Attack Wins', value=resp['versusBattleWins'])
                                em.set_author(name='Builder Base')
                                await ctx.send(embed=em)
                            except KeyError:
                                em = discord.Embed(color=discord.Color(value=0xe5f442))
                                em.description = 'Builder Base is not unlocked yet! Hit Town Hall 4 to unlock.'
                                em.set_author(name='Builder Base')
                                await ctx.send(embed=em)
                            color = discord.Color(value=0xe5f442)
                            try:
                                em = discord.Embed(color=color, title=f"{resp['clan']['name']}, #{resp['clan']['tag']}")
                                em.add_field(name='Clan Level', value=resp['clan']['clanLevel'])                            
                                types = {
                                    'member': 'Member',
                                    'admin': 'Elder',
                                    'coLeader': 'Co-Leader',
                                    'leader': 'Leader'
                                }
                                em.add_field(name='Clan Role', value=types[resp['role']])
                                em.set_author(name='Clan Info')
                                em.set_thumbnail(url=resp['clan']['badgeUrls']['medium'])
                                await ctx.send(embed=em)
                            except KeyError:
                                em = discord.Embed(color=color, title="No Clan")
                                em.set_thumbnail(url='https://cdn.discordapp.com/attachments/388146146029076480/405548101370380291/maxresdefault.jpg')
                                await ctx.send(embed=em)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.clashofclans.com/v1/players/%23{coctag}', headers=self.client) as resp:
                    resp = await resp.json()
                    color = discord.Color(value=0xe5f442)
                    em = discord.Embed(color=color, title=f"{resp['name']}, #{resp['tag']}")
                    em.add_field(name='XP Level', value=resp['expLevel'])
                    em.add_field(name='Trophies', value=resp['trophies'])
                    try:
                        leaguename = resp['league']['name']
                    except KeyError:
                        leaguename = 'Unranked'
                    em.add_field(name='League', value=leaguename)
                    em.add_field(name='Best Trophies', value=resp['bestTrophies'])
                    em.add_field(name='Town Hall', value=resp['townHallLevel'])
                    em.add_field(name='Attack Wins', value=resp['attackWins'])
                    em.add_field(name='Defense Wins', value=resp['defenseWins'])
                    em.add_field(name='Donations', value=resp['donations'])
                    em.add_field(name='Donations Received', value=resp['donationsReceived'])
                    em.add_field(name='War Stars', value=resp['warStars'])
                    try:
                        em.set_thumbnail(url=resp['league']['iconUrls']['medium'])
                    except KeyError:
                        em.set_thumbnail(url='http://clash-wiki.com/images/progress/leagues/no_league.png')
                    em.set_author(name='Normal Base')
                    await ctx.send(embed=em)
                    try:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.add_field(name='Builder Hall', value=resp['builderHallLevel'])
                        em.add_field(name='Trophies', value=resp['versusTrophies'])
                        em.add_field(name='Personal Best', value=resp['bestVersusTrophies'])
                        em.add_field(name='Attack Wins', value=resp['versusBattleWins'])
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=discord.Color(value=0xe5f442))
                        em.description = 'Builder Base is not unlocked yet! Hit Town Hall 4 to unlock.'
                        em.set_author(name='Builder Base')
                        await ctx.send(embed=em)
                    color = discord.Color(value=0xe5f442)
                    try:
                        em = discord.Embed(color=color, title=f"{resp['clan']['name']}, #{resp['clan']['tag']}")
                        em.add_field(name='Clan Level', value=resp['clan']['clanLevel'])                            
                        types = {
                            'member': 'Member',
                            'admin': 'Elder',
                            'coLeader': 'Co-Leader',
                            'leader': 'Leader'
                        }
                        em.add_field(name='Clan Role', value=types[resp['role']])
                        em.set_author(name='Clan Info')
                        em.set_thumbnail(url=resp['clan']['badgeUrls']['medium'])
                        await ctx.send(embed=em)
                    except KeyError:
                        em = discord.Embed(color=color, title="No Clan")
                        em.set_thumbnail(url='http://i1253.photobucket.com/albums/hh599/bananaboy21/maxresdefault_zpseuid4jln.jpg')
                        await ctx.send(embed=em)


def setup(bot): 
    bot.add_cog(coc(bot)) 


						







