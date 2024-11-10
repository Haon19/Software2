'use strict';

function even(arr) {
  const evenNumbers = [];
  for (const number of arr){
    if (number % 2 === 0){
      evenNumbers.push(number);
    }
  }
  return evenNumbers;
}

const numbers = [2,7,4,5];
console.log(numbers);
console.log(even(numbers));