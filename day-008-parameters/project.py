from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(encode_or_decode):
    result = ''

    new_shift = shift
    if encode_or_decode == 'decode':
        new_shift = shift * -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = 0
            new_position = position + new_shift
            
            if new_position > len(alphabet):
                new_position = new_position - len(alphabet)
            elif new_position > len(alphabet):
                new_position = new_position + len(alphabet)
            
            result += alphabet[new_position]
        else:
            result += letter
    
    if encode_or_decode == 'encode':
        print(f'The encrypted text is: {result}')
    else:
        print(f'The decrypted text is: {result}')

def get_direction():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        return direction
    get_direction()

end = False

while not end:
    direction = get_direction()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)

    caesar(direction)

    is_end = input("Do you want to end the game? Type 'y' or 'n'\n").lower()
    if is_end != 'n':
        print('Bye!')
        end = True

