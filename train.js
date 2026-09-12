// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

function findDoublers(str) {
  let letters = [];

  for (let a = 0; a < str.length; a++) {
    if (letters.includes(str[a])) {
      return true;
    }

    letters.push(str[a]);
  }

  return false;
}

const result = findDoublers("Hello");
console.log("Result: ", result);

// TASK E:

// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getReverse(str) {
//   let result = "";
//   for (let i = str.length - 1; i >= 0; i--) {
//     result += str[i];
//   }
//   return result;
// }
// const result = getReverse("hello");
// console.log("Result: ", result);
