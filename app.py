from flask import Flask, render_template, url_for
from jikanpy import Jikan

obj = Jikan()

app = Flask(__name__)

schedules = obj.schedule()

Details= []
# genre = []
type(Details)

# Uncomment this for genre
# for i in range(0,len(schedules['friday'])):  
#   for j in range(0, len(schedules['friday'][i]['genres'])):
#     genre.append(schedules['friday'][i]['genres'][j]['name'])

#day = input('Schedule of which day : ')

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

print(Details)

# posts should be of this form [{},{}]

#print(Details)

@app.route('/home')
@app.route('/')
def homePage():
    return render_template('index.html', monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday) 
    # here posts is user defined variable that is used in index html to iterate over the data in 'someData'

@app.route('/projects')
def projectPage():
   return render_template('projects.html', monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
#title = 'Projects',


@app.route('/test')
def testing():
   return render_template('test.html', monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
#title = 'Projects',

@app.route('/test2')
def testing2():
   return render_template('test2.html', monday = monday, tuesday = tuesday, wednesday = wednesday, thursday = thursday, friday = friday, saturday = saturday, sunday = sunday)
#title = 'Projects',



@app.route('/<errors>')
def errorPage(errors):
	#return (errors + ' not found')
    return render_template('errors.html')   

if __name__ == '__main__':
    # app.debug = True
    # app.run()
    # either above or the below code can be used to change debug mode
    app.run(debug = True)
