import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)
    lst = tree.findall('result/geometry/location')
    lst1 = tree.findall('result')
    #TODO
    #Return lat,lng,adress
    for item in lst:
        print 'lat,lng', item.find('lat').text , item.find('lng').text
    for item1 in lst1:
        print  item1.find('formatted_address').text
        


