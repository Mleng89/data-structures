function twoSum(target, array) {
	let i = 0;
	let j = array.length - 1;
	array.sort((a, b) => a - b);
	while (i <= j) {
		let sum = array[i] + array[j];
		if (sum > target) {
			j -= 1;
		} else if (sum < target) {
			i += 1;
		} else {
			return [array[i], array[j]];
		}
	}
	return 'No pairs';
}

module.exports = twoSum;
