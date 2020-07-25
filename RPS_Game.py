from os import system
import random
import time
r='\033[1;91m'
g='\033[1;92m'
y='\033[1;93m'
w='\033[1;97m'
print(f'{g}  --------------------------------------')
print('|                                        |')
print('|  programmer : Sachindu Sahan           |')
print('|                                        |')
print('|                                        |')
print(f' --------------------------------------{w}')
i = 1
computer_points = 0
user_points = 0
while i < 999999:
	index = 1
	list = ["Rock","Paper","Scissor"]
	for l in list:
		print(index,l) 
		index += 1
	user_input = input('Enter Your Selecting Number : ')
	computer_input = random.choice(list)
	print(f'Computer selected {y}{computer_input}{w} ')
	time.sleep(0.3)
	if user_input == '1':
		if computer_input =='Rock':
			cp = 0
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score > {y}{user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y} Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					system('clear')
					pass
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				
				print(f'{y}Hey You Won  {w}')
				print(f"{r}Computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					system('clear')
					pass
				elif again == 'N':
					print('Bye Bye')
					system('exit()')
					break
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
		if computer_input == 'Paper':
			cp = 10
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score > {y}{user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					system('clear')
					pass
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
			
		if computer_input == 'Scissor':
			up = 10
			cp = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score > {y}{user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won{w} ')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
	if user_input == '2':
		if computer_input == 'Rock':
			cp = 0
			up = 10
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score > {y}{user_points}{w}')
			print('')
			
			if computer_points == 100:
				
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					system('clear')
					pass
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won  {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					system('clear')
					pass
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break

			if user_points != 100:
				if computer_points != 100:
					pass
		if computer_input == 'Paper':
			cp = 0
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score >{y} {user_points}{w}')
			print('')
			
			if computer_points == 100:
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won  {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
		if computer_input == 'Scissor':
			cp = 10
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score >{y} {user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won  {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
	if user_input == '3':
		if computer_input == 'Rock':
			cp = 10
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score >{y} {user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won  {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
		if computer_input == 'Paper':
			cp = 0
			up = 10
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score >{y} {computer_points} {g}Your Score >{y} {user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won {w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
		if computer_input == 'Scissor':
			cp = 0
			up = 0
			computer_points = computer_points + cp
			user_points = user_points + up
			print (f'{r}Computer Score > {y}{computer_points} {g}Your Score >{y} {user_points}{w}')
			print('')
			if computer_points == 100:
				print(f'{y}Game Over Computer Won{w}')
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points == 100:
				print(f'{y}Hey You Won {w}')
				print(f"{r}computer » Wtf come again {w}")
				again = input('Are You Wanted To Play Again Y/N : ')
				if again == 'Y':
					computer_points = 0
					user_points = 0 
					pass
					system('clear')
				elif again == 'N':
					print('Bye Bye')
					break
					system('exit()')
				else:
					break
			if user_points != 100:
				if computer_points != 100:
					pass
	i += 1