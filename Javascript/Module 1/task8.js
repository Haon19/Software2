'use strict';

const startYear = parseInt(prompt("Enter Start Year"));
const endYear = parseInt(prompt("Enter End Year"));

for (let i = startYear; i <= endYear; i++){
  if (i % 4 === 0 && i % 100 !== 0 || i % 400 === 0){
    document.querySelector('#target').innerHTML += `<li>${i}</li>`;
  }
}