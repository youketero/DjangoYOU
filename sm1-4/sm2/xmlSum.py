import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'comments_283746.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
commentinfo = ET.fromstring(data)
lst = commentinfo.findall('comments/comment')
#TODO
#Find sum in count elements
it = 0
for item in lst:
    it = it+ int(item.find('count').text)
print it    




