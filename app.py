from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'some_secret_key'


class MentalHealthForm(FlaskForm):
    question1 = SelectField('How often have you been feeling anxious?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question2 = SelectField('How often have you felt little interest or pleasure in doing things?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question3 = SelectField('How often have you felt nervous or on edge?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question4 = SelectField('How often have you had trouble sleeping or staying asleep?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question5 = SelectField('How often have you felt tired or had little energy?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question6 = SelectField('How often have you felt irritable or easily annoyed?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question7 = SelectField('How often have you felt hopeless about the future?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])
    question8 = SelectField('How often have you felt socially withdrawn?',
                            choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'),
                                     ('3', 'Nearly every day')],
                            validators=[DataRequired()])

    submit = SubmitField('Check my mental health')


def calculate_diagnosis(score):
    if score >= 20:
        return ("Severe", "It seems like you're experiencing significant anxiety, depression, or stress. It's highly recommended to seek professional mental health support.")
    elif 10 <= score < 20:
        return ("Moderate", "You might be experiencing moderate symptoms. Consider talking to a counselor or mental health professional.")
    elif 5 <= score < 10:
        return ("Mild", "Your symptoms appear to be mild, but it's a good idea to practice self-care and monitor your feelings.")
    else:
        return ("Normal", "You seem to be managing well, but it's always important to prioritize mental wellness.")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MentalHealthForm()
    if form.validate_on_submit():
        score = (int(form.question1.data) +
                 int(form.question2.data) +
                 int(form.question3.data) +
                 int(form.question4.data) +
                 int(form.question5.data) +
                 int(form.question6.data) +
                 int(form.question7.data) +
                 int(form.question8.data))

        severity, diagnosis = calculate_diagnosis(score)

        return redirect(url_for('result', diagnosis=diagnosis, severity=severity))

    return render_template('index.html', form=form)


@app.route('/result')
def result():
    diagnosis = request.args.get('diagnosis')
    severity = request.args.get('severity')
    return render_template('result.html', diagnosis=diagnosis, severity=severity)

if __name__ == '__main__':
    app.run(debug=True, port=8000)