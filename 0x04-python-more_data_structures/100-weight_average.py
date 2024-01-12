#!/usr/bin/python3
def weight_average(my_list=[]):
  if not my_list:
    return 0
    
  num1 = 0
  num2 = 0

  for tuple in my_list:
    num1 += tuple[0] * tuple[1]
    num2 += tuple[1]
    
    return (num1 / num2)
