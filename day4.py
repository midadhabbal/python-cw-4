def my_name (name):
 print ("my name is " + name)
my_name ("medad")
def my_meal (food, drink):
  print (f'I like to eat {food} and while I drink {drink}')
my_meal('oat', 'milk')
def cube (number):
   return number**3
def by_there(number):
   if number % 3 == 0:
      return cube (number)
   else:
      return False
print (by_there(15))