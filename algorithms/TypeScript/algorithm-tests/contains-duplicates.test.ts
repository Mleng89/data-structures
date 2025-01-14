import { containsDuplicate } from '../Blind75/contains-duplicates';

describe('containsDuplicate', () => {
	test('returns true for an array with duplicates', () => {
		const nums = [1, 2, 3, 1];
		expect(containsDuplicate(nums)).toBe(true);
	});

	test('returns false for an array without duplicates', () => {
		const nums = [1, 2, 3, 4];
		expect(containsDuplicate(nums)).toBe(false);
	});

	test('returns false for an empty array', () => {
		const nums: number[] = [];
		expect(containsDuplicate(nums)).toBe(false);
	});

	test('returns false for a single-element array', () => {
		const nums = [1];
		expect(containsDuplicate(nums)).toBe(false);
	});

	test('returns true for an array with multiple duplicates', () => {
		const nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2];
		expect(containsDuplicate(nums)).toBe(true);
	});

	test('handles negative numbers correctly', () => {
		const nums = [-1, -2, -3, -1];
		expect(containsDuplicate(nums)).toBe(true);
	});

	test('handles a mix of positive and negative numbers', () => {
		const nums = [-1, 1, -2, 2];
		expect(containsDuplicate(nums)).toBe(false);
	});
});
