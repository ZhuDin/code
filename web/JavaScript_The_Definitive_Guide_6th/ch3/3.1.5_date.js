let then = new Date(2022, 2, 2);
let later = new Date(2022, 2, 12, 12, 12, 15);
let now = new Date();
let elapsed = now - then;
console.log(later.getFullYear());
console.info(later.getMonth());
console.info(later.getDate());
console.info(later.getDay());
console.info(later.getHours());
console.info(later.getUTCHours());
console.info(elapsed);