naturalNumbersTotal = 0

for questionNumber in range (1, 1000):
    if(((questionNumber % 5) == 0) or ((questionNumber % 3) == 0)):
        naturalNumbersTotal = questionNumber + naturalNumbersTotal
        
print naturalNumbersTotal