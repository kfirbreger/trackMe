"""
Open Weather API support to get weather information
"""
import requests
import datetime

URL = "http://api.openweathermap.org/data/2.5/onecall/timemachine"

def get(**kwargs):
    """
    Retrieves the data of the given location at a given date.
    If non is given, getting the one for yesterday
    """
    lat = kwargs.get("lat", None)
    lon = kwargs.get("lon", None)
    api_key = kwargs.get("openweather_api_key", None)
    if lat is None or lon is None or api_key is None:
        print("Missing required keys")
        return

