"""contains the main logic of the application"""
# pylint: disable=E1101
from datetime import datetime

from flask import Flask, render_template, request, url_for, redirect

from models import db, Blogpost

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)


@app.route('/')
def index():
    """renders homepage"""
    posts = Blogpost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    """renders about page"""
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    """renders post page"""  
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)
    
@app.route('/addpost')
def addpost():
    """renders page to see added posts"""
    return render_template('addpost.html')

@app.route('/add', methods=['POST'])
def add():
    """renders page to add posts"""
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle,
                    author=author, content=content, date_posted=datetime.now())
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
