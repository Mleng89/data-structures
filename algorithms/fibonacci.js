function fibonacci(num) {
	if (num <= 2) return 1;

	return fibonacci(num - 1) + fibonacci(num - 2);
}

//DYNAMIC OR USING MEMOIZATION
function fibonacciMemo(num, memo) {
	memo = {};

	if (memo[num]) return memo[num];
	if (num <= 2) return 1;

	return (memo[num] =
		fibonacciMemo(num - 1, memo) + fibonacciMemo(num - 2, memo));
}

module.exports = fibonacci;
module.exports = fibonacciMemo;
