function mathOperations(numOne, numTwo, operator) {
    let result;
    switch(operator) {
        case '+':
            result = numOne + numTwo;
            break;
        case '-':
            result = numOne - numTwo;
            break;
        case '*':
            result = numOne * numTwo;
            break;
        case '/':
            result = numOne / numTwo;
            break;
        case '%':
            result = numOne % numTwo;
            break;
        case '**':
            result = numOne ** numTwo;
            break;
}
    console.log(result)
}

mathOperations(5, 6, '+')
mathOperations(3, 5.5, '*')