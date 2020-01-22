# here the code is modified so that the program does not blow up and display error massages due to wrong input. i1t simply exits.
# this is to return the sum of num1 and num2.
def add(num1, num2):
	return num1 + num2
# this is to return the result of subtracting num1 and num2
def sub(num1, num2):
	return num1 - num2
# this is to return the product of num1 and num2
def mul(num1, num2):
	return num1 * num2
# this is to return the result of dividing num1 and num2	
def div(num1, num2):
	return num1 / num2
	
	 #this shows up to signfy the booting of the program.
print ("booting system")
print ('.....................')
print ( 'configuring settings :_ _ _')
print ('system ready') 
 #this is to capture the name of the particpant and repond accordingly.
myVar = "hello!"
print (myVar) 
myName = input('what is your name?') 
print ('pleased to meet you')
print (myName)
print ('My name is Nine.')
 # this is to capture the intentions of the particpant
print ('I would like to run some simple analysis.')
myPad = input('Would you do some simple calculations with me?') 
 # this is a conditional operator that provides a response depending on the answers given above.
print (myPad) 
if ( myPad == "yes"):
	print ("okay let us proceed then.")
	print ("please enter the relevant inputs where necessary.")
elif(myPad == "no"):
	print ("okay i understand.")
else: 
	print ("Thats an invalid response,system will now  shutdown")
		
        #CALCULATOR STARTS HERE
def main():
	user_continue = True
	while user_continue:
		#Allows user to run basic calculator operations with two numbers.
		validinput = False
		while not validinput:
		#this is the exeption.
			try:
			#gets user input
				num1 = int(input("what is number 1?")) 
				num2 = int(input("what is number 2?"))
				operation =input("what do you whant to do? 1)add,2)subtract,3)multiply,4)divide)")
				validinput = True
			except:# if the program fails
				print("invalid input. please try again ")
		#determine the program.
		if (operation == '1'):
			print("adding...")
			print(add(num1, num2))
		elif (operation == '2'):
			print("subtracting...")
			print(sub(num1, num2))
		elif (operation == "3"):
			print("multiplying...")
			print(mul(num1, num2))
		elif (operation == '4'):	
			print("dividing...")
			print(div(num1, num2))
		else:
			print("I dont understand") 
		#ask user to continue
		User_yn = input("would you like to continue?(y for yes or any other key to exit)")
		if(User_yn != "y"):
			user_continue = False
			break
		else:
			continue
