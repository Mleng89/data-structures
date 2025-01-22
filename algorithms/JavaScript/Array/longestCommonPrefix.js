function longestCommonPrefix(strs) {
	if (strs.length === 0) return '';

	let prefix = strs[0];
	console.log('my prefix', prefix);

	for (let i = 0; i < strs.length; i++) {
		console.log('is this it too?', !strs[i].startsWith(prefix));
		while (!strs[i].startsWith(prefix)) {
			prefix = prefix.slice(0, -1);
			console.log('inside while loop prefix', prefix);
			if (prefix === '') return '';
		}
	}
	return prefix;
}

console.log(longestCommonPrefix(['flower', 'flow', 'flight']));
