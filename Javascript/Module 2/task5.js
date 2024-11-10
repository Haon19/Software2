'use strict';


let number = parseInt(prompt("Enter a number"))
let x = true
let set = new Set([number])

while (x === true){
  number = parseInt(prompt("Enter a number"))
  if (set.has(number)){
    x = false
  }
  set.add(number)


}
const sorted = Array.from(set).sort((a, b) => a - b)

console.log(sorted)