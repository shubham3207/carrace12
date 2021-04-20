def sum_element(l):
    if(len(l) == 1):
        return l[0]
    else:
        value = l.pop()
        return value+sum_element(l)

if __name__ == "__main__":

    list1 = [2,4,6,8]
    result = sum_element(list1)
    print('sum of element :', result)