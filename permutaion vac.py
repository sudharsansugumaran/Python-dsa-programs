def permutations(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current.copy())
            return

        for i in range(len(remaining)):
            current.append(remaining[i])

            new_remaining = remaining[:i] + remaining[i+1:]

            backtrack(current, new_remaining)

            current.pop()

    backtrack([], nums)
    return result


nums = [1, 2, 3]
print(permutations(nums))