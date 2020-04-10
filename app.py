from flask import Flask, render_template, url_for, request
import testJikan

app = Flask(
  __name__,
  static_folder='static',
  template_folder ='templates'
)

sunday = testJikan.animeSchedule('sunday')
monday = testJikan.animeSchedule('monday')
tuesday = testJikan.animeSchedule('tuesday')
wednesday = testJikan.animeSchedule('wednesday')
thursday = testJikan.animeSchedule('thursday')
friday = testJikan.animeSchedule('friday')
saturday = testJikan.animeSchedule('saturday')


@app.route('/home', methods=['POST','GET'])
@app.route('/', methods=['POST','GET'])
def homePage():
    return render_template( 'index.html') 

@app.route('/search', methods=['POST','GET'])
def searchPage():
    return render_template( 'search.html') 



@app.route('/schedule')
def testing2():
  return render_template(
    'schedule.html', monday = monday, tuesday = tuesday, wednesday = wednesday, 
    thursday = thursday, friday = friday, saturday = saturday, sunday = sunday
  )


@app.route('/<errors>')
def errorPage(errors):
	#return (errors + ' not found')
    return render_template('errors.html',errors = errors)   

if __name__ == '__main__':
    # app.debug = True
    # app.run()
    # either above or the below code can be used to change debug mode
    app.run(debug = True)
