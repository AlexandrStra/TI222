def remove_zeroes(numbers: list[int]) -> int:
    non_zeros_count = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zeros_count], numbers[i] = numbers[i], numbers[non_zeros_count]
            non_zeros_count += 1

    return non_zeros_count

# Пример использования:
nums = [0, 42, 21, 0, 100, 0, 5, 1, 0, 7, 3, 0, 404, 0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42, 21, 100, 5, 1, 7, 3, 404]