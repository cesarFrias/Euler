from string import letters

def get_names():
    file_name = open('names.txt', 'r')
    names = file_name.read()
    names = names.replace('"', '').lower()
    names = names.split(',')
    names.sort()
    return names

def find_letter_value(letter):
    return letters.find(letter) + 1

def main():
    total_value = 0
    names = get_names()
    for i, name in enumerate(names):
        word_value = 0
        for letter in name.lower():
            word_value += find_letter_value(letter)
        total_value += word_value * (i + 1)
    print total_value

if __name__ == '__main__':
    main()
