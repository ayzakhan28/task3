from flask import Flask,render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ayza.db'
db=SQLAlchemy(app)

# Model
class User(db.Model):
    id=db.Column(db.Integer, primary_key =True)
    username=db.Column(db.String(90), unique=True, nullable =False)
    password=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(80), nullable=False)
    role=db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()    



class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    if request.method == 'POST':
        return redirect(url_for('books'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        # TODO: save to DB

        return redirect(url_for('success'))  # ✅ Make sure this line is here

    return render_template('register.html')  # ✅ Also make sure you return the form for GET

@app.route('/success')
def success():
    return render_template('success.html')


from flask import render_template, request, redirect, url_for

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        
        new_book = Book(title=title, author=author, genre=genre)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))

    all_books = Book.query.all()
    return render_template('books.html', books=all_books)



if __name__ == '__main__':
    app.run(debug=True)