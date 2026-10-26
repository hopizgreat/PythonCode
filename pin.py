
card_valid = str(input("enter access card True or False:"))
pin = str(input("enter pin True or False:"))
if card_valid == "True":
    print("access card accepted")
    if pin == "True":
        print("access granted")
    else:
        print("incorrect PIN")
else:
    print("Invalid access card")