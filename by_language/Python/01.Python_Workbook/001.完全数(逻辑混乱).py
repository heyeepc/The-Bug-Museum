def factors(n): 
  result = [] 
  Perfect = [] 
  for i in range(1, n): 
  if n % i == 0: result.append(i) 
    return result a = sum(z for z in result) if n == a: Perfect.append(a)
