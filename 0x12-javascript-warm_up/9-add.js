#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Get the integers from command line arguments
const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

// Call the add function and print the result
console.log(add(num1, num2));
