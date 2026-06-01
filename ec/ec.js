/**
 * =====================
 * monday, june 01
 * =====================
*/
function freqName(names){
  const freqUsers = {};
  
  for(const n of names){
    console.log(n);
  }
}

freqName(['shahed', 'wahid', 'rachem kaka']);

console.log("\n") // create a new empty line for better understanding


function sumOfOddNumsInOneToHundreed(nims){
  let sum = 0;
  
  for(let i = 1; i <= 100; i++){
    if(i % 2 !== 0){
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