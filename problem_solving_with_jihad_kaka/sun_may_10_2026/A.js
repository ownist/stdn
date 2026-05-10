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

console.log("\n");

/**
 * ===============================
 * Find the biggest number in an array.
 * ==============================
 */
function largestNumber(arr) {
  let largestNum = arr[0];

  for (const n of arr) {
    if (n > largestNum) {
      largestNum = n;
    }
  }

  return `${largestNum} is the largest numebr in the ${arr}`;
}

console.log(largestNumber([4, 7, 2, 9, 1]));

console.log("\n");

/**
 * ====================================
 * Reverse a string.
 * ====================================
 */
function reverseStr(str) {
  return str.split("").reverse().join("");
}

console.log(reverseStr("ownist"));

console.log("\n");

/**
 * =========================
 * Count vowels in a string.
 * =========================
 */
function countVowels(str) {
  let count = 0;

  for (const char of str) {
    const charLower = char.toLowerCase();
    if (
      charLower === "a" ||
      charLower === "e" ||
      charLower === "i" ||
      charLower === "o" ||
      charLower === "u"
    ) {
      count++;
    }
  }

  return `"${str}" er moddhe ${count} ta vowels ache`;
}

console.log(countVowels("shahed and ownist"));
