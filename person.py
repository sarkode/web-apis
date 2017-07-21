def get_age():
  age = (int)(raw_input("What is your age?"))
  return age

def get_name():
  return  raw_input("What is your name?")


age = get_age()
name= get_name()
print "Hey, " + name + " , you are " + age + "years  old, dude!"
