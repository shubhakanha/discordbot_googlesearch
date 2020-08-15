from googlesearch import search


#to get the google top 5 result
def search_from_google(query):
    urls_list = []
    for url in search(query, tld='com', lang='en', num=5, start=0, stop=5, pause=1.0):
        urls_list.append(url)
    return urls_list