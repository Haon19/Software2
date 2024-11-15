'use strict';

function addElement(element,addClass) {

  const newLi = document.createElement("li");

  const newContent = document.createTextNode(element);

  newLi.appendChild(newContent);

  newLi.className = addClass;

  const currentDiv = document.getElementById("target");

  document.body.insertBefore(newLi, currentDiv);
}

addElement('First item', null);
addElement('Second item','my-item');
addElement('Third item', null);