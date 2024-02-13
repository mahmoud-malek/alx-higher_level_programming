#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Base case: 0! and 1! are both 1
  } else {
    return n * factorial(n - 1); // Recursive case
  }
}

// Get the integer from the command line argument
const input = parseInt(process.argv[2], 10);

// Call the factorial function and print the result
console.log(factorial(input));
