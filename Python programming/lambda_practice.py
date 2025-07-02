print((lambda f: f(5))(lambda x: x + 2))

print((lambda x: x*3)(4))

print((lambda x: (lambda y: x + y))(2)(3))

print((lambda f: f(f(f(1))))(lambda x: x + 2))

asq_pb = (lambda a: (lambda b: a * a + b))
result = asq_pb(3)(4)  # (3 * 3) + 4 = 9 + 4 = 13
print(result)  # Output: 13