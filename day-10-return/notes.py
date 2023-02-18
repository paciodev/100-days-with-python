def format_name(first_name, last_name):
    """Take a first and last name and format it to return the title case version of the name.""" # DOCSTRING - hover over format_name() to see it
    if first_name == '' or last_name == '':
        return 'Please provide all of the parameters'
    full_name = f'{first_name} {last_name}'.title()
    return full_name

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print(format_name(first_name, last_name))