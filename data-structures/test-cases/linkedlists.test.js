const { expect } = require('@jest/globals');
const months = require('../linkedlists');

test('Linked list should be an object', () => {
	expect(typeof months).toBe('object');
});
