# from googlesearch import search


def search_from_google(query):
    result_list = []
    # for i in search(query, tld='com', lang='en', num=5, start=0, stop=5, pause=1.0):
    #     result_list.append(i)

    result_list = ['https://www.java.com/', 'https://www.oracle.com/java/technologies/',
                   'https://www.lifewire.com/what-is-java-4172382',
                   'https://en.wikipedia.org/wiki/Java_(programming_language)',
                   'https://www.oracle.com/in/java/technologies/javase-downloads.html']

    return result_list