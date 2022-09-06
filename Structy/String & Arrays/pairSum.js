const pairSum = (numbers, targetSum) => {
	// todo
	if (numbers.length < 2) {
		return 'Not enough numbers to use';
	}
	let pairs = {};
	for (let i = 0; i < numbers.length; i++) {
		const num = numbers[i];
		const complement = targetSum - num;

		// console.log(pairs);
		if (complement in pairs) return [i, pairs[complement]];
		pairs[num] = i;
	}
};
/**
 * TESTS
 */
console.log(pairSum([3, 2, 5, 4, 1], 8)); // -> [0, 2]
console.log(pairSum([4, 7, 9, 2, 5, 1], 5)); // -> [0, 5]
console.log(pairSum([4, 7, 9, 2, 5, 1], 3)); // -> [3, 5]
console.log(pairSum([1, 6, 7, 2], 13)); // -> [1, 2]
console.log(pairSum([9, 9], 18)); // -> [0, 1]
console.log(pairSum([6, 4, 2, 8], 12)); // -> [1, 3]
