from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class SearchForm(Form):
    search_content = TextField('search', validators = [Required()])
