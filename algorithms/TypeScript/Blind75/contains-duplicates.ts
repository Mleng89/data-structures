export const containsDuplicate = (nums: number[]): boolean => {
	const numMap: Record<number, boolean> = [];

	for (const num of nums) {
		if (numMap[num]) {
			return true;
		}
		numMap[num] = true;
	}
	return false;
};

/***
 * NOTE:
 * Would a set be more optimized?
 */
