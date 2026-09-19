// TASK K:

// Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
// MASALAN: countVowels("string") return 1;


function countVowels(str) {
  let lowStr = str.toLowerCase();
  let count = 0;
  for (let char of lowStr) {
    if (
      char === "a" ||
      char === "o" ||
      char === "e" ||
      char === "i" ||
      char === "u"
    ) {
      count++;
    }
  }
  return count;
}

const result = countVowels("string");
console.log(result);

// TASK G:

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

// function getHighestIndex(arr) {
//   let maxIndex = 0;

//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] > arr[maxIndex]) {
//       maxIndex = i;
//     }
//   }
//   return maxIndex;
// }

// const result = getHighestIndex([5, 21, 12, 21, 8]);
// console.log("Result: ", result);

// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function findDoublers(str) {
//   let letters = [];

//   for (let a = 0; a < str.length; a++) {
//     if (letters.includes(str[a])) {
//       return true;
//     }

//     letters.push(str[a]);
//   }

//   return false;
// }

// const result = findDoublers("Hello");
// console.log("Result: ", result);

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
