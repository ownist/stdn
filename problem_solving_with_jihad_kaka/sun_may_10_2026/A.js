/**
 * ===================================
 * Write a function to check if a number is even or odd.
 * ===================================
 */
const checkisEvenOrOdd = (num) => {
  if (num % 2 === 0) {
    return `${num} is even`;
  }

  return `${num} is odd`;
};

console.log(checkisEvenOrOdd(56));

console.log("\n");

/**
 * ==============================
 * Find total sum of all numbers in an array.
 * ==============================
 */
function totalSum(arr) {
  let sum = 0;

  for (const n of arr) {
    sum += n;
  }

  return `total sum of numbers are: ${sum}`;
}

console.log(totalSum([1, 2, 3, 4]));
