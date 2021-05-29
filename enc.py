import pyDes


def img_encryptor(im_path, key):

    encryptor = pyDes.triple_des(
        key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

    with open(im_path, 'rb') as im_file:

        image = im_file.read()

    encrypted_data = encryptor.encrypt(image)

    with open(f"{im_path.split('.')[0]}.enc", 'wb') as enc_file:
        enc_file.write(encrypted_data)


if __name__ == '__main__':

    try:
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

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except Exception as e:
        print(f"\nSome error occurred, error detail: {e}")
