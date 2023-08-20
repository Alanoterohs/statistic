def average(listNumber: list) -> int:
    averageReturn = 0
    for value in listNumber:
        averageReturn += value
    return averageReturn/len(listNumber)

def median(listNumber: list) -> int:
    sorted(listNumber)
    index = len(listNumber)//2
    if(len(listNumber) % 2 == 0):
        return (listNumber[index-1] + listNumber[index])/2
    else:
        return listNumber[index]
