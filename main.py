from parser import check_word

def process_input(input_string):
    words = input_string.split()
    output_words = []

    for word in words:
        result = check_word(word)
        if result == "ERRO":
            return "ERRO"
        output_words.append(result)

    return ' '.join(output_words)

if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        for line in infile:
            line = line.strip()
            result = process_input(line)
            print(result)



