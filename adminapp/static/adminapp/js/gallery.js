// const cards = document.querySelectorAll('.card');
const container = document.querySelector('.container');
cards.forEach((card) => {
  card.addEventListener('mouseover', (e) => {
    cards.forEach((c) => {
      c.classList.remove('active');
    })
    e.currentTarget.classList.add('active');
  })
})

container.addEventListener('mouseleave', () => {
  cards.forEach((c) => {
    c.classList.remove('active');
  })
})
