# module imports
from datetime import datetime

name =input("what is your name?\n")
allowedUsers =['seyi','mike','love','a']
allowedPassword =['passwordSeyi','passwordMike','passwordLove','a']

if(name in allowedUsers):
    password =input("your password?\n")
    userId = allowedUsers.index (name)
    
    # login successful
    if(password == allowedPassword[userId]):
      currentDateTime = datetime.today();
      print(currentDateTime)
      print('welcome %s' % name)
      print('These are the available options:')
      print('1. withdrawal')
      print('2. cash deposit')
      print('3. complaint')

      selectedOption = int(input('please select an option:'))

      if(selectedOption == 1):
          print('you selected %s' % selectedOption) 
          
      elif(selectedOption == 2):
           print('you selected %s' % selectedOption)    
           
      elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            
      else:
            print('invalid option selected, please try again')


    else:
       print('Password Incorrect, please try again')

else:
    print('Name not found,please try again')
