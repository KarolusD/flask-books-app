function resetForm(form, alert) {
  form.forEach((input) => {
    input.value = ''
  })

  alert.innerText = ''
}

export default resetForm
