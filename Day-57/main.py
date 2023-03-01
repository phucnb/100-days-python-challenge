from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    posts = Post().get_posts()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = Post().get_post(id)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
