import googlemaps
from googlemaps.exceptions import HTTPError

gmaps = googlemaps.Client('AIzaSyAwPCAuEsaMumBAn8vEurCa1sSE8mkSaxc')


def find_address(lat, long):
    # Look up an address with reverse geocoding
    # (52.3862755, 4.8728798)
    try:
        result = gmaps.reverse_geocode((lat, long))
        return result[0]['formatted_address']
    except HTTPError as e:
        print(e)

# https://maps.google.com/?q=52.3862755,4.8728798

print('good')
print(find_address(52.3862755, 4.8728798))
print('false')
print(find_address(1000.3862755, 1000.8728798))
