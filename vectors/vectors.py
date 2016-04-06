def scalar( value ):
  return value

def vector( list ):
  # forces iterables in vectors for no particular reason
  vector = []
  for element in list:
    vector.append(element)
  return vector

print(vector({1:2,3:4}))
