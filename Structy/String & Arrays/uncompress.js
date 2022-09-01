const uncompress = s => {
	/*** todo:
  -create new variable to hold return statement
  -loop to check if value at idx is num
    -if num, * by char and concat to string
  -return string
  ***/
	let result = [];
	// let arr = s.split('')
	let pointA = 0;
	let pointB = 0;
	while (pointB < s.length) {
		if (isNaN(s[pointB])) {
			let number = Number(s.slice(pointA, pointB));
			for (let count = 0; count < number; count += 1) {
				result.push(s[pointB]);
			}
			pointB += 1;
			pointA = pointB;
		} else {
			pointB += 1;
		}
	}
	return result.join('');
};

/***
 * Tests:
 */

uncompress('2c3a1t'); // -> 'ccaaat'
uncompress('4s2b'); // -> 'ssssbb'
uncompress('2p1o5p'); // -> 'ppoppppp'
uncompress('3n12e2z'); // -> 'nnneeeeeeeeeeeezz'
uncompress('127y'); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
