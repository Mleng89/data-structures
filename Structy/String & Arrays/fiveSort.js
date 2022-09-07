const fiveSort = nums => {
	let i = 0;
	let j = nums.length - 1;
	while (i < j) {
		if (nums[j] === 5) {
			j -= 1;
		} else if (nums[i] === 5) {
			[nums[i], nums[j]] = [nums[j], nums[i]];
			i += 1;
		} else {
			i += 1;
		}
	}
	return nums;
};

/**
 * TEST
 */
fiveSort([12, 5, 1, 5, 12, 7]);
// -> [12, 7, 1, 12, 5, 5]
fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
fiveSort([5, 5, 5, 1, 1, 1, 4]);
// -> [4, 1, 1, 1, 5, 5, 5]
fiveSort([5, 5, 6, 5, 5, 5, 5]);
// -> [6, 5, 5, 5, 5, 5, 5]
fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
// -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
const fives = new Array(20000).fill(5);
const fours = new Array(20000).fill(4);
const nums = [...fives, ...fours];
fiveSort(nums);
// twenty-thousand 4s followed by twenty-thousand 5s
// -> [4, 4, 4, 4, ..., 5, 5, 5, 5]

/**
 * NOTES
 *
	for(let i = 0; i <nums.length;i++){
	if(nums[i] === 5){
	    let five = nums.splice(i,1)
	    console.log('test-->', five)
	    nums.push(parseInt(five))
	  }
    }
REASON THIS SOLUTION MAY NOT WORK:

INITIAL VALUE FOR NUMS: [5, 5, 5, 1, 1, 1, 4]
LOOPING from i=0 to i < nums.length
nums: [5, 5, 5, 1, 1, 1, 4]
i(0):  ^
updatedNums: [5, 5, 1, 1, 1, 4, 5]
        i(1):     ^
updatedNums: [5, 1, 1, 1, 4, 5, 5]
        i(2):        ^
As you can see, you'll never reach i(0) again and that five won't be captured
*/
