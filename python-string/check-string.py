#3 Check if the skill in resume is found
resume = input("Enter resume text:")

if "python " in resume.lower():
    print("Python skill found")

else:
    print("Python skill not found")