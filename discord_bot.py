import discord
from google_search import search_from_google

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hi'):
        await message.channel.send('Hey')

    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        # post_search_data(author_id, query)

        results = search_from_google(query)
        if results:
            links = ' \n'.join(results)
            msg = 'Hello {}, you searched for {}. The top five results are: \n {}'.format( message.author.mention, query, links)
        else:
            msg = 'Hello {}, you searched for {}. \n Sorry, no matching links found.'.format(message.author.mention, query)

        await message.channel.send(msg)

token = ''

client.run(token)