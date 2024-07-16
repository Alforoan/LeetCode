/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let result = ""
     let table = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40:"XL",
        50:"L",
        90:"XC",
        100:"C",
        400:"CD",
        500:"D",
        900:"CM",
        1000:"M"
    }
    while(num >= 1000){
        result += table[1000]
        num -= 1000
}
    while(num >= 900){
        result += table[900]
        num -= 900
}
    while(num >= 500){
        result += table[500]
        num -= 500
}
    while(num >= 400){
        result += table[400]
        num -= 400
}
    while(num >= 100){
        result += table[100]
        num -= 100
}
    while(num >= 90){
        result += table[90]
        num -= 90
}
    while(num >= 50){
        result += table[50]
        num -= 50
}
    while(num >= 40){
        result += table[40]
        num -= 40
}
    while(num >= 10){
        result += table[10]
        num -= 10
}
    while(num >= 9){
        result += table[9]
        num -= 9
}
    while(num >= 5){
        result += table[5]
        num -= 5
}
    while(num >= 4){
        result += table[4]
        num -= 4
}
    while(num > 0){
        result += table[1]
        num -= 1
}
    return result
}
