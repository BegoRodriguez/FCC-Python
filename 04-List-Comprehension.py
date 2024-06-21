# In this project, you'll write a program that takes a string 
# formatted in Camel Case or Pascal Case, then converts it into Snake Case.

# You'll learn how to use List Comprehension instead of a loop to achieve 
# the same results.

def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()