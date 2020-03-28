
from flask import Flask, render_template, url_for
from jikanpy import Jikan

obj = Jikan()

app = Flask(__name__)

schedules = obj.schedule()


# using function to get day details

def animeSchedule(day):
  tempDay = []
  for i in range(0,len(schedules[day])):
    Detail = {
      'image_url' : schedules[day][i]['image_url'],
      'title' : schedules[day][i]['title'],
      'MAL_Url': schedules[day][i]['url'],
      'synopsis': schedules[day][i]['synopsis'],
      # 'genre': genre
      }
    tempDay.append(Detail)
  return tempDay


# Uncomment this for genre
# for i in range(0,len(schedules['friday'])):  
#   for j in range(0, len(schedules['friday'][i]['genres'])):
#     genre.append(schedules['friday'][i]['genres'][j]['name'])

#day = input('Schedule of which day : ')

# Using loops to get day details

Details= []
# genre = []
type(Details)

days =['sunday','monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
sunday = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []


for day in days:
  for i in range(0,len(schedules[day])):
    if day == 'monday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      monday.append(Detail)
    if day == 'tuesday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      tuesday.append(Detail)
    if day == 'wednesday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      wednesday.append(Detail)
    if day == 'thursday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      thursday.append(Detail)
    if day == 'friday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      friday.append(Detail)
    if day == 'saturday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      saturday.append(Detail)
    if day == 'sunday':
      Detail = {
        'image_url' : schedules[day][i]['image_url'],
        'title' : schedules[day][i]['title'],
        'MAL_Url': schedules[day][i]['url'],
        'synopsis': schedules[day][i]['synopsis'],
        # 'genre': genre
        }
      sunday.append(Detail)

