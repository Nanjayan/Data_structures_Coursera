# python3


def max_sliding_window_naive(sequence, m):
    if not sequence:
        return []
    stack_1, maximums = [], []
    for i, num in enumerate(sequence):
        # remove the queue head when it's size over the limited length m
        if i >= m and stack_1[0] <= i - m:
            stack_1.pop(0)
        while stack_1 and sequence[stack_1[-1]] <= num:
            stack_1.pop()
        stack_1.append(i)
        if i >= m - 1:
            maximums.append(sequence[stack_1[0]])
        
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_naive(input_sequence, window_size))))

