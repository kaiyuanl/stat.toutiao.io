from flask import Flask, render_template
from sttdata import toutiao
from sttform import SearchForm

app = Flask(__name__)

@app.route('/')
def Stat():
	return render_template('stt.html')

@app.route('/search', methods = ['GET', 'POST'])
def Search():
	form = SearchForm()
	if form.validate_on_submit():
		keyword = str(form.search_content.data).encode('utf-8')
		result = toutiao.search(keyword)
		return render_template('stt.html', form = form, posts = result)

	

@app.route('/about')
def About():
	return 'about'

@app.route('/page/<number>')
def Page(number):
	return 'page'

@app.route('/all')
def  All():
	return render_template('stt.html', posts = toutiao.list_post())

app.run(debug=True)