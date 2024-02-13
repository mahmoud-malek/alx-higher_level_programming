#!/usr/bin/node

// Define the incrementAndCall function
const incrementAndCall = (number, theFunction) => {
  number++;
  theFunction(number);
};

// Export the incrementAndCall function to make it visible from outside
module.exports = { incrementAndCall };
