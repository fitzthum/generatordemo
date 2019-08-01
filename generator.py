# a demonstration of some generator and iterator stuff
import random 
import itertools
import timeit

def gen1():
  print("gen1")
  for i in range(100): 
    yield i

def gen2():
  print("gen2")
  i = 1
  while i < 100: 
    yield i 
    i = random.randint(1,101)

def gen3(x):
  for i in range(x):
    yield random.randint(1,x) 

def gen4(x):
  if x > 20: 
    return None
  else:
    for i in range(x):
      yield random.randint(1,x)

def gen5():
  return None 
  yield 1

def gen6():
  yield 1 
  yield 2 
  yield 3

def reader1():
  for n in gen1():
    print(n)

def reader2():
  for n in gen2():
    print(n)

def reader3():
  gen = itertools.chain(gen1(),gen2())
  for n in gen:
    print(n)

def reader4():
  its = []
  for i in range(20):
    its.append(gen3(i))
  print(list(its))
  for n in itertools.chain(its):
    print(list(n))

# won't work 
def reader5():
  i = 1
  it = gen4(i)
  # this check never works
  while it is not None:
    print(it)
    i += 1
    it = gen4(i)

# more extreme version of 5
def reader6():
  if gen5() is not None:
    print("Well...")

def reader7():
  for i in gen5():
    print(i)
  print("that's it")

def reader8():
  i = 1
  it = gen4(i)
  while i < 20:
    for n in gen4(i):
      print(n)
    i += 1

def reader9():
  for i in gen2():
    for j in gen3(i):
      print(j)

def reader10():
  try:
    print(gen5().next())
  except:
    print("end")

def reader11():
  for i in gen6():
    print(i)

reader11()
