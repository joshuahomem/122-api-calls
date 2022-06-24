import requests
import json
from env.key import key

APIkey = key
again = True

def getInput():
    CoZ = input("Enter City Name (C)?: ")
    return CoZ.upper()
        
def getData(CoZ):
    if CoZ == "C":
        city = input("Enter City Name: ")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"
    elif CoZ == "Z":
        countrycode = input("Enter Country Code: ")
        zipcode = input("Enter Zip Code: ")
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={APIkey}"
    else:
        print("Invalid Input")
        exit()
             
    data = requests.get(url)
    jData = json.loads(data.text)
    return jData

def checkError(jData):
    if jData['cod'] == '404':
        return 1

    elif jData['cod'] == '400':
        return 2

    elif jData['cod'] == 200:
        return 3

def giveData(jData):
    def getCelsius(temp):
        #convert kelvin to celsius 
        return (temp - 273.15)

    cityname = jData['name']
    countryname = jData['sys']['country']
    temp = getCelsius(jData["main"]['temp'])
    ftemp = getCelsius(jData['main']['feels_like'])
    weather = (jData['weather'][0]['description'])
    humidity = jData['main']['humidity']
    
    return cityname, countryname, temp, ftemp, weather, humidity

def define_city(cityname, countryname, temp, ftemp, weather, humidity):
    currentCity = city(cityname, countryname, temp, ftemp, weather, humidity)
    return currentCity

class city():
    def __init__(self, cityname, countryname, temp, ftemp, weather, humidity):
        self.cityname = cityname
        self.countryname = countryname
        self.temp =  temp
        self.ftemp = ftemp
        self.weather = weather
        self.humidity = humidity

    def getNames(self, cityname, countryname):
        return (cityname + ", " + countryname)
    
    def getConditions(self, ftemp, weather):
        return ("Currently feels like " + str(round(ftemp, 2)) + "° with " + weather.lower() + ".")
    
    def getTemp(self, temp):
        return ("Temperature: " + str(round(temp, 2)) + "°")
   
    def getHumidity(self, humidity):
        return ("Humidity: " + str(humidity) + "%")

def repeat():
    while True:
        again = input("Do you want to run the program again? (Y/N): ")
        again = again.upper()
    
        if again == "Y":
            return True
        elif again == "N":
            print("Thank you for using the program.")
            return False
        else:
            print("Invalid input, please try again.")
            continue

def main(): 
    ivalue = getInput()
    data = getData(ivalue)
    errorCheck = checkError(data)

    if errorCheck == 1:
        print("Error 404, city not found.")

    elif errorCheck == 2:
        print("Error 400, invalid zip code.")
        
    elif errorCheck == 3:
        values = giveData(data)
        currentCity = define_city(values[0], values[1], values[2], values[3], values[4], values[5])
        
        print("")
        print("===========================")
        print(currentCity.getNames(values[0], values[1]))
        print(currentCity.getConditions(values[3], values[4]))
        print(currentCity.getTemp(values[2]))
        print(currentCity.getHumidity(values[5]))
        print("===========================")
        print("")

while again == True:
    main()
    again = repeat()

