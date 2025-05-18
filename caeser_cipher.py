import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text,shift_amount,encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1
    output_text = ""
    for letter in original_text:
        if letter not in original_text:
            letter += output_text

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position].title()
    print(f"Here's the {encode_or_decode}d result: {output_text}.")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt? ")
    text = input("Type your message? ")
    shift = int(input("Type the shift amount? "))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("GoodBye.")


