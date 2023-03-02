from flask import Flask, render_template, request
from post import Post
import smtplib, os

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
RECEIVER = os.environ.get("RECEIVER")

app = Flask(__name__)

@app.route('/')
def home():
    posts = Post().get_posts()
    return render_template("home.html", posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = Post().get_post(id)
    return render_template("post.html", post=post)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    error = False
    sent=False
    if request.method == "POST":
        data = request.form
        sent = True

        # Send email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=RECEIVER,
                    msg=f"Subject:New Message\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
                )
            print("sent")
        except Exception as e:
            print(e)
            error = True


    return render_template("contact.html", sent=sent, error=error)

if __name__ == "__main__":
    app.run(debug=True)


