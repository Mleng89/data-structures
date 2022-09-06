const pairProduct = (numbers, targetProduct) => {
	// todo
	let pairs = {};
	for (let i = 0; i < numbers.length; i++) {
		const num = numbers[i];
		const complement = targetProduct / num;
		if (complement in pairs) {
			return [i, pairs[complement]];
		}
		pairs[num] = i;
	}
};

/**
 * TEST
 */
pairProduct([3, 2, 5, 4, 1], 8); // -> [1, 3]
pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
pairProduct([4, 7, 9, 2, 5, 1], 5); // -> [4, 5]
pairProduct([4, 7, 9, 2, 5, 1], 35); // -> [1, 4]
pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
pairProduct([4, 6, 8, 2], 16); // -> [2, 3]
