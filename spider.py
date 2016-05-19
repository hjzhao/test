#!/usr/local/bin/python3

"""http://python.usyiyi.cn/python_343/library/index.html"""

from urllib import request

url = "http://python.usyiyi.cn/python_343/library/index.html"
print(request.urlopen(url).read());