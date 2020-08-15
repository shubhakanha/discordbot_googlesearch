from googlesearch import search


def search_from_google(query):
    result_list = []
    for i in search(query, tld='com', lang='en', num=5, start=0, stop=5, pause=1.0):
        result_list.append(i)
    return result_list