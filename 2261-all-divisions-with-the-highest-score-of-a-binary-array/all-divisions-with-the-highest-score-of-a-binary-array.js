/**
 * @param {number[]} nums
 * @return {number[]}
 */
var maxScoreIndices = function(nums) {
  let scoreArr = [];
  let rightSum = returnNumberOfOnes(nums);
  let leftSum = 0;

  for(let i = 0; i < nums.length + 1; i++){
    let totalSum = 0;
    const prev = nums[i-1];
    if(i === 0){
      leftSum = 0;
      totalSum = leftSum + rightSum;
    }else{
      if(prev === 0){
        leftSum++;
        totalSum = leftSum + rightSum;
      }else{
        rightSum--;
        totalSum = leftSum + rightSum;
      }
    }
    scoreArr.push(totalSum)
  }

  const maxNumber = Math.max(...scoreArr);
  let finalArr = [];
  scoreArr.forEach((num, index) => {
    if(num === maxNumber){
      finalArr.push(index)
    }
  })
  return finalArr;
};

function returnNumberOfOnes(arr) {
  let count = 0;
  arr.forEach((num) => {
    if (num === 1) {
      count++;
    }
  });

  return count;
}