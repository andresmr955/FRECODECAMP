const character = "#";
const count = 8;
const rows = [];

console.log("-".repeat(100))
console.log("THIS IS THE FIRST LOOP")

for (let i =  0; i < 10; i++) {
    // console.log(`With js:, ${i}`)
    rows.push(character.repeat(i))
    console.log(rows)
}


console.log("-".repeat(100))
console.log("THIS IS THE SECOND LOOP")

let result = ""

for ( const row of rows){
    console.log(row)
    console.log(typeof(row))
    result = result + row + "\n";
}

console.log("-".repeat(100))
console.log("THIS IS THE RESULT")

console.log(result)
console.log(typeof(result))
