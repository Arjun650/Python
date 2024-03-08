console.log("Hello World")

//this is comment 

function isPrime(num) {
    // Check if the number is less than 2, as prime numbers start from 2
    if (num < 2) {
        return false;
    }
    // Loop through numbers from 2 to the square root of the given number
    for (let i = 2; i <= Math.sqrt(num); i++) {
        // If the number is divisible by any number other than 1 and itself, it's not prime
        if (num % i === 0) {
            return false;
        }
    }
    // If the loop completes without finding any divisors, the number is prime
    return true;
}

// Example usage:
const numberToCheck = 17;
if (isPrime(numberToCheck))
