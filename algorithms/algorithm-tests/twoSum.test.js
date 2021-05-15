const { expect } = require('@jest/globals');
const twoSum = require('../twoSum');

test('twoSum should be a function', () => {
	let func = typeof twoSum === 'function';
	expect(func).toBe(true);
});
