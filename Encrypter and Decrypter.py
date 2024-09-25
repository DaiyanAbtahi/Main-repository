import random
import os
import string

KEY_OF_WORD: dict[str, list] | None = None # insert Key of word here


def create_key() -> None:
    extra_characters = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТ'
    
    charecters: str = string.ascii_letters + string.digits + string.punctuation + ' ' + '\n'
    character_list = list(charecters + extra_characters)
    alphabet_code: dict[str, list] = {charecter: [] for charecter in charecters}

    random.shuffle(character_list)
    index: int = 0
    
    for alphabet in alphabet_code:
        for _ in range(2):
            alphabet_code[alphabet].append(character_list[index])
            index += 1
    print(alphabet_code)

def coded_message(message: str) -> str:
    try:
        word_list: list = list(message)
        coded_word: str = ""
        for word in word_list:
            selected_key_word: str = random.choice(KEY_OF_WORD[word])
            coded_word += selected_key_word
            
        return coded_word
    except:
        print('\nERROR_\n')
        quit()

def decoded_message(message: str) -> str:
    try:
        coded_list: list = list(message)
        decoded_word: str = ""
        for coded_word in coded_list:
            for word in list(KEY_OF_WORD):
                if coded_word in KEY_OF_WORD[word]:
                    decoded_word += word
                    
        return decoded_word
    except:
        print('\nERROR_\n')
        quit()

def code_file(file_path: str) -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            txt_data: str = file.read()

        coded_word: str = ""
        for word in txt_data:
            if word in KEY_OF_WORD:
                selected_word = random.choice(KEY_OF_WORD[word])
                coded_word += selected_word
            else:
                # Handle characters that aren't in the dictionary (optional, log or skip)
                coded_word += word  # Keeping unknown characters as they are
                
        with open(file_path, 'w', encoding='utf-8') as write_code:
            write_code.write(coded_word)
        
        print(f"File {file_path} has been encrypted successfully.")
    
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decode_file(file_path: str) -> None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            txt_data: str = f.read()
        
        decoded_word: str = ""
        for coded_word in txt_data:
            found = False
            for word, codes in KEY_OF_WORD.items():
                if coded_word in codes:
                    decoded_word += word
                    found = True
                    break
            if not found:
                decoded_word += coded_word  # Keep unknown characters as they are

        with open(file_path, 'w', encoding='utf-8') as write_code:
            write_code.write(decoded_word)
        
        print(f"File {file_path} has been decrypted successfully.")
    
    except Exception as e:
        print(f"Error decrypting file: {e}")

if __name__ == "__main__":
    os.system('cls')
    
    if KEY_OF_WORD == None:
        create_key()
        print("\nSet this as 'KEY_OF_WORD' in the code to continue using this script.")
        quit()
    
    while True:
        choice: int | str = input("""What do you want to do?:
                        1. Encrypt a text that I input
                        2. Decrypt a text that I input
                        3. Encrypt a file (File Path required)
                        4. Decrypt a file (File Path required)\n\n""")
        if choice.isdigit():
            choice = int(choice)
            os.system('cls')
            if choice < 6 and choice > 0:
                if choice == 1:
                    message: str = input("Write the message you want to encrypt:\n")
                    encrypt_message: str = coded_message(message)
                    print (f"Encrypted message: {encrypt_message}")
                    break
                elif choice == 2:
                    message: str = input("Write the message you want to decrypt:\n")
                    decrypt_message: str = decoded_message(message)
                    print(f"Decrypted message: {decrypt_message}")
                    break
                elif choice == 3:
                    file_path: str = input("Enter the file path of the file you want to encrypt:\n")
                    os.system('cls')
                    code_file(file_path)
                    break
                elif choice == 4:
                    file_path: str = input("Enter the file path of the file you want to decrypt:\n")
                    os.system('cls')
                    decode_file(file_path)
                    break
                elif choice == 5:
                    print(create_key())
                    break
            else:
                print("\nERROR_INVALID_INPUT_\n")
                continue
        else:
            print("\nERROR_INVALID_INPUT_\n")
            continue