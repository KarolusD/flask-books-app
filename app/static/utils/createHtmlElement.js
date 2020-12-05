/**
 * Create new HTML element
 * @param {string} elementTag
 * @param {string[]} classNames
 * @param {string} content
 * @param {Object} parent
 * @returns {Object}
 */
function createHTMLElement(
  elementTag,
  classNames,
  content = null,
  parent = null
) {
  const element = document.createElement(elementTag)
  classNames.forEach((name) => {
    element.classList.add(name)
  })

  if (content) {
    element.innerText = content
  }

  if (parent) {
    parent.appendChild(element)
    return parent
  }

  return element
}

export default createHTMLElement
