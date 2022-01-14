// Declare the variable
var number = 1011;
var resultNumber = 0;

// Write the function 
function reverseBinary(n) {
    let reverseNumber;

    // Transform the number in a string 
    reverseNumber = n.toString();


    // Split the string to an array 
    reverseNumber = reverseNumber.split("");

    // Reverse the array 
    reverseNumber.reverse();

    // Join the array to create a string
    reverseNumber = reverseNumber.join("");

    // Return the reverse string transformed into a number
    return parseInt(reverseNumber);
};

// Print the result 
resultNumber = reverseBinary(number);

console.log(`Start number: ${number}`);
console.log(`Result number: ${resultNumber}`);