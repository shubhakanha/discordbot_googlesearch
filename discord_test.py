import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hello, I am Shubham')

client.run('NzQyNzkwNjkxMDk2MzYzMDU4.XzLPvQ.7ZLoWKTaJhnxA1O-K4Ot_1bm5W0')