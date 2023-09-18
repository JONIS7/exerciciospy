num = int(input('Digite um numero: '))
a, b = 0, 1
fibonacci_sequence = []
while len(fibonacci_sequence) < num:
    fibonacci_sequence.append(a)
    a, b = b, a + b
print(fibonacci_sequence)