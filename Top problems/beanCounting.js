// function to count the number of b's in a given string.
function countBs(word) {
    var count = 0
    for (let i = 0; i < word.length; i++) {
        if (word.charAt(i) === 'b' || word.charAt(i) === 'B') {
            count += 1
        }
    }
    return count
}

const str = "bBBSbB"

console.log(countBs(str))