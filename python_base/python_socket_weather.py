
import urllib.request
import json

def weather(city):
	city_code = '101010100' # the code of Beijing
	url = 'http://m.weather.com.cn/data/'+ city_code
	file = urllib.request.urlopen('http://m.weather.com.cn/data/'+ city_code)
	weatherHTML = file.read().decode('utf-8')
	weatherJSON = json.JSONDecoder().decode(weatherHTML)
	weatherInfo = weatherJSON['weatherinfo']

	print_info(weatherInfo)

def print_info(weatherInfo):
	print('city: ', weatherInfo['city'])
	print('time: ', weatherInfo['date_y'])
	
	print('Weather of 24 hours'.center(30,'*'))
	print('temperature: ', weatherInfo['temp1'] )
	print('weather: ', weatherInfo['weather1'])
	print('wind: ', weatherInfo['wind1'])
	print('UV: ', weatherInfo['index_uv']) # zi wai xian
	print('cloth: ',weatherInfo['index_d'])


if __name__ == '__main__':
	city = input('请输入城市名：')
	weather(city)
