score = 0

python = input("Do you know Python? (yes/no): ")
aws = input("Do you know AWS? (yes/no): ")

if python == "yes":
   score = score + 10

if aws == "yes":
   score = score + 10

print("Resume Score:", score)

