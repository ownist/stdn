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
