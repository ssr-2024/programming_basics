# Playing and testing elif-Statements

name=input('Please enter your name ')
age=input('Please enter your age ')

if name == 'Alice':
    print('Hi Alice')
elif int(age) < 12:
    print('You are not Alice, kiddo')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie') # example from Automate the Boring Stuff
# However, what happens if the person is older than 12 but younger than 100? Therefore:
elif int(age) < 100:
    print('You might be as old as Alice, but you are not her.') # Adds an answer in case the person is Alice's age
# Otherwise an else-Statement would've done the trick, according to the book.