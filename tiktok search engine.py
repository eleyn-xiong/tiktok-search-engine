from exa_py import Exa
exa = Exa('4c4c63e5-6319-4991-a531-de218935da0f')
query = input('Search here: ')
response = exa.search(
    query,
    num_results=10,
    type='keyword',
    include_domains=['https://www.tiktok.com'],
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()