/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let tempLowest = Infinity;
    let diff = tempLowest - target;
    for(let i = 0; i < nums.length; i++){
        const first = nums[i];
        for(let j = i + 1; j < nums.length; j++){
            const second = nums[j];
            for(let k = j + 1; k < nums.length; k++){
                const third = nums[k];
                totalSum = first + second + third;
                let tempDiff = Math.abs(totalSum - target);
                if(Math.abs(totalSum - target) < diff){
                    diff = tempDiff;
                    tempLowest = totalSum;
                }
            }
        }
    }
    return tempLowest;
};