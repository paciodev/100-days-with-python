#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open(f"{__file__}/../input/starting_letter.txt") as f:
    starting_letter = f.read()
    
    with open(f"{__file__}/../input/invited_names.txt") as f2:
        invited_names = f2.read().split('\n')
        for name in invited_names:
            mail_to_send = starting_letter.replace('[name]', name)
            print(name)
            with open(f"{__file__}/../output/letter_for_{name}.txt", 'w') as f3:
                f3.write(mail_to_send)