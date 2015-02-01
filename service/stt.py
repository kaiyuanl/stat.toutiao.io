from flask import Flask

app = Flask(__name__)

@app.route('/')
def Stat():
	pass

@app.route('/search')
def Search():
	pass

@app.route('/about')
def About():
	pass

@app.route('/page/<number>')
def Page(number):
	pass