alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
'w','x','y','z']
direction = input("Type 'encode' to Encrypt and Type 'decode' to Decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
    
def cesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = new_position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here the{cipher_direction}d result : {end_text}")
should_continue = True
while should_continue:
    direction =  input("Type 'encode' to Encrypt and Type 'decode' to Decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25 
    cesar(start_text = text , shift_amount = shift , cipher_direction = direction)
    result = input("Type 'Yes' if you want to go Again . Otherwise type 'No' .\n")
    if result == "No":
        should_continue = False
        print("Goodbye")