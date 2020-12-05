async function deleteBook(id) {
  try {
    const url = '/delete_book/'
    console.log('deleting a book!', id)
    await fetch(url + id, {
      method: 'DELETE',
    })

    const book = document.querySelector(`[data-id="${id}"]`)
    book.style.opacity = 0

    setTimeout(() => {
      book.remove()
    }, 400)
  } catch (error) {
    console.error(error)
  }
}

const updateBook = async (event, id) => {
  event.preventDefault()
  console.log(event, id)
  try {
    const url = '/update_book/'

    const csrf = document.getElementById('csrf_token')
    const title = document.querySelector('#title input')
    const author = document.querySelector('#author input')
    const genre = document.querySelector('#genre select')

    const newBook = {
      csrf_token: csrf.value,
      title: title.value,
      author: author.value,
      genre: genre.value,
    }

    const response = await fetch(url + id, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      redirect: 'follow',
      body: JSON.stringify(newBook),
    })
    window.location.href = '/'
  } catch (error) {
    console.error(error)
  }
}

const getBooks = async () => {
  try {
    await fetch('/', {
      method: 'GET',
      headers: {
        'Content-Type': 'text/html',
      },
    })
  } catch (error) {
    console.error(error)
  }
}
