function rotate(nums, k) {
  let stopAtKTimes = 0;
  while (stopAtKTimes < k) {
    const lastNum = nums.pop();
    nums.unshift(lastNum);
    stopAtKTimes++;
  }
  console.log(nums);
  return nums;
}
rotate([1, 2, 3, 4, 5, 6, 7], 3);
