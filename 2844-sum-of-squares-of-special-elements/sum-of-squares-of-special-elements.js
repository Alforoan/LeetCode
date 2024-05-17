/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfSquares = function(nums) {
    let length = nums.length;
    let sum = 0;
    nums.forEach((num,i) => {
        if(length % (i+1) === 0){
            sum += (num ** 2)
        }
    })
    return sum;
};