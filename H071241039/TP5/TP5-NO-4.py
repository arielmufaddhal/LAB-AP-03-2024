kata = input("Input your string: ")
print("===============")
def substring(kata):
    for i in range(1, len(kata) + 1):
        for j in range(len(kata) - i + 1):
            print(kata[j:j+i])
substring(kata)

