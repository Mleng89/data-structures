/*
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.
*/

function canBeEqual(target, array) {
	const sortTarget = target.sort((a, b) => a - b);
	const sortArray = array.sort((a, b) => a - b);

	for (let i = 0; i < array.length; i++) {
		if (sortTarget[i] === sortArray[i]) {
			continue;
		} else {
			return false;
		}
	}
	return true;
}
module.exports = canBeEqual;
