def pot(base, exp):
    if exp == 0:
        return 1
    else:
        return (base * pot(base, exp - 1))
    
def print_upper_texts(*text):
    for element in text:
        print(element.upper())