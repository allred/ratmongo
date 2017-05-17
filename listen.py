#!/usr/bin/env python
from base import *

#print(reddit.read_only)
#print(subreddit.title)

def retrieve(url):
  file_temp = tempfile.NamedTemporaryFile(
    delete=False,
    mode='w+b',
    prefix='rmg-',
    suffix='.jpg',
  )
  print(file_temp.name)
  urllib.request.urlretrieve(url, file_temp.name)
  i = Image.open(file_temp.name)
  info = i._getexif()
  for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    #pp.pprint(decoded)
    #pp.pprint(value)



for submission in subreddit.stream.submissions():
  pp.pprint(inspect.getmembers(submission))
  if submission.preview:
    #pp.pprint(submission.preview['images'][0]['resolutions'][-1]['url'])
    url = submission.preview['images'][0]['resolutions'][-1]['url']
    retrieve(url)
    print(submission.title)
