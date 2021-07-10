import urllib.request as ur

with ur.urlopen('http://www.bbc.com/') as repsonse:
    html = repsonse.read()

print(html)