import urllib2
import json
import sys

website = sys.argv[0]

def geturllist(site):
    url = "https://web.archive.org/cdx/search/cdx?url=" + site + "&fl=digest,timestamp,urlkey&collapse=digest&filter=statuscode:200&output=json"
    data = json.load(urllib2.urlopen(url))
    result_dict = dict((x[0], x) for x in data).values()
    return(result_dict)

tocheck = geturllist(website)

for x in range(len(tocheck)): 
    print(x)
    url = "https://web.archive.org/web/" + tocheck[x][1] + "/http://www." + website
    print(url)
