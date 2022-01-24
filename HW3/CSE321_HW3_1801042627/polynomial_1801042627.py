poly = [[2,3], [3,1], [10, 0], [8,2]]
# polynomials accepts only non negative powers
def power(num,pow):
    if(pow <= 0):
        return 1
    return num* power(num,pow-1)
    
def efficientPower(num,pow):
    if(pow<=0):
        return 1
    val = 1
    if(pow % 2 == 1):
        val = num
        pow = pow-1
    temp = efficientPower(num, pow/2)
    return (val * temp*temp)

def calculatePolynomial(poly,x):
  sum = 0
  for r in poly:
    sum = sum + r[0] * power(x,r[1])
    print(f'{r[0]} * {x} ^ {r[1]} +')  
  print("=")
  return sum
def calculatePolynomialEfficient(poly,x):
  sum = 0
  for r in poly:
    sum = sum + r[0] * efficientPower(x,r[1])
    print(f'{r[0]} * {x} ^ {r[1]} +')  
  print("=")
  return sum

print(calculatePolynomial(poly,3))
print(calculatePolynomialEfficient(poly,3))
