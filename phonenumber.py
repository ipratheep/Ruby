import getpass
import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

key = ''


def location():
    if key == "":
        text = "empty"
        return text
    else:
        number = input("Enter phone number with country code to track : ")
        phonenumber = phonenumbers.parse(number)
        location = phonenumbers.geocoder.description_for_number(phonenumber, 'en')
        print("Country : " + location)
        provider = carrier.name_for_number(phonenumber, 'en')
        print("Service provider :" + provider)
        geocoder = OpenCageGeocode(key)
        query = str(location)
        result = geocoder.geocode(query)
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        print(f"Coordinates : {lat},{lng}")

        mymap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=[location, provider, number]).add_to(mymap)
        mymap.save("/home/"+getpass.getuser()+"/Ruby/location.html")


