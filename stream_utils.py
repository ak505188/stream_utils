import json
import urllib2
import sys
import os

print str(sys.argv)
key = os.environ['YOUTUBE_API']

# Possible uses
# Search
# Stream
# Download
# -a Download audio -d Download to specific directory

# functions
def search(search_str):
  search_str = search_str.replace(" ", "+") 
  APIurl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + \
    search_str + '&key=' + key
  print search_str
  data = json.load(urllib2.urlopen(APIurl))
  for index in range(5):
    if 'videoId' in data['items'][index]['id']:
      print ("[" + str(index) + "]")
      print (data['items'][index]['snippet']['title'])
      print (data['items'][index]['snippet']['channelTitle'])
      print (data['items'][index]['snippet']['publishedAt'])
      print "www.youtube.com/watch/" + (data['items'][index]['id']['videoId']) + "\n"
  return 1;

search(sys.argv[1])
# for x in range(1, len(sys.argv)):
#   search = search + sys.argv[x]
#   if x is not (len(sys.argv)):
#    search = search + "+"


