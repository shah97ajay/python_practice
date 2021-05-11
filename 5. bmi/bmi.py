Height= float(input("Enter your height in cm: "))
Weight= float(input("Enter your wight in kgs: "))

Height = Height/100
BMI = Weight/(Height * Height)
print("your body mask index is : ","{0:.2f}".format(BMI))

if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")