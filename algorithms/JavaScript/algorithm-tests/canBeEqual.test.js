const canBeEqual = require('../Array/canBeEqual');
const { expect } = require('@jest/globals');

test('canBeEqual is a function', () => {
	const func = typeof canBeEqual === 'function';
	expect(func).toBe(true);
});

test('canBeEqual test case 1', () => {
	let tar = [1, 2, 3, 4];
	let arr = [2, 4, 1, 3];
	expect(canBeEqual(tar, arr)).toStrictEqual(true);
});

test('canBeEqual test case 2', () => {
	let tar = [3, 7, 9];
	let arr = [3, 11, 7];
	expect(canBeEqual(tar, arr)).toStrictEqual(false);
});
