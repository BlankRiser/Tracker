from flask import Flask, render_template, url_for
from jikanpy import Jikan

obj = Jikan()

app = Flask(__name__)

schedules = obj.schedule()
  
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

sunday = animeSchedule('sunday')
monday = animeSchedule('monday')
tuesday = animeSchedule('tuesday')
wednesday = animeSchedule('wednesday')
thursday = animeSchedule('thursday')
friday = animeSchedule('friday')
saturday = animeSchedule('saturday')

# posts should be of this form [{},{}]

#print(Details)

@app.route('/home')
@app.route('/')
def homePage():
    return render_template('index.html') 
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
