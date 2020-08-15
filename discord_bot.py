import discord

import settings
from bot_db import get_recent_search_data, save_search_keyword
from google_search import search_from_google

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    #reply hey to hi message
    if message.content.startswith('hi'):
        await message.channel.send('Hey')

    #fetch google results and update keyword into mysql db
    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        user_id = message.author.id

        #save search keyword to db
        save_search_keyword(user_id, query)

        #to search from google
        google_result = search_from_google(query)
        if google_result:
            links = ' \n'.join(google_result)
            msg = 'Hello, you searched for {}. The top five results are: \n {}'.format(query, links)
        else:
            msg = 'Hello, you searched for {}. \n Sorry, no matching links found.'.format(query)

        await message.channel.send(msg)

    #return searhced keywords data based on a match keyword
    if message.content.startswith('!recent'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id

        #get related searched keyword history
        results = get_recent_search_data(author_id, query)
        if len(results) > 0:
            keywords = 'Your matching search results are: \n' + ' \n'.join([x[1] for x in results])
        else:
            keywords = 'No matching results found'

        await message.channel.send(keywords)

token = settings.BOT_TOKEN
client.run(token)