def reverse_number(n):
    if n < 0:
        return -int(str(n)[1:][::-1])
    else:
        return int(str(n)[::-1])

    
def count_by(x, n):
  result = []
  for i in range(1, n+1):
    result.append(i*x)
  return result 


def bmi(weight, height):
  bmi = weight / height**2
  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 25:
    return "Normal"
  elif bmi <= 30:
    return "Overweight"
  else:
    return "Obece"