const jumpingOnClouds = require('../jumpingOnTheClouds');
const { expect } = require('@jest/globals');

test('jumpingOnClouds should be a function', () => {
	let func = typeof jumpingOnClouds === 'function';
	expect(func).toBe(true);
});

test('jumpingOnClouds test case 1', () => {
	expect(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0])).toStrictEqual(3);
});
