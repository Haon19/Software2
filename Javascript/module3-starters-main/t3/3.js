'use strict';
const names = ['John', 'Paul', 'Jones'];

for (let name = 0;name < names.length; name++){
  document.querySelector('#target').innerHTML += `<li>${names[name]}</li>`;
}