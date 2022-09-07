const linkedListValues = require('../linkedListValues');
const { expect } = require('@jest/globals');
class Node {
	constructor(val) {
		this.val = val;
		this.next = null;
	}
}

test('linkedListValues is a function', () => {
	const func = typeof linkedListValues === 'function';
	expect(func).toBe(true);
});

test('linkedListValues test case 1', () => {
	const a = new Node('a');
	const b = new Node('b');
	const c = new Node('c');
	const d = new Node('d');

	a.next = b;
	b.next = c;
	c.next = d;

	// a -> b -> c -> d
	expect(linkedListValues(a)).toStrictEqual(['a', 'b', 'c', 'd']);
});

test('linkedListValues test case 2', () => {
	const x = new Node('x');
	const y = new Node('y');

	x.next = y;

	expect(linkedListValues(x)).toStrictEqual(['x', 'y']);
});

test('linkedListValues test case 3', () => {
	const q = new Node('q');

	expect(linkedListValues(q)).toStrictEqual(['q']);
});

test('linkedListValues test case 4', () => {
	expect(linkedListValues(null)).toStrictEqual([]);
});
