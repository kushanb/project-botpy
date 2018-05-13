print("WELCOME TO CHATBOT")
x=str(input("Press enter to start"))
while x!="end":
    x=str(input("Enter question: "))
    count=0 #to get the count of matching words
    q1=x.upper().split() #used to convert the asked question to capital and list
    char=".,?" #contains the punctuation marks
    for ch in char: #to go through the punctuation marks
        if (q1[-1][-1]) == ch: #checking if the last word contains a punctuation
            q1[-1]=q1[-1].replace(q1[-1][-1],"") #removing the last char if its a punctuation
#print(q1)    #just for testing


    answers=open(q1[0].lower()+".txt","r") #accessing the notepad file that stores the questions
    lines=answers.readlines() #reads the lines in the file

    endLoop= False #
    for line in lines: #goes through every line
        count=0 #creating variable to count matching words
        answer=line.strip().split("|") #seperates into sections from each | sign
        for word in q1: #going through the words in the asked question
            question=answer[1].split() #index [1] has the question that I stored in the txt file
            #print (question) #finished testing with this so made it a comment
            for i in question: #going through the words in the question in the txt file
                #print(i) #commented after testing
                if i==word: #checking if the word match
                    count+=1 #increasing the counter everytime a word matches
                    #print(count,word) #commented after testing
                    if count==len(question): #checks if the number of words in the q in the txt is equal to the word count of the input
                        print ("BOT: ",answer[3].strip()) #prints the answer. strip removes the whitespace in front and back
                        endLoop= True      
        if endLoop== True:
            break
        else: #if the word count isn't equal it checks keywords
            if count!=len(question):
                keys=answer[2].strip().split(",") #extracting the keywords
                #print("keys: ", keys)
                for word in q1:
                    #print("word: ", word)
                    for key in keys:
                        key=key.strip()
                        #print(key)
                        if word==key: #if a keyword is there in the question it still prints
                            print("BOT: ",answer[3].strip())
                            endLoop= True
                if endLoop==True:
                    break

