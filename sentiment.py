

# ------------- Positive / Negative dictionaries ------------ #

postiveCounter = {}
negativeCounter = {}
with open("positiveWords.txt", 'r') as positive, open("negativeWords.txt", 'r') as negative:
    pWords = positive.read().split("\n")
    nWords = negative.read().split("\n")

    for word in pWords:
        postiveCounter[word] = 0

    for word in nWords:
        negativeCounter[word] = 0

# -------------------------- END ---------------------------- #

# --------------------- main logic --------------------------- #

fOut = open("sentimentOutput.csv", "a")
fOut.write("TWEET #" + " , " + "MESSAGE" + " , " + "MATCH" + " , " + "POLARITY" + "\n")

bowList = []
for i in range(1,2664):

    f = open("tweets/file_" + str(i) + ".txt", 'r')
    bow = {}
    negativePolarity = 0
    positivePolarity = 0
    polarity = ""
    matchingList = []

    data = f.read()
    lines = data.split("\n")
    for line in lines:
        words = line.split(" ")
        for word in words:

            if (bow.keys().__contains__(word)):
                bow["word"] = bow["word"] + 1
            else:
                bow["word"] = 1

            if (postiveCounter.keys().__contains__(word)):
                positivePolarity += 1
                postiveCounter[word] += 1
                matchingList.append(word)

            if (negativeCounter.keys().__contains__(word)):
                negativePolarity += 1
                negativeCounter[word] += 1
                matchingList.append(word)

    bowList.append(bow)

    if positivePolarity > negativePolarity:
        polarity = "Positive"

    if negativePolarity > positivePolarity:
        polarity = "Negative"

    if positivePolarity == negativePolarity:
        polarity = "Neutral"

    if len(matchingList) == 0:
        polarity = "Neutral"
        matchingList.append("No Match")

    fOut.write(str(i) + " , " + str(data) + " , ")
    for lst in matchingList:
        if(len(matchingList) > 1):
            fOut.write(lst + " | ")
        else:
            fOut.write(lst)
    fOut.write(", " + polarity + " \n")

    f.close()
fOut.close()


counter = 1
with open("bagOfWords.txt", "a") as f:

    for bag in bowList:
        f.write("Tweet# " + str(counter) + "\n")
        for key,value in bag.items():
            f.write(str(key) + " : " + str(value) + " , ")
        f.write("\n\n")
        counter += 1

with open("postiveWordsCount.csv", "a") as f:

    for key,value in postiveCounter.items():
        if(value > 0):
            f.write(key + " , " + str(value))
            f.write("\n")

with open("negativeWordsCount.csv", "a") as f:
    for key, value in negativeCounter.items():
        if(value > 0):
            f.write(key + " , " + str(value))
            f.write("\n")

with open("polarityCount.csv", "a") as p:
    for key,value in postiveCounter.items():
        if(value > 0):
            p.write(key + " , " + str(value) + " , " + "positive")
            p.write("\n")

    for key, value in negativeCounter.items():
        if(value > 0):
            p.write(key + " , " + str(value) + " , " + "negative")
            p.write("\n")

# ------------------------------ END --------------------------------- #
