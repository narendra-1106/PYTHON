question=[["Which language was used to create instagram ?" , "Python" , "java", "java script" , "C++" , "none" , 4] ,
["Which language was used to create instagram" , "Python" , "java", "java script" , "C++" , "none" , 4],
["Which language was used to create instagram" , "Python" , "java", "java script" , "C++" , "none" , 4],
["Which language was used to create instagram" , "Python" , "java", "java script" , "C++" , "none" , 4],
]

levels= [1000, 2000, 5000, 10000, 20000, 40000,80000, 160000, 320000]
money= 0

i=0
for i in range (0, len(question)):
    question=question[i]
    print(f"question for RS.{levels[i]}")
    print(f"a.{question[1]}  b.{question[2]} ")
    print(f"c.{question[3]}  d.{question[4]} ")
    reply=("Enter your ans (1-4)")
    if(reply== question[-1]):
        print(f"Correct ans , you won RS.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=32000

    else:
        print("Wrong ans")
        break
