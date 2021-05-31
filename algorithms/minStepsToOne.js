/*
Write a function that returns the minimum steps
you can take from n to 1

If n can divide by 2, divide by 2
If n can divide by 3, divide by 3
Or else, subtract by 1

5-> 4-> 2-> 1 /// n = 5 output =3

n = 10 output 3
10-> 5-> 4-> 2-> 1 return: 4
10-> 9-> 3-> 1 return: 3
*/

/*
Recursion
*/
function minStepsToOne(n) {
	if (n === 0) return 0;
	//subtract 1
	let steps = minStepsToOne(n - 1);
	//divide 2
	if (n % 2 === 0) {
		let div2 = minStepsToOne(n / 2);
		steps = Math.min(steps, div2);
	}
	//divide 3
	if (n % 3 === 0) {
		let div3 = minStepsToOne(n / 3);
		steps = Math.min(steps, div3);
	}
	return steps + 1;
}
console.time('RECURSION');
console.log(minStepsToOne(14));
console.timeEnd('RECURSION');
/*
Memoization
*/
let memo = {};
function minStepsToOneM(n) {
	if (n in memo) {
		return memo[n];
	}
	if (n === 1) return 0;
	//subtract 1
	let steps = minStepsToOneM(n - 1);
	//divide 3
	if (n % 3 === 0) {
		let div3 = minStepsToOneM(n / 3);
		steps = Math.min(steps, div3);
	}
	//divide 2
	if (n % 2 === 0) {
		let div2 = minStepsToOneM(n / 2);
		steps = Math.min(steps, div2);
	}

	memo[n] = steps + 1;
	// console.log('what is in my memo', memo);
	return memo[n];
}
console.time('MEMOIZATION');
console.log(minStepsToOneM(100));
console.timeEnd('MEMOIZATION');

/*
TABULATION
*/

function minStepsToOneT(n) {
	let result = new Array(n + 1);

	//BASE CASE SIMILAR TO IF N === 1 RETURN 0
	result[1] = 0;
	for (let i = 2; i < result.length; i++) {
		//subtract 1
		let steps = result[i - 1];

		//divide 2
		if (i % 2 === 0) {
			let div2 = result[i / 2];
			steps = Math.min(steps, div2);
		}
		if (i % 3 === 0) {
			let div3 = result[i / 3];
			steps = Math.min(steps, div3);
		}
		result[i] = steps + 1;
	}
	// console.log(result);
	return result[n];
}
console.time('TABULATION');
console.log(minStepsToOneT(100));
console.timeEnd('TABULATION');

module.exports = minStepsToOne;
module.exports = minStepsToOneM;
module.exports = minStepsToOneT;
