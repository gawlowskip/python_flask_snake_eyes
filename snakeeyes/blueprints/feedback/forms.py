from flask_wtf import Form
from wtforms import TextAreaField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class FeedbackForm(Form):
    email = EmailField("What's your e-mail address?", [DataRequired(), Length(3, 254)])
    message = TextAreaField("Your feedback", [DataRequired(), Length(1, 8192)])
