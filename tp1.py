def average(listNumber: list) -> int:
    averageReturn = 0
    for value in listNumber:
        averageReturn += value
    return averageReturn/len(listNumber)
