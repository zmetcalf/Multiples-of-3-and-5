naturalNumbers = []

for questionNumber in range (1, 100):
    if(((questionNumber % 5) == 0) or ((questionNumber % 3) == 0)):
        naturalNumbers.append(questionNumber)
        
print naturalNumbers