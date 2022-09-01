const compress = s => {
	/*** todo
  -create result variable
  -create number of occurance variable
  loop string:
  -previous char variable to check previous
    -numberOfOccurance += 1
    -previous char = s[idx]
    -if curr char === previous char:
      numberOfOccurance += 1
      else:
      -for(let i = 0, i <= numberOfOccurance, i += 1){
         result += prevChar

      }
      -reset numberOfOccurance and move on
  ***/
	let result = '';
	// let numberOfOccurance = 0
	let pointA = 0;
	let pointB = 1;

	let numberOfOccurrence = 1;
	while (pointA < s.length) {
		let currChar = s[pointA];
		let nextChar = s[pointB];
		if (currChar === nextChar) {
			numberOfOccurrence += 1;
			pointB += 1;
		} else {
			if (numberOfOccurrence === 1) {
				result += currChar;
				pointA = pointB;
				pointB += 1;
			} else {
				result += numberOfOccurrence + currChar;
				numberOfOccurrence = 1;
				pointA = pointB;
				pointB += 1;
			}
		}
	}
	return result;
};
// c c a a a t s s s
//     A     B
/***
prevChar = c
numberOfOccurance = 2

***/

/***
 * TESTS
 * */

compress('ccaaatsss'); // -> '2c3at3s'
compress('ssssbbz'); // -> '4s2bz'
compress('ppoppppp'); // -> '2po5p'
compress('nnneeeeeeeeeeeezz'); // -> '3n12e2z'
compress(
	'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
);
// -> '127y'
