## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

import requests
import json
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/question', methods= ['POST','GET'])
def getting_number():
	j = """<!DOCTYPE html>
	<html>
	<body>
	<form action="http://localhost:5000/result" method="GET">
	Enter your favorite number:<br>
	<input type="text" name="number" value="0">
	<br>
	<input type="submit" value="Submit">
	</form> 
	</body>
	</html>""" 
	return j

@app.route('/result', methods= ['POST','GET'])
def doubling_number():
	if request.method == 'GET':
		result = request.args
		num = result.get('number')
		new_number = 2*(int(num))
		return "Double your favorite number is {}".format(new_number)

# QUESTION 2:

@app.route('/songsearch', methods= ['POST','GET'])
def enter_song():
	jl = """<!DOCTYPE html>
	<html>
	<body>
	<form action="http://localhost:5000/songresults" method="GET">
	Who is your favorite artist?<br>
	<input type="text" name="artist" value="Taylor Swift">
	<br>
	How many song suggestions would you like?<br>
	<input type="radio" name="number" value="1">1<br>
	<input type="radio" name="number" value="2">2<br>
	<input type="radio" name="number" value="3">3<br>
	<input type="radio" name="number" value="4">4<br>
	<input type="radio" name="number" value="5">5<br>
	<input type="submit" value="Submit">
	</form> 
	</body>
	</html>""" 
	return jl

@app.route('/songresults', methods= ['POST','GET'])
def song_results():
	if request.method == 'GET':
		result = request.args
		artist = result['artist']
		num = int(result['number'])
		d = {'term': artist, 'media': 'music', 'format':'json'}
		resp = requests.get('https://itunes.apple.com/search?', params = d)
		d_info = json.loads(resp.text)
		count = 0
		songs_d = {}
		for song in d_info['results']:
			if count >= num:
				break
			elif count < num:
				songs_d[count] = song['trackName']
				count += 1
		if songs_d == {}:
			return "I'm sorry, there are no songs to show for this artist"
		else:
			return render_template("HW2results.html", result=songs_d)



if __name__ == '__main__':
    app.run()


## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application. It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)









