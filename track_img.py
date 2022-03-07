import getpass
from GPSPhoto import gpsphoto
import folium


def img_meta():
    img = input("Enter path of image : ")
    data = gpsphoto.getGPSData(img)
    if len(data) == 0:
        text = "empty"
        return text
    else:
        lat = data['Latitude']
        lng = data['Longitude']
        date = data['Date']
        time = data['UTC-Time']
        alt = data['Altitude']

        mymap = folium.Map(location=(lat, lng), zoom_start=9)
        folium.Marker(location=(lat, lng), popup=(date, time, alt)).add_to(mymap)
        mymap.save("/home/"+getpass.getuser()+"/ruby/img_location.html")
