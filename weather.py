!pip install pyowm
from pyowm import OWM
owm = OWM('c685a7a08cf0f9d864caaebffa6e00a4')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('India,ASIA')
w = observation.weather
print(w)