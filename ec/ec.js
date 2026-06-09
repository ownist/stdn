/**
 * =====================
 * monday, june 01
 * =====================
 */
function freqName(names) {
  const freqUsers = {};

  for (const n of names) {
    console.log(n);
  }
}

freqName(["shahed", "wahid", "rachem kaka"]);

console.log("\n"); // create a new empty line for better understanding

function sumOfOddNumsInOneToHundreed() {
  let sum = 0;

  for (let i = 1; i <= 50; i++) {
    if (i % 2 !== 0) {
      sum += i;
    }
  }

  return sum;
}

console.log(sumOfOddNumsInOneToHundreed());

/**
 * =====================
 * monday, june 01
 * =====================
 */

console.log("\n"); // create a new empty line for better understanding

/**
 * =====================
 * monday, june 02
 * =====================
 */
function onlyEven(arr) {
  for (const n of arr) {
    if (n % 2 === 0) {
      console.log(n);
    }
  }
}
onlyEven([5, 6, 8, 47, 89]);

function onlyOdd(arr) {
  for (const n of arr) {
    if (n % 2 !== 0) {
      console.log(n);
    }
  }
}
onlyOdd([5, 6, 8, 47, 89]);

console.log("\n"); // create a new empty line for better understanding

function onlyEven() {
  for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
      console.log(i);
    }
  }
}
onlyEven();
/**
 * =====================
 * monday, june 02
 * =====================
 */

/**
 * ====================
 * tuesday, june 09
 * ====================
 */
function loopUsers(users) {
  for (const u of users) {
    console.log(u);
  }
}

loopUsers(["shahed", "ownist", "jihad kaka", "rachel kaka", "tomzid kaka"]);
/**
 * ====================
 * tuesday, june 09
 * ====================
 */
