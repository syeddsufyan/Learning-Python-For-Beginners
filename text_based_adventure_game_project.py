name = input("Enter your name!")
print(f"Greeting {name}! Welcome to your adventure ")
start = input('would you rather play the game or perish? ')
if start == 'play':
    print("Great let's play the game! ")
    setting = input('Want to go to the jungle or tha desert? ')
else:
    print('Lame, Okay you\'re dead me....')
    quit()
    
if setting == 'jungle':
    print('Welcome to the mighty Amazon rainforest! Your tour guide told you to wait here....')
    response = input('But he has been game a long time.... follow him or wait here')
    if response == 'follow':
        print('You folloe him into the trees,,,')
    elif response == 'wait':
        print('You wait another ten minutes. and he still isn\'t here? ')
    else:
        print('Invalid response! you lose')
    quit()
        
elif setting == 'desert':
    print('Welcome to the mighty Sahra Desert! Your tour guide told you to wait here....')
    response = input('But he has been game a long time.... follow him or wait here')
    if response == 'follow':
        print('You folloe him into the dunes,,,')
    elif response == 'wait':
        print('You wait another ten minutes. and he still isn\'t here? ')
    else:
        print('Invalid response! you lose')
    quit()
else:
    print('Invalid response! you lose')
     quit()