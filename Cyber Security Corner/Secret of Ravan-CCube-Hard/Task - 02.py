import pyzipper
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6, '5':8}
f=0
for i in characters:
    for j in characters:
        password='n_^'+i+'`W'+j+'5'
        try:
            with pyzipper.AESZipFile('The_secret.zip') as zf:
                zf.extractall('',pwd=password.encode())
            print("password found:",password)
            f=1
        except:
            f=0
        if f==1:
            break
    if f==1:
        break





# As you can see, characters at 4th and 7th position are missing. You need to find those characters using brute-force.

# Write your code here