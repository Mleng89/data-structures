const sockMerchant = require('../Array/sockMerchant');
const { expect } = require('@jest/globals');

test('sockMerchant is a function', () => {
	let func = typeof sockMerchant === 'function';
	expect(func).toBe(true);
});

test('sockMerchant test case 1', () => {
	expect(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])).toStrictEqual(2);
});

test('sockMerchant test case 2', () => {
	expect(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])).toStrictEqual(4);
});
