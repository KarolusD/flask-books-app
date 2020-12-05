from app import db
from app.books.forms import AddBookForm, UpdateBookForm
from app.books.utils import fill_books_genre
from app.models import Book
from flask import (Blueprint, render_template, url_for, flash, redirect, request)
from flask_login import current_user, login_required

books = Blueprint('books', __name__)


@books.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = AddBookForm()
    fill_books_genre(form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_book = Book(title=form.title.data, author=form.author.data,
                            genre=form.genre.data, user_id=current_user.id)
            db.session.add(new_book)
            db.session.commit()
            flash('Your book has been created!', 'alert__success')
            return redirect(url_for('main.home'))

    return render_template('add_book.html', form=form, title='Add book')


@books.route('/update_book/<id>', methods=['GET', 'PUT'])
@login_required
def update_book(id):
    book_to_update = Book.query.get_or_404(id)
    form = UpdateBookForm()
    fill_books_genre(form)

    if request.method == 'PUT':
        try:
            body = request.get_json()
            if form.validate_on_submit():
                book_to_update.title = body.get('title')
                book_to_update.author = body.get('author')
                book_to_update.genre = body.get('genre')
                db.session.commit()

        except Exception:
            db.session.rollback()
            flash('Something went wrong!', 'alert__warning')
            return redirect(url_for('books.update_book'))

        books_list = Book.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', books_list=books_list)

    if request.method == 'GET':
        try:
            form.title.data = book_to_update.title
            form.author.data = book_to_update.author
            form.genre.data = book_to_update.genre
        except Exception:
            db.session.rollback()
            flash('Something went wrong!', 'alert__warning')
            return redirect(url_for('books.update_book'))

        books_list = Book.query.filter_by(user_id=current_user.id).all()
        return render_template('update_book.html', form=form, title='Edit book', book_to_update=book_to_update)


@books.route('/delete_book/<id>', methods=['DELETE'])
@login_required
def delete_book(id):
    try:
        flash('Something went wrong!', 'alert__warning')
        print('hello form delete', id)
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()

    except Exception:
        db.session.rollback()
        flash('Something went wrong!', 'alert__warning')

    books_list = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', books_list=books_list)
