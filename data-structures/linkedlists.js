class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
	setNextNode(node) {
		if (node instanceof Node || node === null) {
			this.next = node;
		} else {
			throw new Error('Next node must be a number of the Node class.');
		}
	}
	getNextNode() {
		return this.next;
	}
}

class LinkedList {
	constructor() {
		this.head = null;
	}
	addToHead(data) {
		const newHead = new Node(data);
		const currentHead = this.head;
		this.head = newHead;

		if (currentHead) {
			this.head.setNextNode(currentHead);
		}
	}

	addToTail(data) {
		let tail = this.tail;
		if (!tail) {
			this.head = new Node(data);
		} else {
			while (tail.getNextNode() !== null) {
				tail = tail.getNextNode();
			}
			tail.setNextNode(new Node(data));
		}
	}

	removeHead() {
		const removedHead = this.head;
		if (!removedHead) {
			return;
		}
		this.head = removedHead.getNextNode();
		return removedHead.data;
	}

	showList() {
		let currentNode = this.head;
		let output = '[HEAD  NODE]';
		while (currentNode !== null) {
			output += currentNode.data + ' ';
			currentNode = currentNode.getNextNode();
		}
		output += '[TAIL NODE]';
		console.log(output);
	}
}

const months = new LinkedList();
//Linked list is not empty
months.addToTail('December');

// console.log(typeof months);

module.exports = months;
