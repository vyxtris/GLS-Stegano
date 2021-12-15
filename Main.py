# 2301894155 - Valentino Nooril

import steganoImage
import uploadImage

def main():
    a = int(input("Steganography C&C\n1.Create new C&C\n2.Get C&C command\n>> "))

    if (a == 1):
        filename = steganoImage.encode()
        link = uploadImage.upload(filename)

    elif (a == 2):
        print("Decoded Word : " + steganoImage.decode())
    else:
        raise Exception("Enter correct input")

if __name__ == "__main__":
    main()