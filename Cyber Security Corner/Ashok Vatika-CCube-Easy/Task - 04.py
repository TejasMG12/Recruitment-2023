encrypted_txt = "|OP`Z<E]|Y\$"
key = "Jai Shree Ram!"
# Your code goes here
ans=""
for i in range(len(encrypted_txt)):
    ans+= chr(ord(encrypted_txt[i])^ord(key[i % len(key)]))
print(ans)

