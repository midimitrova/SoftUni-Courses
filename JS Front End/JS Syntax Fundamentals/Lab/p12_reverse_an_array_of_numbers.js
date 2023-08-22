function solve(n, arr) {
    let newArr = []
    for (let i=0; i<n; i++) {
        newArr.push(arr[i])
    }
    console.log((newArr.reverse().join(' ')))
}

solve(3, [10, 20, 30, 40, 50])
solve(4, [-1, 20, 99, 5])
solve(2, [66, 43, 75, 89, 47])