import pyDes


def img_decryptor(enc_file_path, key, file_ext):

    decryptor = pyDes.triple_des(
        key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

    with open(enc_file_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()
        decrypted_data = decryptor.decrypt(encrypted_data)

    with open(f"{enc_file_path.split('.')[0]}_decrypted.{file_ext}", 'wb') as img_file:
        img_file.write(decrypted_data)


if __name__ == '__main__':

    try:
        enc_file_path = input(
            r'Please enter the path of the file you want to decrypt: ')


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

            print(f"{enc_file_path} decrypted successfully and stored as {enc_file_path.split('.')[0]}_decrypted.{ext}")

        except FileNotFoundError:
            print("The file you have specified doesn't exist, Please try again with a valid file..")
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except Exception as e:
        print(f"\nSome error occurred, error detail: {e}")
