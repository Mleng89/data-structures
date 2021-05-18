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
function sockMerchant(n, arr) {
	//EDGE CASES
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
	//RETURN PAIRS
	return pairs;
}
*/

//HASH TABLE -- LOOK UP
function sockMerchant(n, arr) {
	//EDGE CASE
	if (arr.length !== n) return 0;
	let pairs = 0;
	const sockHash = arr.reduce((a, b) => {
		!a[b] ? (a[b] = 1) : (a[b] += 1);
		return a;
	}, {});

	for (let key in sockHash) {
		pairs += Math.floor(sockHash[key] / 2);
	}
	return pairs;
}

module.exports = sockMerchant;
