import sys
sys.path.append('..')
from flask import Flask, render_template
from infra.data import toutiao
from infra.items import Post
from forms import SearchForm

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['GET', 'POST'])
def Search():
    form = SearchForm(csrf_enabled=False)
    if form.validate_on_submit():
        keyword = form.search_content.data.encode('utf-8')
        result = toutiao.search(keyword)
        return render_template('Items.html', form = form, posts = result)

    return render_template('Main.html', form = form)

@app.route('/about')
def About():
    return 'about'


if __name__ == '__main__':
    app.run(debug = True)
