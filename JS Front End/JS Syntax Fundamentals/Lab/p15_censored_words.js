function solve(text, word) {
    while (text.includes(word)) {
        let lengthWord = word.length
        text = text.replace(word, '*'.repeat(lengthWord))
    }
    console.log(text)
}

solve('A small sentence with some words', 'small')
solve('Find the hidden word', 'hidden')