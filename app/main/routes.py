from flask import Blueprint, render_template, flash
from app.models import Book
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def home():
    try:
        books_list = Book.query.filter_by(user_id=current_user.id).all()
        return render_template('index.html', books_list=books_list)
    except Exception:
        flash('Something went wrong!', 'alert__warning')
