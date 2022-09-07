const { expect } = require('@jest/globals');
const twoSum = require('../Integers/twoSum');

test('twoSum should be a function', () => {
	let func = typeof twoSum === 'function';
	expect(func).toBe(true);
});

test('twoSum function', () => {
	let test = [1, 5, 7, 3, 9, 5];
	const expected = [1, 5];
	expect(twoSum(6, test)).toStrictEqual(expected);
});
