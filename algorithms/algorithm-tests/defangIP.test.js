const defangIP = require('../defangIP');
const { expect } = require('@jest/globals');

test('defangIP should be a function', () => {
	const func = typeof defangIP === 'function';
	expect(func).toBe(true);
});

test('defangIP test case 1', () => {
	const ip = '1.1.1.1';
	expect(defangIP(ip)).toStrictEqual('1[.]1[.]1[.]1');
});

test('defangIP test case 2', () => {
	const ip = '255.100.50.0';
	expect(defangIP(ip)).toStrictEqual('255[.]100[.]50[.]0');
});
