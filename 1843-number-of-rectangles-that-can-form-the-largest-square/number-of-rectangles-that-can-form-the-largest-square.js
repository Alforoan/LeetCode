/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    // #as you iterate through the array, find a lower value
    //     #append that lower value to the list
    //     #find the maximum value from the list
    //     #iterate through the list that contains the lower values and increase the counter
    //     #every time the element is equal to the maximum value
    const lowerValues = [];
    for(let i = 0; i < rectangles.length; i++){
        const len = rectangles[i][0];
        const wid =  rectangles[i][1];
        const lowerValue = Math.min(len, wid);
        lowerValues.push(lowerValue);
    }
    const maxValue = Math.max(...lowerValues);
    let counter = 0;
    lowerValues.forEach(value => {
        if(value === maxValue){
            counter++;
        }
    })
    return counter;
};