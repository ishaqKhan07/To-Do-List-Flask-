from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class AssessmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    module_code = StringField('Module Code', validators=[DataRequired(), Length(max=20)])
    deadline = DateField('Deadline', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Submit')
