
gender = int(input("Введите 1 если вы мужчина и введите 2 если вы женщина: "))
height = int(input("Введите ваш рост в см: "))

if (gender == 1):
    result = int(((height*4/2.54)-128)*0.453)
elif (gender == 2):
    result = int(((height*3.5/2.54)-108)*0.453)
else :
    print("Введите 1 или 2, зависимо от пола")

print("Ваш идеальный вес: " + str(result) + " " + "кг")
