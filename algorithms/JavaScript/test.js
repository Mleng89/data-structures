const obj = {
	NSG: {
		name: 'NNSSP',
		position: 3
	},
	CAB: {
		name: 'CBSSP',
		position: 2
	},
	EQU: {
		name: 'SSP',
		position: 3
	}
};

const sortByName = obj => {
	const entries = Object.entries(obj);
	const response = {};
	entries.sort((a, b) => {
		if (a[1]['name'] < b[1]['name']) {
			return -1;
		} else if (a[1]['name'] > b[1]['name']) {
			return 1;
		}
		return 0;
	});
	for (let i = 0; i < entries.length; i++) {
		const key = entries[i][0];
		response[key] = entries[i][1];
	}
	return response;
};
// console.log(sortByName(obj));

const sortByPosition = obj => {
	const order = [];
	const orderAsMap = new Map();

	const res = {};

	Object.keys(obj).forEach(key => {
		// orderAsMap.set(obj[key]['position'], obj[key]);
		order[obj[key]['position']] = key;
	});
	// console.log(
	// 	'SORTED ARRAY FROM MAP:',
	// 	[...orderAsMap.entries()].sort()
	// );
	order.forEach(key => {
		// console.log('order loop key', key)
		res[key] = obj[key];
	});
	return res;
};

console.log(sortByPosition(obj));
