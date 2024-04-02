/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves2 = function(nums) {
   
  //[1,2,9,10]
  //find the middle number (if odd length of arr)
  //
  nums = nums.sort((a,b) => a-b);
  let middleNum = nums[Math.floor(nums.length / 2)]
  let totalSum = 0;
  nums.forEach(num => totalSum += Math.abs(num-middleNum));
  return totalSum
};