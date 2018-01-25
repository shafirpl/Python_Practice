import array
import copy

def reverse(list2):
    value = len(list2)-1
    for i in range(0,value):
        array_value = list2[i]
        list2[i] = list2[value]
        list2[value] = array_value
        value -= 1
        if value==i:
            break
    return list2



def rotation():

    list1 = [1,2,3,4,5,6];
    value = input("Enter the index you wanna rotate: ")
    real_value = value+1

    print "before rotaiton"

    print list1
    list2 = copy.copy(list1)


    print "after rotation"

    if value==len(list1)-1:
        print list1
        return
    elif value==0:
        list3 = reverse(list2)
        print(list3)
        return




    for i in range(0,len(list1)):
        list2[i] = list1[real_value]
        real_value += 1
        if real_value>len(list1)-1:
            break
    #print list2
    #print "real_value is:%d" %real_value

    real_value = i+1
    print "real_value is:%d" %real_value
    # print list2
    # print list1

    for j in range(0,value+1):
        #print "j value is %d" %j
        list2[real_value] = list1[j]
        real_value += 1
        if real_value>len(list1)-1:
            break
        #real_value += 1

    print list2


rotation()
