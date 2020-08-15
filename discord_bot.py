import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hi'):
        await message.channel.send('Hey')

token = ''

client.run(token)