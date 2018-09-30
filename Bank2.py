balance = 2000
rt = 0.01
years = 0

while True:
    
 print(' Welcome to STATE BANK OF INDIA \n')

 print('Please Choose an Option')
 print('Option 1: Debit')
 print('Option 2: Credit')
 print('Option 3: Check_Balance')
 print('Option 4: Balance with Updated Interest')
 print('Option 5: Exit\n')


 option = int(input('Choose an Option:'))
 years = years + 1

 if option == 1:
  Debit = int(input('How much do you want to Debit?:'))
  balance = balance - Debit
  print (' New Balance :', balance)
 elif option == 2:
  Credit = int(input('How much do you want to Credit?:'))
  balance = balance + Credit
  print (' New Balance:', balance)
 elif option == 3:
  print('Balance:', balance)
 elif option == 4:
  balance = balance * ( 1 + ( 0.0001 * years ))
  print (' Updated Balance', balance)
 elif option == 5:
  print (' Thank you for using THE STATE BANK OF INDIA ')
  exit()
 else:
  print('Invalid Input')
