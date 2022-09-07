const romanToInt = require('../Integers/romanToInt');
const { expect } = require('@jest/globals');

test('romanToInt is a function', () => {
	let func = typeof romanToInt === 'function';
	expect(func).toBe(true);
});

test('romanToInt test case 1', () => {
	expect(romanToInt('III')).toStrictEqual(3);
});

test('romanToInt test case 2', () => {
	expect(romanToInt('IV')).toStrictEqual(4);
});

test('romanToInt test case 3', () => {
	expect(romanToInt('MCCXXXI')).toStrictEqual(1231);
});
