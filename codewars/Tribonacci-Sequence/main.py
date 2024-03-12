# Recursive
def tribonacci(signature, n):
    if n < len(signature):
        return signature[:n]

    next_num = sum(signature[-3:])
    signature.append(next_num)
    return tribonacci(signature, n)


print(tribonacci([1, 1, 1], 10))