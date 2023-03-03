from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.models import Book
from app.book.forms import BookForm, EditBookForm

book = Blueprint('book', __name__)

@book.route('/')
@login_required
def index():
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', books=books)

@book.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully.', 'success')
        return redirect(url_for('book.index'))
    return render_template('add_book.html', form=form, title='Add Book')

@book.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.user_id != current_user.id:
        flash('You are not authorized to edit this book.', 'danger')
        return redirect(url_for('book.index'))
    form = EditBookForm()
    if form.validate_on_submit():
        book.rating = form.rating.data
        db.session.commit()
        flash('Book updated successfully.', 'success')
        return redirect(url_for('book.index'))
    return render_template('edit_book.html', form=form, title='Edit Book')

@book.route('/book/<int:book_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.user_id != current_user.id:
        flash('You are not authorized to delete this book.', 'danger')
        return redirect(url_for('book.index'))
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully.', 'success')
    return redirect(url_for('book.index'))