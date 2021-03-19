from datum_point_calculation import GetDatumPointOverWaze
import os, json


''' 
The function bellow is my way to work with GetDatumPointOverWaze api.
you can implement the GetDatumPointOverWaze api as you want.
'''
def get_datum_point(locations=""):

	datum_list = []
	for address in locations:
		addr_info = GetDatumPointOverWaze(address)
		datum_point = addr_info.address_to_coords()
		datum_list.append({address: tuple(datum_point.values())[:2]})
	return datum_list


print(get_datum_point(["Tel Aviv, Azrieli"]))