#array = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
array = ["2.0.0", "2"]



dots_count1 = array[0].split(".")
dots_count2 = array[1].split(".")
for x in dots_count1:
    int(x)
for x in dots_count2:
    int(x)


#for r in range(0,min(len(dots_count1), len(dots_count2))):
if dots_count1[0] > dots_count2[0]: #первые цифры не равны
    dots_count1[0], dots_count2[0] =  dots_count2[0], dots_count1[0]

if dots_count1[0] == dots_count2[0]: #первые цифры равны, значит...
    if min(len(dots_count1), len(dots_count2)) > 1: #если колво чисел больше одного
        if int(dots_count1[1]) > int(dots_count2[1]): #если вторые числа не равны
            dots_count1[0], dots_count2[0] =  dots_count2[0], dots_count1[0]
            print("yes")

    elif (len(dots_count1) > len(dots_count2)): и если длины не равны
        dots_count1[0], dots_count2[0] =  dots_count2[0], dots_count1[0]
        print("yes new")
