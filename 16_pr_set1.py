mydict = {
    "pankha": "fan",
    "dabba": "box",
    "ghari": "watch",
    "ghar": "house"
}

a = input("enter hindi word : ")
# print("the meaning of", a ,"is : ",mydict[a])

#below line will not show an error if the key is not present in dict
print("the meaning of", a ,"is :",mydict.get(a))