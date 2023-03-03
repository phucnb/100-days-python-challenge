from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# with app.app_context():
#     db.create_all()

class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Update")

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
   
    movies = Movie.query.order_by(Movie.rating.asc()).all()
    return render_template("index.html", movies=movies)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    movie = Movie.query.get(id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        movie.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('home'))
    form.rating.data = movie.rating
    form.review.data = movie.review
    form.img_url.data = movie.img_url
    return render_template("edit.html", movie=movie, form=form)

@app.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        query = form.title.data
        end_point = 'https://api.themoviedb.org/3/search/movie'
        body = {
            # 'api_key' : os.environ.get('TMDA_API_KEY'),
            'api_key' : '11d6c1805ce5db19ff02ca4e7f423b80',
            'query' : query
        }

        response = requests.get(url=end_point, params=body).json()
        print(response)
        results = response['results']
        print(results)
        return render_template('select.html', results=results)
    return render_template('add.html', form=form)

@app.route('/add/id/<int:id>')
def addMovie(id):
    end_point = f'https://api.themoviedb.org/3/movie/{id}'
    body = {
        'api_key' : os.environ.get('TMDA_API_KEY'),
    }

    response = requests.get(url=end_point, params=body).json()
    movie = Movie(
        title = response['original_title'],
        year = int(response['release_date'].split('-')[0]),
        description = response['overview'],
        rating = response['vote_average'],
        ranking = 0,
        review = 'not yet',
        img_url = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
