import urllib
import json
import sys

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
a = []
d = {}
s = []
while True:
    try:
        address = raw_input('Enter location: ')
    except:
        print "Wrong location"
        break
    
    if len(address) < 1 :
        print "Wrong location"
        break


    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data

    try: 
	    js = json.loads(str(data))
    except: 
	    js = None
    if 'status' not in js or js['status'] != 'OK':
	    sys.exit("Failure To Retrieve")
    place_id = js["results"][0]["formatted_address"]
    short_name = js["results"][0]["address_components"][0]['short_name']
    
    lat = js["results"][0]["geometry"]['location']['lat']
    a.append(lat)
    lng = js['results'][0]['geometry']['location']['lng']
    a.append(lng)
    a.append(str(place_id))
    s.append(short_name)
    d =  {str(s):a}
    print 'lat',lat,'lng',lng
    print place_id
    print short_name

    
    print d
    
    #place_id = js["results"][0]["place_id"]
    #print 'Place id',place_id

    #TODO
    #Return dictionary {short_name: [lat,lng,adress]}

'''
print 'lat',lat,'lng',lng
print location
print short_name
print dictionary
'''
