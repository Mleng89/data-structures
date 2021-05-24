const fibonacci = require('../fibonacci');
const fibonacciMemo = require('../fibonacci');
const { expect } = require('@jest/globals');

test('fibonacci & fibonacciMemo are functions', () => {
	let func =
		typeof fibonacci === 'function' && typeof fibonacciMemo === 'function';
	expect(func).toBe(true);
});

test('fibonacci test case 1', () => {
	expect(fibonacci(2)).toStrictEqual(1);
});

test('fibonacci test case 2', () => {
	expect(fibonacci(4)).toStrictEqual(3);
});

test('fibonacci test case 2', () => {
	expect(fibonacci(10)).toStrictEqual(55);
});

//FIBONACCI MEMO
test('fibonacciMemo test case 1', () => {
	expect(fibonacciMemo(30)).toStrictEqual(832040);
});
//GOING FROM 50+ SLOWS THE MEMO
//DO A TABULATION SOLUTION
