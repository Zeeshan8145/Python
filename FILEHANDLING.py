try:
    with open(r"C:\Users\ZEESHAN\Desktop\pythonn.txt") as fh:
        for line in fh:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please check the filename and location.")

with open(r"C:\Users\ZEESHAN\Desktop\pythonn.txt") as f:
    lines = [line.rstrip() for line in f]
with open(r"C:\Users\ZEESHAN\Desktop\pythonn_copy.txt", 'w') as fw:
      fw.write('\n'.join(lines))

from collections import Counter
from string import ascii_letters
chars = ascii_letters + ' '
def sanitize(s, chars):
  return ''.join(c for c in s if c in chars)
def reverse(s):
    return s[::-1]
with open(r'C:\Users\ZEESHAN\Desktop\pythonn.txt') as stream:
   lines = [line.rstrip() for line in stream]
with open(r'C:\Users\ZEESHAN\Desktop\testtttt.txt', 'w') as stream:
   stream.write('\n'.join(reverse(line) for line in lines))
# now we can calculate some statistics
lines = [sanitize(line, chars) for line in lines]
whole = ' '.join(lines)
print(whole)
cnt = Counter(whole.lower().split())
print(cnt.most_common(3))

import shutil
import os

BASE_PATH = 'ops_example' # this will be our base path
os.mkdir(BASE_PATH)
path_b = os.path.join(BASE_PATH, 'A', 'B')
path_c = os.path.join(BASE_PATH, 'A', 'C')
path_d = os.path.join(BASE_PATH, 'A', 'D')
os.makedirs(path_b)
os.makedirs(path_c)
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(os.path.join(path_b, filename), 'w') as stream:
         stream.write(f'Some content here in {filename}\n')
shutil.move(path_b, path_d)
shutil.move(
 os.path.join(path_d, 'ex1.txt'),
 os.path.join(path_d, 'ex1d.txt')
)

import os

desktop_path = r"C:\Users\ZEESHAN\Desktop"
for root, dirs, files in os.walk(desktop_path):
   print(os.path.abspath(root))
   if dirs:
     print('Directories:')
     for dir_ in dirs:
       print(dir_)
     print()
   if files:
     print('Files:')
     for filename in files:
       print(filename)
     print()

import json
class ComplexEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, complex):
      return {
        '_meta': '_complex',
        'num': [obj.real, obj.imag],
        }
    return json.JSONEncoder.default(self, obj)
data = {
 'an_int': 42,
 'a_float': 3.14159265,
 'a_complex': 3 + 4j,
}
json_data = json.dumps(data, cls=ComplexEncoder)
print(json_data)
def object_hook(obj):
  try:
    if obj['_meta'] == '_complex':
      return complex(*obj['num'])
  except (KeyError, TypeError):
    return obj
data_out = json.loads(json_data, object_hook=object_hook)
print(data_out)

import requests
urls = {
    'get': 'https://httpbin.org/get?title=learn+python+programming',
    'headers': 'https://httpbin.org/headers',
    'ip': 'https://httpbin.org/ip',
    'user-agent': 'https://httpbin.org/user-agent',
    'UUID': 'https://httpbin.org/uuid',
}
def get_content(title, url):
  resp = requests.get(url)
  print(f'Response for {title}')
  print(resp.json())
for title, url in urls.items():
   get_content(title, url)
   print('-' * 40)
url = 'https://httpbin.org/post'
data = dict(title='Learn Python Programming')
resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())

