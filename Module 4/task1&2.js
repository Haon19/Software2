'use strict';

// When the form is submitted...
const tvForm = document.querySelector('#tv-shows');
tvForm.addEventListener('submit', async function(evt) {
    document.querySelector('#target').innerHTML = '';
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const query = document.querySelector('input[name=q]').value;
    try {// error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const tvShows = await response.json();

        for (const tvShow of tvShows){
          const html = `<article><h3>${tvShow.show.name}</h3><img src = \"${tvShow.show.image?.medium}\"></article>`
          document.querySelector('#target').innerHTML += html;
        }   // log the result to the console

    }
    catch (error) {
        console.log(error.message);
    }
});