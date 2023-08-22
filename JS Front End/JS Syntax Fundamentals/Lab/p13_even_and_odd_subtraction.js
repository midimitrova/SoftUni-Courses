function solve(arr) {
    let evenArr = [];
    let evenSum = 0;
    let oddArr = [];
    let oddSum = 0;
    for(let i=0; i<=arr.length - 1; i++){
        if (arr[i] % 2 === 0){
             evenArr.push(arr[i])
             evenSum += arr[i]
        }
        else{
            oddArr.push(arr[i])
            oddSum += arr[i]
        }
           
    }

   
    console.log(evenSum - oddSum)
    
}       

solve([1,2,3,4,5,6])
solve([3,5,7,9])
solve([2,4,6,8,10])