# -*- coding: utf-8 -*-
"""


模块和包


"""



import os
print (os.path.isdir(r'C:\Windows'))
print (os.path.isfile(r'C:\Windows\notepad.exe'))



# python中动态导入模块

try:
    import json
except ImportError:
    import simplejson as json

print (json.dumps({'python':2.7}))

# Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。要“试用”某一新的特性，就可以通过导入__future__模块的某些功能来实现。



# from __future__  import unicode_literals
#
# s = 'am I an unicode?'
# print (isinstance(s, "unicode"))

