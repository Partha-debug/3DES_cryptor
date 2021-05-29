from enc import img_encryptor
from dec import img_decryptor

def show_logo():

    print("""
    
    3DES                                  __                      
      ____   _______   ___.__. ______   _/  |_    ____   _______  
    _/ ___\  \_  __ \ <   |  | \____ \  \   __\  /  _ \  \_  __ \ 
    \  \___   |  | \/  \___  | |  |_> >  |  |   (  <_> )  |  | \/ 
     \___  >  |__|     / ____| |   __/   |__|    \____/   |__|    
         \/            \/      |__|                               
                                                 ©Partha-debug
    """)

def main():
    print("Please choose a option: ")
    print("[+] 1 - encrypt a file")
    print("[+] 2 - decrypt a file")
    
    choice = input().strip()

    if choice == '1':

        im_path = input(
        r'Please enter the path of the image you want to encrypt : ')

        key = input(
            "Please enter the encryption key, It must contain 24 characters and shouldn't have any spaces: ")

        if len(key.strip()) != 24 or ' ' in key.strip():
            key = input(
                "Invalid key... Please try again with a key with 24 characters and no spaces in it: ")

        key = bytes(str(key), encoding='utf-8')

        try:
            print(
                f'Encrypting {im_path} with key {key.decode("utf-8")}, It may take several mins...')

            img_encryptor(im_path, key)

            print(
                f"{im_path} encrypted successfully and stored as {im_path.split('.')[0]}.enc")
        except FileNotFoundError:
            print("The file you have specified doesn't exist, Please try again with a valid file..")
        except Exception as e:
            print(f"Some error occurred, error detail: {e}")
    
    elif choice == '2':
         
        enc_file_path = input(r'Please enter the path of the file you want to decrypt: ')

        ext = input("Please enter the extension of the file before encryption(eg:- jpg, png the default is jpg hit enter if you want to go with it): ")

        if not ext.strip():
            ext = 'jpg'

        key = input(
            "Please enter the decryption key, It must contain 24 characters and shouldn't have any spaces: ")

        if len(key.strip()) != 24 or ' ' in key.strip():
            key = input(
                "Invalid key... Please try again with a key with 24 characters and no spaces in it: ")

        key = bytes(str(key), encoding='utf-8')

        try:
            print(
                f'Decrypting {enc_file_path} with key {key.decode("utf-8")}... It may take several mins.')

            img_decryptor(enc_file_path, key, ext)

            print(f"{enc_file_path} decrypted successfully and stored as {enc_file_path.split('.')[0]}.{ext}")

        except FileNotFoundError:
            print("The file you have specified doesn't exist, Please try again with a valid file..")
        except Exception as e:
            print(f"Some error occurred, error detail: {e}")

    else:

        print('Please enter a valid choice.')
        main()


if __name__ == '__main__':

    try:
        show_logo()
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except Exception as e:
        print(f"\nSome error occurred, error detail: {e}")