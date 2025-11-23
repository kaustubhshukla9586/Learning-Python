def student_marks(english,hindi,maths):
    avg = (english+hindi+maths) / 3
    if avg>33:
        print(f"Pass! Your average is : {avg:.2f}")
    else:
        print(f"Fail! Your average is : {avg:.2f}")

english = int(input("Enter your English Marks: "))
hindi = int(input("Enter your Hindi Marks: "))
maths = int(input("Enter your Maths Marks: "))
student_marks(english, hindi, maths)