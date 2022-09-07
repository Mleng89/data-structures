const romanToInt = function (s) {
	let roman = {
		I: 1,
		V: 5,
		X: 10,
		L: 50,
		C: 100,
		D: 500,
		M: 1000
	};
	let total = 0;
	for (let i = 0; i < s.length; i++) {
		let curr = roman[s[i]];
		// console.log('what is curr', curr);
		let next = roman[s[i + 1]];
		// console.log('what is next', next);

		if (next) {
			if (curr >= next) {
				total += curr;
			} else {
				total += next - curr;
				i++;
			}
		} else {
			total += curr;
		}
	}
	return total;
};

module.exports = romanToInt;
