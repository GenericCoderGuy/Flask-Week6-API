from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonGift(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    description = StringField('Description', validators = [DataRequired()])
    type = StringField('Type', validators = [DataRequired()])
    submit_button = SubmitField('Gift Pokemon!')

class PokemonCapture(FlaskForm):
    capture = StringField('Capture', validators = [DataRequired()])
    submit_button = SubmitField('Capture!')