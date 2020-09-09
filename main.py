import math

array=[]

def solution(area):
    global array
    array =[]
    area_cut = area 
    
    def take_square(count):
                
        platform = int(math.sqrt(count))
        platform = platform**2
        array.append(platform)
        count = count - platform
        return count

    while area_cut >0 :
        area_cut = take_square(area_cut)

    return(array)


