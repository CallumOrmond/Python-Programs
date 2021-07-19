import googlesearch

query = input("Search - ")

for i in googlesearch.search(query, start=0, stop=10):
    print(i)
