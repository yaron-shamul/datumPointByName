
import requests


class GetDatumPointOverWaze(object):
	"""Calculate actual route time and distance with Waze API"""

	WAZE_URL = "https://www.waze.com/"
	HEADERS = {
		"User-Agent": "Mozilla/5.0",
		"referer": WAZE_URL,
	}

		
	def __init__(self, address):
		self.BASE_COORDS = {"lat": 31.768, "lon": 35.214} # Change to your capital city
		self.COORD_SERVERS = 'il-SearchServer/mozi'
		self.address = address
		
		
	def address_to_coords(self):
		"""Convert address to coordinates"""
		base_coords = self.BASE_COORDS
		get_cord = self.COORD_SERVERS
		url_options = {
			"q": self.address,
			"lang": "eng",
			"origin": "livemap",
			"lat": self.BASE_COORDS["lat"],
			"lon": self.BASE_COORDS["lon"]
		}
		try:
			response = requests.get(self.WAZE_URL + get_cord, params=url_options, headers=self.HEADERS)
			for response_json in response.json():
				if response_json.get('city'):
					lat = response_json['location']['lat']
					lon = response_json['location']['lon']
					bounds = response_json['bounds']  # sometimes the coords don't match up
					if bounds is not None:
						bounds['top'], bounds['bottom'] = max(bounds['top'], bounds['bottom']), min(bounds['top'], bounds['bottom'])
						bounds['left'], bounds['right'] = min(bounds['left'], bounds['right']), max(bounds['left'], bounds['right'])
					else:
						bounds = {}
					return {"lat": lat, "lon": lon, "bounds": bounds}

		except Exception as e:
			print(e)
		
		return self.BASE_COORDS , {"bounds": 1}

