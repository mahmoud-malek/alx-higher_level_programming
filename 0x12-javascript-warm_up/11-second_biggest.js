#!/usr/bin/node

// Get the arguments excluding the first two which are node and script path
const args = process.argv.slice(2);

// Check if there are no arguments or only one argument
if (args.length < 2) {
  console.log(0);
} else {
  // Convert arguments to integers and sort them in ascending order
  const sortedArgs = args.map(Number).sort((a, b) => a - b);

  // Remove duplicates
  const uniqueArgs = Array.from(new Set(sortedArgs));

  // If there are only duplicates, print the largest value
  if (uniqueArgs.length === 1) {
    console.log(uniqueArgs[0]);
  } else {
    // Otherwise, print the second largest value
    console.log(uniqueArgs[uniqueArgs.length - 2]);
  }
}
