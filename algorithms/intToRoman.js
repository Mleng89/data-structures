const intToRoman = function (num) {
	/** 
I:1
V:5
X:10
L:50
C:100
D:500
M:1000 
**/
	const one = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'];
	const tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'];
	const hund = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'];
	const thous = ['', 'M', 'MM', 'MMM'];

	let result =
		thous[Math.floor(num / 1000)] +
		hund[Math.floor((num % 1000) / 100)] +
		tens[Math.floor((num % 100) / 10)] +
		one[Math.floor((num % 10) / 1)];

	return result;
};

module.exports = intToRoman;
