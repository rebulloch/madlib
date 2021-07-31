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

#######################################################################
# Rachel's first madlib program:
# ------------------------------
# input_type_list = [ 'holiday', 'verb', 'proper noun', 
#                     'place', 'noun', 'verb', 
#                     'verb', 'verb', 'verb', 
#                     'noun', 'noun', 'plural noun', 
#                     'silly word', 'adjective', 'adjective', 
#                     'piece of clothing', 'body part']
# blanks = []

# for input_type in input_type_list:
#     blanks.append(input(f'Enter a {input_type}: '))

# print(f'''
# Today is {blanks[0]}! I'm going to {blanks[1]} to celebrate! Will {blanks[2]} go to a {blanks[3]} to celebrate? Will you throw a {blanks[4]}
# to celebrate? Will you {blanks[5]} and {blanks[6]}? Is anybody you know going to come over and {blanks[7]} me? I like to {blanks[8]}for
# {blanks[9]} when this holiday comes around! I will decorate my {blanks[10]} with {blanks[11]} and {blanks[12]}s! That wll make it very 
# {blanks[13]} and perfect for this time of year! Happy holidays! 
# Oh yeah! Do you like my new {blanks[14]} {blanks[15]}? It fits perfectly over my {blanks[16]}! See ya later!
# ''')

#######################################################################
# Working with files and arguments:
# ---------------------------------
# I know, you are probably wondering why you would get into an argument with your computer program,
# but that is not what an argument means in this context.  Remember how you run this Python program
# from the terminal by tying `python madlib.py`?  Well, you can pass extra information to the program
# by adding a space, and then extra words after the program name.  The extra words can be stored in
# a list and used to change how the program runs; this list is called the argument list.  It may be
# easier to understand if you think of arguments as parameters that are passed to the entire program
# instead of just to a function.
# Anyway, to get the arguments we have to import a module called `sys` that we can use to see the
# arguments the user passes into the program when they type in the command to start it.
import sys

arguments = sys.argv[1:]

# There we go! now we have a list of all the arguments that the user passed, but the program doesn't
# magically know what to do with them, we have to teach it what to expect and how to react appropriately.
# You may have noticed that the list above skipps the first item in argv (because of the [1:]).  This is
# because the first item in the argv list is the name of the program, which we will not be using.
# Now, you may be wondering why we want arguments at all, well I'm gald you asked!  By using arguments
# we can let the user tell us about a file outside the program that we can use to create our MadLib.  We
# could also just ask them with prompts instead, but allowing the user to pass that information as an
# argument instead allows for some neat things that we will cover in future lessons.

# Now that you have a basic understanding of arguments and what we are tying to achieve by using them
# we can teach the program what it should expect:

file_to_open = ''
if (len(arguments) > 0):
    file_to_open = arguments[0]
else:
    file_to_open = 'sample_madlib.txt'

# The if-block above teaches our program to expect the first argument to be the name of a file that will
# be opened.  The else-block will execute if the user did not provide an argument by using the sample
# file that should be in the same directory.

# Now that we expect to have a file to open, we will show how to open it using a `with open() as...` block.
# This block of code tells the program to open a file (the file we provided earlier) and it will automatically
# close the file for us when we exit the block.  The open() function takes two parameters as strings, the
# name of the file we want to open and what we want to be able to do with it.  In this case, we only want to
# read the file, not change it, so we use 'r' for read as the second parameter.  Finally, the `as input_file`
# part means that we can use the variable name `input_file` to reference the file we have open until we leave
# the with-block.

# The format of the input file should be that all 'blanks' are represented with '{some_prompt}' where 'some_prompt'
# is replaced with the prompt to tell the user what to type.  The prompts must use '_' characters instead of spaces
# if more than a single word is required.  See the example file, 'sample_madlib.txt' to see how it should look.

with open(file_to_open, 'r') as input_file:
    # an open file has a built-in method called readlines().  A method is like a special function that is
    # built into some types of variables called 'objects'.  In this case, the input_file variable is an
    # object with a readlines() method.  In VSCode, you can find the methods that an object has by typing
    # the object's variable name followed by a '.' character, which will bring up a list of known methods!
    # the readlines() method will give us a list of strings where each string matches with a line of text
    # in the input_file.
    input_lines = input_file.readlines()

    # String variables are also objects, so we can use the '.' after a string to access its methods too!
    # We can use string methods to manipulate the input from the file.  The first thing we will do is
    # to join the input lines into a single string by using the join() method.  The join() method will
    # combine a list of strings into a single string, the portion before the '.' character is what you want
    # as a separator.  Since we don't need to add a separator in this case, we will use an empty string: ''.
    joined_lines = ''.join(input_lines)

    # Now that we have a single string, we can split it into words by using the split() method.  This method
    # will split the string provided before the '.' by some separator.  If you don't provide a separator then
    # it will split it by 'whitespace' meaning spaces, tabs, and new-lines.
    input_words = joined_lines.split()

    # # NOTE: you can combine the above three lines into a single line like this:
    # input_words = ''.join(input_file.readlines()).split()
    
    # before the loop, we need an empty list of 'blanks'
    blanks = []

    # in this for-loop, we will need an index and each word so that we know which word to replace with the user's input
    # so we can use the enumerate() function to get it.  Whenever you don't just need the item from a list, but you also
    # need to know *where* that item is in the list, you can use enumerate() like this:
    for (index, word) in enumerate(input_words):

        
            # Because all blank-prompts are contained within {} we know that we found a blank when we find a word that starts with '{'
        if word[0] == '{':

            # The line below extracts the prompt from the {} portion, splits the string on '_' characters, and then joins
            # the string back together with a ' ' (space) character as the separator
            prompt = ' '.join(word[1:word.index('}')].split('_'))

            # We then collect the user's response to the prompt, add anything that came after the final '}' character so that we
            # don't accidentally lose some punctuation, and then replace the word in our input_words list with the user's input.
            input_words[index] = input(f'Enter a {prompt}: ') + word[word.index('}') + 1:]
    
    # now that all of the prompts have been replaced with the user's input, we can join the list back into a string so that it is ready
    # to output to the terminal!
    madlib_output = ' '.join(input_words)

    # I think it looks better with a blank line before the madlib stats, so that is the reason for the empty print() function
    print()
    print(madlib_output)

