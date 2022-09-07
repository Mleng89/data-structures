class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

const a = new Node('A');
const b = new Node('B');
const c = new Node('C');
const d = new Node('D');
const e = new Node('E');

a.next = b;
b.next = c;
c.next = d;
d.next = e;

const printLinkedList = head => {
	let curr = head;
	let output = `[HEAD NODE] `;
	while (curr !== null) {
		output += curr.data + ' -> ';
		curr = curr.next;
	}
	output += ` [TAIL NODE]`;
	console.log(output);
};

printLinkedList(a);
