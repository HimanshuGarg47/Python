def get_domain_name(url):
    # remove protocol (http/https)
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    # remove www prefix (if it exists)
    if url.startswith('www.'):
        url = url[4:]
    # remove path and query parameters
    url = url.split('/')[0]
    # return domain name
    return url


url1 = 'https://www.abc.com/random.html'
url2 = 'http://www.abc.com/hello/random.html'
url3 = 'www.abc.com'
url4 = 'http://abc.com'

print(get_domain_name(url1))  # output: 'abc.com'
print(get_domain_name(url2))  # output: 'abc.com'
print(get_domain_name(url3))  # output: 'abc.com'
print(get_domain_name(url4))  # output: 'abc.com'
