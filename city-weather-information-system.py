cities = [
    {'name': 'Delhi', 'temperature': 42, 'population': 19000000},
    {'name': 'Mumbai', 'temperature': 34, 'population': 20000000},
    {'name': 'Jaipur', 'temperature': 39, 'population': 4000000},
    {'name': 'Shillong', 'temperature': 22, 'population': 500000},
    {'name': 'Kolkata', 'temperature': 33, 'population': 14900000}
]

def title():
  print('CITY WEATHER INFORMATION SYSTEM')
  print('--------------------------------')
def show_all_cities():
  print('All cities:')
  for city in cities:
    print(city['name'])
def search_city(city_name):
  for city in cities:
    if city['name'] == city_name:
      print('City found:', city['name'])
      print('Temperature:', city['temperature'])
      print('Population:', city['population'])
def show_hottest_city():
  hottest_city = cities[0]
  for city in cities:
    if city['temperature'] > hottest_city['temperature']:
      hottest_city = city
  print('city:', hottest_city['name'])
  print('temperature :',hottest_city['temperature'],'°C')
def temp_greater_than(temp):
  print('Cities with temperature greater than', temp, 'degrees:')
  for city in cities:
    if city['temperature'] > temp:
      print(city['name'])
def total_population():
  total = 0
  for city in cities:
    total += city['population']
  print('Total population:', total)
def highest_population():
  highest = cities[0]
  for city in cities:
    if city['population'] > highest['population']:
      highest = city
  print('Highest population city:')
  print(highest['name'])



def average_population():
  total = 0
  for city in cities:
    total += city['population']
  average = total / len(cities)
  print('Average population:', round(average, 2))
title()
print()
show_all_cities()
print()
search_city('Jaipur')
print()
show_hottest_city()
print()
temp_greater_than(35)
print()
highest_population()
print()
total_population()
print()
average_population()
print()    now i know how to make it look professional i want to edit if there is anything you can and lets just add this oj github now
