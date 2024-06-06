import random
import numpy as np

def vonNeumann(u):
  u= (u**2 // 100) % 10000
  return u

def randMixto(a,c,M,u):
  return (a*u+c) % M 

def randMulti(a,M,u):
  return (a*u) % M

def ej1_a(x):
  for _ in range(10):
    x = vonNeumann(x)
    print(x)

def ej1_b(x):
  print(x)  
  for _ in range(10):
    x = randMixto(5,4,2**5,x)
    print(x)

def ej1_c(x, a, c, M):
  xs = [x]
  print(x)
  while True:
    x = randMixto(a,c,M,x)
    if x in xs:
      print("se repite" + " " + str(x))
      print(len(xs))
      break

    xs.append(x)
  print(len(xs))


def ej2(num_iter):

  '''
  Las probabilidades de ganar son las siguientes:
  P(X >= 1 | U < 1/2) + P(X >= 1 | U >= 1/2)  


  '''
  won_games = 0

  for _ in range(num_iter):
    u = random.random()
    num = random.random() + random.random()
    if u >= 0.5:
      num += random.random() 
    
    if num >= 1:
      won_games += 1
  print(f"P[X>=1] = {won_games / num_iter}")

'''
  n      | 100  | 1000  | 10000  | 100000  | 1000000
 P[X>=1] | 0.69 | 0.649 | 0.6614 | 0.66816 | 0.666195
'''

def ej3(num_iter):
  won_games = 0
  for _ in range(num_iter):
    rand = random.random()
    num = random.random() + random.random()
    if rand >= 1/3:
      num += random.random()
    
    if num <= 2:
      won_games += 1
  print(f"P[X<=2] = {won_games / num_iter}")

'''
  n       | 100  | 1000  | 10000  | 100000  | 1000000
  P[X<=2] | 0.94 | 0.884 | 0.8891 | 0.88961 | 0.88903
'''

# Montecarlo en (0,1)
def Montecarlo(fun, nsim):
  Integral = 0
  for _ in range(nsim):
    x = random.random()
    Integral += fun(x)
  
  return Integral / nsim

# Montecarlo en (a,b)
def Montecarlo_ab(fun, nsim, a, b):
  Integral = 0
  for _ in range(nsim):
    Integral += fun(a + (b-a) * random.random())
  return Integral * (b-a) / nsim

# Montecarlo en (0,inf)
def Montecarlo_inf(fun, nsim):
  Integral = 0
  for _ in range(nsim):
    y = random.random()
    Integral += fun(1/y - 1) / y**2
  
  return Integral / nsim

# Integrales dobles
# Por contrato fun toma dos variables

def Montecarlo_doble(fun, nsim):
  Integral = 0
  for _ in range(nsim):
    Integral += fun(random.random(),random.random())
  
  return Integral / nsim

def Montecarlo_doble_abcd(fun, nsim, a, b, c ,d):
  Integral = 0
  for _ in range(nsim):
    Integral += fun(a + (b-a) * random.random(), c + (d-c) * random.random())
  
  return Integral * (b-a) * (d-c) / nsim

def Montecarlo_doble_inf(fun, nsim):
  Integral = 0
  for _ in range(nsim):
    x = random.random()
    y = random.random()
    Integral += fun(1/x - 1, 1/y - 1) / (x**2 * y**2)
  
  return Integral / nsim

# Ejercicio 5b

def fun5b(x):
  return x / (x**2 - 1)

def fun5c(x):
  return x * (1 + x**2) ** (-2)

def fun5d(x):
  return np.exp(-x**2)

def fun5e(x, y):
  return np.exp((x + y)**2)

# Indicadora para f
def If(x, y):
  if x < y: return 1
  else: return 0

def fun5f(x, y):
  return np.exp(-(x + y)) * If(x, y)

# Ejercicio 6

def valorPi(nsim):
  enCirculo = 0
  for _ in range(nsim):  
    u1 = 2*random.random() - 1
    u2 = 2*random.random() - 1

    if u1**2 + u2**2 <= 1:
      enCirculo += 1
  return 4 * enCirculo / nsim

'''
n = 1000   3.136
n = 10000  3.1432
n = 100000 3.14224
'''

def ej7(nsim):
  N = 0
  for _ in range(nsim):
    sum = 0
    n = 0
    while sum <= 1:
      sum += random.random()
      n += 1
    N += n 

  return N / nsim

def ej8(nsim):
  val = np.exp(-3)
  N = 0
  for _ in range(nsim):
    prod = 1
    n = 0
    while prod > val:
      n += 1
      prod *= random.random()
    N += (n-1)

  return N / nsim
    

print(ej8(10000000))
