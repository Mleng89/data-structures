const intToRoman = require('../Integers/intToRoman');
const { expect } = require('@jest/globals');

test('intToRoman should be a function', () => {
	let func = typeof intToRoman === 'function';
	expect(func).toBe(true);
});

test('intToRoman test case 1', () => {
	expect(intToRoman(1231)).toStrictEqual('MCCXXXI');
});

test('intToRoman test case 1', () => {
	expect(intToRoman(4)).toStrictEqual('IV');
});
