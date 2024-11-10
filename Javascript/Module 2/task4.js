'use strict';
let number = parseInt(prompt("Enter a number, enter 0 to stop"));

array = [number]

while(number !== 0){
  number = parseInt(prompt("Enter a number, enter 0 to stop"))
  array.push(number)
}

array.sort()

array.reverse()

console.log(array)