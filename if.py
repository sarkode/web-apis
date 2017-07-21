i = 8
if (i % 2):
   print "odd number"
else:
   print "even number"

# The % is a mudulu that devide two numbers 

def even (number):
	acc = 0
	for i in number :
		 if (i % 2 ==0):
			 acc = acc + i
			 return acc
			 
print even ([1,6,3,7,5,8])
print even ([76,9,43,7])

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)

	
