def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))

 bmi = weight / (height * height)

 print("bmi = " + str(round(bmi,2)))

 if bmi < 18.5:
  print("Under Weight")
  bmi=-1
  return bmi
 
 elif 18.5 <= bmi <= 25.0:
  print("Normal Weight")
  bmi=0
  return bmi

 elif bmi > 25.0:
  print("Over Weight")
  bmi=1
  return bmi


calculate_bmi(weight=57, height=1.73)