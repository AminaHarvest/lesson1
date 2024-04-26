def get_summ(one, two, delimiter=''):
    one = str(one)
    two = str(two)
    delimiter_string = delimiter.join(str(one)) + delimiter.join(str(two))
    return delimiter_string

python_help = get_summ('Learn ', 'python')
print(python_help.upper())