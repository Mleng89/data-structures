def combinationSum(candidates, target: int):
    res = []

    def dfs(i, currList, total):
        if i >= len(candidates) or total > target:
            return
        if total == target:
            res.append(currList.copy())
            return
        currList.append(candidates[i])
        dfs(i, currList, total + candidates[i])
        currList.pop()
        dfs(i + 1, currList, total)

    dfs(0, [], 0)
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
