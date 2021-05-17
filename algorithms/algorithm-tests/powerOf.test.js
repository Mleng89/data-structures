const { expect } = require('@jest/globals');
const powerOfThree = require('../powerOf');

test('powerOfThree should be a function', () => {
	let func = typeof powerOfThree === 'function';
	expect(func).toBe(true);
});

test('powerOfThree should be true', () => {
	expect(powerOfThree(27)).toStrictEqual(true);
});
