# 0x11. Python - Network #1

## urllib

### HOWTO Fetch Internet Resources Using The urllib Package

The urllib package in Python is used to fetch internet resources. The package includes several modules for different purposes such as:

urllib.request: This module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies, and more.
urllib.parse: This module provides functions for parsing URLs and their components, as well as for handling percent-encoded characters.
urllib.error: This module defines the exception classes for the exceptions that are raised by the urllib.request module.
Here is an example of how to use the urllib.request module to fetch the content of a webpage:

```
import urllib.request

url = "https://www.example.com"

response = urllib.request.urlopen(url)
webContent = response.read()
print(webContent)
```

This will open the specified URL and read the content of the webpage, which is then stored in the webContent variable. The read() function can be used to read the content of the webpage.

- You can also add some custom headers to the request, like this:

```
import urllib.request

url = "https://www.example.com"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
webContent = response.read()
print(webContent)

```

You can also send POST request using urllib package by using the urllib.request.urlopen function and passing data in the data parameter, like this:

```
import urllib.parse
import urllib.request

url = 'http://httpbin.org/post'
data = urllib.parse.urlencode({'key': 'value'})
data = data.encode('ascii')
req = urllib.request.Request(url, data=data)
with urllib.request.urlopen(req) as response

```
