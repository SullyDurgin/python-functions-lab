inputs = []
while True:
     inputline = input("Enter numbers to multiply & enter with no number to get an answer: ")
     if inputline == "":
         break
     num = int(inputline)
     inputs.append(num)
def product(args):
     answer = 1
     for i in args:
         answer *= i
     return answer
print(product(inputs))


# I went off the rails a bit 

def product(*args):
  answer = 1
  for arg in args:
    answer *= arg
  return answer
