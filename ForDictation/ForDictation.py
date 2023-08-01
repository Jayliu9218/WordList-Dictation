import random

NumberPath = input('input the chapter number : ')

inputPath = '../' + NumberPath + '.txt'
outputPath = './' + NumberPath + '.txt'

LinesOfFile = 0
NewContent = []
with open(inputPath, 'r', encoding='UTF-8') as MyFile:
    for line in MyFile.readlines():
        LinesOfFile = LinesOfFile + 1
        NewContent.append(line)
print(LinesOfFile)


OrderList = [i for i in range(1, LinesOfFile + 1)]
print(OrderList)
random.shuffle(OrderList)
print(OrderList)


TempOrder = 1
with open(outputPath, 'w', encoding='UTF-8') as MyFile:
    while TempOrder <= len(OrderList):
        line = str(TempOrder) + NewContent[OrderList[TempOrder-1]-1]
        MyFile.write(line)
        TempOrder = TempOrder + 1
