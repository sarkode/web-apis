def calculate(op1 , op2, f):
  if  f== "add":
   return op1 + op2
   
  elif f == "subtruct":
   return op1 - op2
   
  elif f == "multiply":
   return op1 * op2
   
  elif f == "devide":
   return  op1 / op2
   
  else:
   print("try again")
   
   print ("select operation.")
   print("add")
   print("subtruct")
   print ("multiply")
   print ("divide")
   
   choice = raw_input("Enter your choice:")
   
   op1 = (raw_input("Enter your first number"))
   op2 = (raw_input("Enter your second number"))
   
   result = calculate(op1, op2, choice)
   print results
      
