import random
length = int(input("enter the length of password"))
sva_slova="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
main = "".join(random.sample(sva_slova,length ))
print(main)

