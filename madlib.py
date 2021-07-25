# # use input() to collect what the user types in the terminal
# # the string inside the parenthesis is called a prompt, it tells the user what to type
# # there are special characters you can put in strings that have a '\' and some letter
# # in the line below, there is a '\n' that tells the computer to move to a new line after
# # outputting the prompt to the terminal, so the input will be on its own line.
# user_name = input('Hi! What is your name? \n')

# # the print() function is used to output things to the terminal, generally strings, but you
# # can also output some other variable types.  The f'' pattern inside the parenteses is for an
# # f-string, or formatted string.  You can insert variables easily into an f-string by using {}
# # with the variable name inside.  You can do more formatting than that, but you can learn about
# # that later.
# print(f'Nice to meet you, {user_name}!')

# # This is an example of a print() statement with a normal string instead of an f-string, since it
# # isn't outputting any variables.
# print("I just realized, I don't have a name.  That makes me sad.")

# # In this input function, we are telling the user that we expect exactly a 'y' or 'n' character
# # see the if..else.. block below for more about how we can react to this sort of input
# answer = input('Will you give me a name? (y/n)')

# # In this if block, we only interpret a lowercase 'y' as yes, everything else is treated as a 'no'
# # this isn't the best solution, because if the user types 'Y' or 'yes' it will be treated as a 'no'
# # later we can learn to manipulate the user's input string to help the computer understand answers
# # that would make sense; for example, we could tell it to treat any response that started with either
# # 'y' or 'Y' as a 'yes'... but then it would count 'yeah right' as a yes, so...
# if (answer == 'y'):
#     print('Yay!')
#     computer_name = input('What name will you give me? ')
#     print(f'Hurray!  My new name is {computer_name}!')
# else:
#     print('Aww... you are no fun!')

input_type_list = [ 'holiday', 'verb', 'noun', 
                    'place', 'noun', 'verb', 
                    'verb', 'verb', 'verb', 
                    'noun', 'noun', 'noun', 
                    'silly word', 'adjective', 'adjective', 
                    'piece of clothing', 'body part']
blanks = []

for input_type in input_type_list:
    blanks.append(input(f'Enter a {input_type}: '))

print(f'''
Today is {blanks[0]}! I'm going to {blanks[1]} to celebrate! Will {blanks[2]} go to {blanks[3]} to celebrate? Will you throw a {blanks[4]}
to celebrate? Will you {blanks[5]} and {blanks[6]}? Is anybody you know going to come over and {blanks[7]} me? I like to {blanks[8]}
{blanks[9]} when this holiday comes around! I will decorate my {blanks[10]} with {blanks[11]} and {blanks[12]}! That wll make it very 
{blanks[13]} and perfect for this time of year! Happy holidays! 
Oh yeah! Do you like my new {blanks[14]} {blanks[15]}? It fits perfectly over my {blanks[16]}! See ya later!
''')