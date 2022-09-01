const anagrams = (s1, s2) => {
	// todo
	console.log('my params', s1, s2);
	let sortedA = s1.split('').sort((a, b) => a.localeCompare(b));
	console.log('sortedA--->', sortedA);
	let sortedB = s2.split('').sort((a, b) => a.localeCompare(b));

	console.log('sortedB--->', sortedB);

	return sortedA.join('') === sortedB.join('');
};

module.exports = {
	anagrams
};

console.log(anagrams('restful', 'fluster'));

/***
 * TESTS
 */
anagrams('restful', 'fluster'); // -> true
anagrams('cats', 'tocs'); // -> false
anagrams('monkeyswrite', 'newyorktimes'); // -> true
anagrams('paper', 'reapa'); // -> false
anagrams('elbow', 'below'); // -> true
anagrams('tax', 'taxi'); // -> false
anagrams('taxi', 'tax'); // -> false
anagrams('night', 'thing'); // -> true
anagrams('abbc', 'aabc'); // -> false
anagrams('po', 'popp'); // -> false
anagrams('pp', 'oo'); // -> false
