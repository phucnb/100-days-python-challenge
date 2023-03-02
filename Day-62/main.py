from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[validators.DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[validators.DataRequired(), validators.URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[validators.DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[validators.DataRequired()])
    coffee = SelectField('Coffee Rating', choices=[('☕️'), ('☕️☕️'), ('☕️☕️☕️'), ('☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️')], validators=[validators.DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=[('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ('💪💪💪💪💪')], validators=[validators.DataRequired()])
    power = SelectField('Power Socket Availability', choices=[('✘'), ('✘✘'), ('✘✘✘'), ('✘✘✘✘'), ('✘✘✘✘✘')], validators=[validators.DataRequired()])
    
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('Day-62/cafe-data.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            print(form.data)
            csv_writer.writerow([form.cafe.data, form.location.data, form.open.data, form.close.data, form.coffee.data, form.wifi.data, form.power.data])
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Day-62/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        cafes = list(csv_data)
        cafes = cafes[1:]
        
    return render_template('cafes.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)
