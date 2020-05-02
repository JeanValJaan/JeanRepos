limit = int(input("Enter the limit of fibonacci numbers to generate :"))
a = 1
b = 1
total = 0
fibo_list = [a, b]
while total < limit:
  total = a + b
  a = b
  b = total
  fibo_list.append(b)
print("From 1 to {} fibonacci numbers are :".format(limit), (fibo_list))
