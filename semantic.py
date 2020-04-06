import math

keywords = ["canada", "university", "dalhousie university", "halifax", "business"]
counterDic = {"canada": 0, "university": 0, "dalhousie university": 0, "halifax": 0, "business": 0}
canadaDoc = []

for word in keywords:
    for i in range(1, 1386):
        f = open("news/News_" + str(i) + ".txt", "r")
        found = 0

        if word in f.read():
            if word == "canada":
                canadaDoc.append(i)
            counterDic[word] += 1

        f.close()

with open("wordCounter.csv", "a") as f:
    f.write("Total Documents" + " , " + str(1386) + "\n")
    f.write("Search Query" + " , " + "Document containing term (df)" + " , "
            + "Total Documents(N)/ number of documents term appeared (df)" + " , " + "Log10(N/df)" + "\n")

    for word in keywords:
        if counterDic[word] != 0:
            calculatedValue = 1386 / counterDic[word]
            calculatedValue = round(calculatedValue, 2)
            logValue = math.log10(calculatedValue)
            logValue = round(logValue, 2)
        else:
            calculatedValue = 0
            logValue = 0

        f.write(word + " , " + str(counterDic[word]) + " , " + str(calculatedValue)
                + " , " + str(logValue) + "\n")

fc = open("canadaCounter.csv", "a")
fc.write("Term" + " , " + "canada" + "\n")
fc.write("canada appeared in " + str(counterDic["canada"]) + " documents" + " , " +
         "Total Words(m)" + " , " + "Frequency (f)" + "\n")

totalWord = 0
canadaCount = 0
relativeFrequency = {}

for i in canadaDoc:
    f = open("news/News_" + str(i) + ".txt", "r")

    for lines in f.read().split("\n"):
        words = lines.split(" ")
        for word in words:
            totalWord += 1
            if word.find("canada") is not -1:
                canadaCount += 1

    fc.write("Article #" + str(i) + " , " + str(totalWord) + " , " + str(canadaCount) + "\n")
    rFrequency = canadaCount / totalWord
    rFrequency = round(rFrequency, 2)
    relativeFrequency[i] = rFrequency

    totalWord = 0
    canadaCount = 0
    f.close()

fc.close()

relativeFrequency = sorted(relativeFrequency.items(), key=lambda x: x[1], reverse=True)

with open("relativeFrequency.csv", "a") as rF:
    docValue = relativeFrequency[0][0]

    rF.write("Article number with highest relative frequency : " + " , " + str(docValue) + "\n")
    rF.write("Article #" + " , " + "Relative Frequency" + "\n")

    for r in relativeFrequency:
        rF.write(str(r[0]) + " , " + str(r[1]) + "\n")

    with open("news/News_" + str(docValue) + ".txt", "r") as maxFreq:
        print("Article number with the maximum relative frequency for word canada is : " + str(docValue) + "\n")
        print("Article content is as below " + "\n" + str(maxFreq.read()))
