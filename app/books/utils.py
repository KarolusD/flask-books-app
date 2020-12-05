def read_file(filename):
    with open(filename) as file:
        return [line.strip() for line in file]


def fill_books_genre(form):
    books_genre = read_file('app/static/booksGenre.txt')
    form.genre.choices = [('', 'Please select an option')]
    form.genre.choices += [(genre, genre) for genre in books_genre]
