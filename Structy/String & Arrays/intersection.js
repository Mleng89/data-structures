const intersection = (a, b) => {
	// todo
	let result = [];
	let numSet = new Set();

	for (let i of a) {
		numSet.add(i);
	}
	for (let i of b) {
		if (numSet.has(i)) {
			result.push(i);
		}
	}
	return result;
};

/**
 * TESTS
 */
intersection([4, 2, 1, 6], [3, 6, 9, 2, 10]); // -> [2,6]
intersection([2, 4, 6], [4, 2]); // -> [2,4]
intersection([4, 2, 1], [1, 2, 4, 6]); // -> [1,2,4]
intersection([0, 1, 2], [10, 11]); // -> []
const a = [];
const b = [];
for (let i = 0; i < 50000; i += 1) {
	a.push(i);
	b.push(i);
}
console.log(intersection(a, b)); // -> [0,1,2,3,..., 49999]
