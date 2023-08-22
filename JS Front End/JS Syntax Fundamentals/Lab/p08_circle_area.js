function area(data) {

    let result;
    if (typeof data === 'number') {
        result = Math.PI * data ** 2
        console.log(result.toFixed(2))
    }

    else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(data)}.`)
    }

    
}

area(5)
area('name')