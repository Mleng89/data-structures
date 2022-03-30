/*
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
*/

function powerOfThree(n) {
	let i = 1;
	while (i < n) {
		i *= 3;
	}
	return i === n;
}

module.exports = powerOfThree;
