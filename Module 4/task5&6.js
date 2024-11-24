'use strict';

const form = document.querySelector('#form');
form.addEventListener('submit', async function (evt) {
  evt.preventDefault();

  const query = document.querySelector('input[name=q]').value;
  const target = document.querySelector('#target');

  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(query)}`);
    const jokes = await response.json();

    // Check if there are jokes and display the first one
    if (jokes.result.length > 0) {
      target.innerHTML = `<p>${jokes.result[0].value}</p>`;
    } else {
      target.innerHTML = '<p>No jokes found for your query.</p>';
    }
  } catch (error) {
    console.log('Error:', error.message);
    target.innerHTML = '<p>Failed to fetch jokes. Please try again later.</p>';
  }
});