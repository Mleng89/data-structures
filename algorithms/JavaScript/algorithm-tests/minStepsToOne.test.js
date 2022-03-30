const minStepsToOne = require('../minStepsToOne');
const minStepsToOneM = require('../minStepsToOne');
const minStepsToOneT = require('../minStepsToOne');
const { expect } = require('@jest/globals');

test('minStepsToOne should be a function', () => {
	const func = typeof minStepsToOne === 'function';
	expect(func).toBe(true);
});
test('minStepsToOneM should be a function', () => {
	const func = typeof minStepsToOneM === 'function';
	expect(func).toBe(true);
});
test('minStepsToOneT should be a function', () => {
	const func = typeof minStepsToOneT === 'function';
	expect(func).toBe(true);
});

test('minStepsToOne test case 1', () => {
	const num = 14;
	expect(minStepsToOne(num)).toStrictEqual(4);
});

test('minStepsToOneM test case 1', () => {
	const num = 100;
	expect(minStepsToOne(num)).toStrictEqual(7);
});

test('minStepsToOneT test case 1', () => {
	const num = 1000;
	expect(minStepsToOne(num)).toStrictEqual(9);
});
