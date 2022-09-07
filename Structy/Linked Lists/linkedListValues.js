// class Node {
// 	constructor(val) {
// 		this.val = val;
// 		this.next = null;
// 	}
// }

const linkedListValues = head => {
	let output = [];
	let currVal = head;
	while (currVal) {
		output.push(currVal.val);
		currVal = currVal.next;
	}
	return output;
};
module.exports = linkedListValues;
