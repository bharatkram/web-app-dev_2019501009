// function to count the number of occurances of letter in the given word.
function countChar(word, letter) {
    if (letter.length > 1)
        return "only one letter allowed as second argument."

    var count = 0
    for (let i = 0; i < word.length; i++) {
        if (word.charAt(i) == letter) {
            count += 1
        }
    }
    return count
}

// function to count the number of b's in a given string.
function countBs(word) {
    return countChar(word, 'B') + countChar(word, 'b')
}

// defining a string for testing.
const str = "bBBSbB"

// printing the output of the function.
console.log(countBs(str))