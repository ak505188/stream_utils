import json
import urllib2
import sys

print str(sys.argv)
key = 'AIzaSyBuXpZ6CN2-WkXnorwt1BC-67vjEFaUOGg'

search = ""
if len(sys.argv) > 1:
  search = sys.argv[1]
  search = search.replace(" ", "+")
  print "Search: " + search 

# for x in range(1, len(sys.argv)):
#   search = search + sys.argv[x]
#   if x is not (len(sys.argv)):
#    search = search + "+"

APIurl = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + \
          search + '&key=' + key
data = json.load(urllib2.urlopen(APIurl))
for index in range(5):
  if 'videoId' in data['items'][index]['id']:
    print ("[" + str(index) + "]")
    print (data['items'][index]['snippet']['title'])
    print (data['items'][index]['snippet']['channelTitle'])
    print (data['items'][index]['snippet']['publishedAt'])
    print "www.youtube.com/watch/" + (data['items'][index]['id']['videoId']) + "\n"
