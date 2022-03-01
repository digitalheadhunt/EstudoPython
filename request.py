import urllib3

http = urllib3.PoolManager()
 
search = 'anal'
search.replace(' ','%')
main_url = 'www.google.com'
link = main_url + search
print(link)
url = http.request('GET',main_url)

print(url.status)

 