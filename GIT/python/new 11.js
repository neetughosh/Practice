const numbers = [2, 4, 6, 8, 9, 15, 16, 64];

// Expected result: [4, 16, 64]

// Sorting numbers ascending.
numbers.sort((n1, n2) => n1 > n2);

const lastNbr = numbers[numbers.length - 1];

const res = [];
let number = numbers[0];
while (number <= lastNbr) {
  if (numbers.indexOf(number) !==-1) {
    res.push(Math.pow(number, 2));
  }
  number *= 2;
}

console.log(res);