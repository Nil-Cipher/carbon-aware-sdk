from geopy.geocoders import Nominatim
import json 

def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.reverse((latitude, longitude), language='en', zoom=10)  # Reverse geocoding

    if location:
        address = location.address
        return address
    else:
        return "Location information not available"

# def get_actual_coordinates(location_name):
#     geolocator = Nominatim(user_agent="my_geocoder")
#     location = geolocator.geocode(location_name)

#     if location:
#         actual_latitude = location.latitude
#         actual_longitude = location.longitude
#         return actual_latitude, actual_longitude
#     else:
#         return None, None

# Specify the path to your JSON file
json_file_path = "gke-regions.json"

# Open the JSON file and load its contents
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

for location, details in json_data.items():
    latitude, longitude = details["Latitude"], details["Longitude"]
    address = get_location_info(latitude, longitude)
    if address == details["Name"]:
        print(f"{details['Name']} matches {latitude}, {longitude}")
    else:
        print(f"queried: {address} does not match {details['Name']}")
