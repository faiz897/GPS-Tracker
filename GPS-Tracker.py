# import the libraries 
import geocoder
import gmaps
import json
from geopy.geocoders import GoogleV3

APi = 'Your API key....'

def location_IP(IP):
    '''
    return the latitude and longitude of a location by IP address
    '''
    # search location with ip
    g = geocoder.ip(IP)
    # load all the fatching values in json format
    load_g = g.json
    # assign latitude and longitude for visualizing
    lat, lng = load_g["lat"], load_g["lng"]
    address = load_g["address"] 
        
    print(f"Your Current location is: {address} and Your IP is: {IP}")
    print(f"Current location latitude: {lat} and longitude: {lng}")
    
    return lat, lng

def direction(IP, name):
    '''
    this function returns the latitude and longitude of direction location by IP address of device and name of the location 
    '''
  	# geting the locaiton with ip
    me = location_IP("me")
    
    # acess the Google maps with google API key  
    geolocator = GoogleV3(api_key=API)
    # get all the fatch data regard to the name of the location
    loc = geolocator.geocode(name)
    
    # get the latitude and longitude of the location
    req_loc = (loc.latitude, loc.longitude)
    
    print(f"\nyour requested location is: {loc}")
    print(f"Requested location latitude: {loc.latitude} and longitude: {loc.longitude}")
    
    return me, req_loc

def main():
	'''
	Main function which can get the location by IP address and name of the location,
	return the direction for the requested location from current location 
	'''
	# unpack the current location and requested location
	me, req = direction("me", "Mumbai")
	# assign the latitude and longitude in list
	locations = [me, req]

	# setup the map
	fig = gmaps.figure(map_type="ROADMAP")
	# geting the directions from current location and desired location
	directions = gmaps.directions_layer(me, req)
	fig.add_layer(directions)
	# View the map
	fig

if __name__ == '__main__':
	# driver
	main()

