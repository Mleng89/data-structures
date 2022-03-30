/*
HACKER RANK
-----------
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example: 
n = 7
arr = [1,2,1,2,1,3,2]

Output : 2 

*/

//NAIVE SOLUTION // BRUTE FORCE
/*
 */
function sockMerchant(n, arr) {
	//EDGE CASES
	console.time('Comparsion Loop');
	if (arr.length !== n) return 0;
	//SORT ARRAY
	arr.sort((a, b) => a - b);
	let pairs = 0;
	//ITERATE THE ARRAY
	for (let i = 0; i < n; i++) {
		//CHECKING ARRAY FOR PAIRS OF SOCKS
		if (arr[i] === arr[i + 1]) {
			pairs++;
			i++;
		}
	}
	console.timeEnd('Comparsion Loop');
	//RETURN PAIRS
	return pairs;
}
//space o(1) time o(n)

//HASH TABLE -- LOOK UP

function sockMerchantTwo(n, arr) {
	//EDGE CASE
	console.time('HASH');
	if (arr.length !== n) return 0;
	let pairs = 0;
	const sockHash = arr.reduce((a, b) => {
		!a[b] ? (a[b] = 1) : (a[b] += 1);
		return a;
	}, {});

	for (let key in sockHash) {
		pairs += Math.floor(sockHash[key] / 2);
	}
	console.timeEnd('HASH');
	return pairs;
}

// space o(n) time o(n)

// sockMerchant(
// 	100,
// 	[
// 		1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1,
// 		5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4,
// 		1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2,
// 		4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1,
// 		2, 4, 1, 5
// 	]
// );

// sockMerchantTwo(
// 	100,
// 	[
// 		1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1,
// 		5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4,
// 		1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2,
// 		4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1, 2, 4, 1, 5, 1,
// 		2, 4, 1, 5
// 	]
// );

// sockMerchant(2, [1, 1]);
sockMerchantTwo(2, [1, 1]);
module.exports = sockMerchant;
