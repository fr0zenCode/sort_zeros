from typing import List


def group_zeros(numbers: List[int]):

    if not numbers:
        raise ValueError
    if len(numbers) == 1:
        return numbers

    result = []
    zero_counter = 0

    for i in range(len(numbers)):
        if numbers[i] == 0:
            result.append(0)
            zero_counter += 1
        else:
            if 0 in result:
                result.insert(len(result) - zero_counter, numbers[i])
            else:
                result.append(numbers[i])
    return result


def test_group_zeros():
    assert (group_zeros([1, 0, 2, -3, 123, 3423, 0, 0, -2314, 0, 12, 3, -43]) ==
            [1, 2, -3, 123, 3423, -2314, 12, 3, -43, 0, 0, 0, 0])


if __name__ == '__main__':
    test_group_zeros()
    print(group_zeros([1, 0, 2, -3, 123, 3423, 0, 0, -2314, 0, 12, 3, -43]))
