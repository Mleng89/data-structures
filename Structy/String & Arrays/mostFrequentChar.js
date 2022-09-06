const mostFrequentChar = s => {
	let frequency = {};
	let char = null;
	for (let i = 0; i < s.length; i++) {
		if (frequency[s[i]]) {
			frequency[s[i]] += 1;
		} else {
			frequency[s[i]] = 1;
		}
	}

	for (let el of s) {
		if (char === null || frequency[el] > frequency[char]) {
			char = el;
		}
	}
	console.log('test--->', frequency);
	// return Object.keys(frequency).reduce((a,b)=>frequency[a] > frequency[b] ? a :b)
	return char;
};
/***
 * TESTS
 */

mostFrequentChar('bookeeper'); // -> 'e'
mostFrequentChar('david'); // -> 'd'
mostFrequentChar('abby'); // -> 'b'
mostFrequentChar('mississippi'); // -> 'i'
mostFrequentChar('potato'); // -> 'o'
mostFrequentChar('eleventennine'); // -> 'e'
mostFrequentChar('riverbed'); // -> 'r'
