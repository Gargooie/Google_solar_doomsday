arr = ['A','e','a','D','f','B'] 
arr.sort(key=lambda x:(not x.islower(), x))
print(arr)

index = 0
dots_count=[]
while index < len(array[0]):    #finding every dot at the array element
    

    index = array[1].find('.', index)
    if index == -1:
        break
    print('got', index)

    dots_count.append(index) #array for finding dots in the list
    index +=1


print(array[7][dots_count[0]+1:dots_count[1]])

def bubble_sort(nums):  
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
