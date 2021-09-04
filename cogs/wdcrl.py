from discord.ext import commands
import discord 

class creditscore(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creditscore(self, ctx, *, content):
        data = list(content.split(" "))
        if len(data) == 2:
            try:
                await ctx.message.server.get_member(data[0])
            except: 
                await ctx.send('错误')
        else: 
            await ctx.send('错误')
        

def setup(client):
    client.add_cog(creditscore(client))
