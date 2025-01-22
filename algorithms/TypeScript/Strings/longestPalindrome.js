function longestPalindrome(s) {
	var expand = function (left, right) {
		while (left >= 0 && right < s.length && s[left] === s[right]) {
			console.log('left and right', left, right);
			left--;
			right++;
		}
		return s.slice(left + 1, right);
	};
	var result = '';
	for (var i = 0; i < s.length; i++) {
		console.log('expanding', expand(i, i));

		var odd = expand(i, i);
		var even = expand(i, i + 1);
		if (odd.length > result.length) result = odd;
		if (even.length > result.length) result = even;
	}
	return result;
}
console.log(longestPalindrome('abbak'));
