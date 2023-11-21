MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(Emessage):
    cipher = ''
    for letter in Emessage:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            cipher += ' '
    return cipher

def decrypt(Dmessage):
    Dmessage += " "
    decipher = ""
    citext = ""

    for letter in Dmessage:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher += " "
            else:
                for key, value in MORSE_CODE_DICT.items():
                    if citext == value:
                        decipher += key

                citext = ""

    return decipher 

def main():
   print("="*100)
   print("\n")
   print("\t\t\tType :")
   print("\n\t\t\t\t1 ------> to decipher english to morse code")
   print("\t\t\t\t2 ------> to decipher morse code to english")
   print("\t\t\t\t3 ------> to exit the program")
   print("\n")
   print("\t\t\tWARNING : Please select an option within range")
   print("\n")
   print("="*100)
   
   while True:
       choice=int(input("\n\t\t\tEnter your choice : "))
       
       if choice==1:
           Emessage=input("\t\t\tEnter ENGLISH message to be translated to MORSE CODE : ")
           print("\n\t\t\t",encrypt(Emessage.upper()))
       elif choice==2:
           Dmessage=input("\t\t\tEnter MORSE CODE message to be translated to ENGLISH : ")
           print("\n\t\t\t",decrypt(Dmessage))
       elif choice==3:
           break
       else:
           print("\n\t\t\tINVALID CHOICE please try again")
           
main()