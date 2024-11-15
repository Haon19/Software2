'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];


let select = document.getElementById("target");
for (let i in students){
  const opt = document.createElement('option');
  opt.value = students[i].id;
    opt.innerHTML = students[i].name;
    select.appendChild(opt);
}
