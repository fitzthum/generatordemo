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

#timeit.timeit(reader1,number=10)
#timeit.timeit(reader2,number=10)
#timeit.timeit(reader3,number=10)

reader4()

