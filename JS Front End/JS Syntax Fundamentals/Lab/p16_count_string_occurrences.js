function solve(text, searchedWord) {
    let words = text.split(' ');
    let wordOccur = 0;
    for (let word of words) {
        if (word === searchedWord ){
            wordOccur += 1
        }
        
    }
    console.log(wordOccur)
}

solve('softuni is great place for learning new programming languages','softuni')
solve('This is a word and it also is a sentence','is')