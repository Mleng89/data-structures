// function stringSearch(target, str) {
// 	return str.indexOf(target);
// }

console.log(stringSearch('hi', 'summer')); //-1
console.log(stringSearch('car', 'racecar')); //4

function indexOf(target, str) {
	for (let i = 0; i < str.length; i++) {
		for (let j = 0; j < target.length; j++) {
			if (str[i + j] !== target[j]) {
				break;
			} 
            if(j + 1 ===target.length){
                return i
            }
		}
	}
	return -1;
}
console.log(indexOf('car', 'racecar')); //4
//r a c e c a r     c a r
//0 1 2 3 4 5 6     0 1 2
console.log(indexOf('hi', 'summer')); //-1
