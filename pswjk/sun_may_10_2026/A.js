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

console.log("\n"); // ============== create a new empty line ==============

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

console.log("\n"); // ============== create a new empty line ==============

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

console.log("\n"); // ============== create a new empty line ==============

/**
 * ====================================
 * Reverse a string.
 * ====================================
 */
function reverseStr(str) {
  return str.split("").reverse().join("");
}

console.log(reverseStr("ownist"));

console.log("\n"); // ============== create a new empty line ==============

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

console.log("\n"); // ============== create a new empty line ==============

/**
 * ========================
 * Check if a word reads same backward.
 * ========================
 */
function palindromeCheck(str) {
  return str.toLowerCase().split("").reverse().join("") === str.toLowerCase();
}

console.log(palindromeCheck("madam"));

console.log("\n"); // ============== create a new empty line ==============

/**
 * ========================
 * Remove duplicate numbers from array.
 * ========================
 */
function uniqueArray(arr) {
  const unique = [];

  for (const n of arr) {
    if (!unique.includes(n)) {
      unique.push(n);
    }
  }

  return unique;
}

console.log(uniqueArray([1, 2, 2, 3, 3, 4]));

console.log("\n"); // ============== create a new empty line ==============

/**
 * ===========================
 * Count how many even numbers in array.
 * ===========================
 */
function countEvenNumbers(arr) {
  let count = 0;

  for (const n of arr) {
    if (n % 2 === 0) {
      count++;
    }
  }

  return count;
}

console.log(countEvenNumbers([1, 2, 3, 4, 54, 65]));

console.log("\n"); // ============== create a new empty line ==============

/**
 * ==========================
 * Count each character.
 * ==========================
 */
function countEachChar(str) {
  const charCount = {};

  for (const char of str) {
    charCount[char] = (charCount[char] || 0) + 1;
  }

  return charCount;
}

console.log(countEachChar("hello"));


console.log("\n")

function sumOfArr(arr) {
  let totalSum = 0;
  
  for(const n of arr){
    totalSum += n;
  }
  
  return totalSum;
}
console.log(sumOfArr(
  [2,4,5,7,1,5,8,7,5,6,9,3]
))


function stopDuplicate(arr) {
  const uniqueArr = [];
  
  for (const n of arr) {
    if (!uniqueArr.includes(n)) {
      uniqueArr.push(n);
    }
  }
  
  return uniqueArr;
}
console.log(stopDuplicate(
  [
    5, 4, 5, 2, 1, 4, 5, 2, 7, 8, 8, 5, 2, 6
  ]
))


function sumOfEvenNums(){
  let sum = 0;
  
  for(let i = 1; i <= 100; i++){
    if(i % 2 === 0){
      sum += i;
    }
  }
  
  return sum;
}

console.log(sumOfEvenNums());
