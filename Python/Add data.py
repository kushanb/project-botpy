#Adding questions form

print("Cutting Edge Chatbot\nAdding new questions to chatbot\n")
print("\u00a9 Kushan Bhareti 2018\n\n")

question=""
while question!="end":
    data=""
    typ=""

    question= str(input("Enter question: "))

    qst= question.upper().split() #capitalising and splitting q by words
    qstn= qst[0].strip() #taking first word
    print(qstn)

    #selecting the type of question
    if qstn=="WHO":
        db=open("who.txt","a")
        dbo=open("who.txt","r")
        typ="who"
    elif qstn=="WHY":
        db=open("why.txt","a")
        dbo=open("why.txt","r")
        typ="why"
    elif qstn=="WHEN":
        db=open("when.txt","a")
        dbo=open("when.txt","r")
        typ="when"
    elif qstn=="WHERE":
        db=open("where.txt","a")
        dbo=open("where.txt","r")
        typ="where"
    elif qstn=="WHAT":
        db=open("what.txt","a")
        dbo=open("what.txt","r")
        typ="what"
    elif qstn=="HOW":
        db=open("how.txt","a")
        dbo=open("how.txt","r")
        typ="how"
    elif qstn=="CAN":
        db=open("can.txt","a")
        dbo=open("can.txt","r")
        typ="can"
    else:
        print("Only WHO, WHY, WHEN, WHERE, WHAT, HOW & CAN questions allowed")
        continue

    #getting other inputs
    keys= str(input("Enter Keywords: (Seperate using commas)\n\t~ "))
    ans=str(input("Enter the answer: "))
    if ans[-1][-1]==".":
        ans[-1]=ans[-1].replace(ans[-1],"")

    #setting the number for the question
    nums= dbo.readlines()
    endNum= nums[-1][0]
    number= str(int(endNum)+1)
    print(number)

    #remove question mark from question
    if qst[-1][-1]=="?":
        qst[-1]=qst[-1].replace(qst[-1][-1],"")

    last=len(qst[-1])
    question=question[:-(last+1)]+qst[-1]
    
    #entering data to the database
    data= number+" | "+question.upper()+ " | "+ keys.upper()+" | " +ans[0].upper()+ans[1:]+"."
    db.write(str(data)+"\n")
    dbo.close()
    db.close()

    print("Success\n")
