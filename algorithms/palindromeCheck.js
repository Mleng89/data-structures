// function isPal(str) {
// 	return str.split('').reverse().join('') === str;
// }

function isPal(str) {
	let left = 0;
	let right = str.length - 1;
	let newStr = str.toLowerCase();
	while (left !== right) {
		if (newStr[left] !== newStr[right]) {
			return false;
		}
		left++;
		right--;
	}
	return true;
}
console.log(isPal('racecar')); //true
console.log(isPal('summer')); //false

/* 
Time complexity - O(n)
Space complexity- O(1)
*/
