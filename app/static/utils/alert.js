window.addEventListener('DOMContentLoaded', () => {
  const alert = document.querySelector('.alert')
  if (alert) {
    alert.style.display = null
    setTimeout(() => {
      alert.style.opacity = 0
    }, 3000)

    setTimeout(() => {
      alert.remove()
    }, 3350)
  }
})
