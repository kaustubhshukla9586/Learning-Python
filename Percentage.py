english = float(input("Enter your marks in English: "))
maths = float(input("Enter your marks in Maths: "))
science = float(input("Enter your marks in Science: "))
sst = float(input("Enter your marks in Social Studies: "))
hindi = float(input("Enter your marks in Hindi: "))
total = english + maths + science + sst + hindi
max_marks = int(input("Enter max number of marks in each subject: "))
actual = max_marks * 5

percentage = (total/actual)*100

if percentage >= 90:
    print("Excellent, your percentage is:",percentage)
elif 70<=percentage<90:
    print("Very Good, your percentage is:",percentage)
elif 60<=percentage<70:
    print("First Division, your percentage is:",percentage)
elif 50<=percentage<60:
    print("Second Division, your percentage is:",percentage)
elif 40<=percentage<50:
    print("Third Division, your percentage is:",percentage)
else :
    print("You Failed, your percentage is:",percentage)