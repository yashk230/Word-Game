#!/usr/bin/env python
# coding: utf-8

# In[1]:


letters = [['h','o','l','i','d','a','y'],

        ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm','i','n','g'],

        ['b','o','o','t','c','a','m','p'],

        ['f','l','o','w','c','h','a','r','t'],

        ['w', 'o', 'r', 'd', 's', 'c', 'a','p','e','s']]


words = [["hi","hay","day","had","lay","dal","lad","lid","hold","lady","hail"],

        ["go","an","in","no","on","map","mom","gap","gag","pig","man","ping",

        "pong","pram","prom","ramp","pro","gram"],

        ["am","at","to","cab","cap","cob","cop","map","mop","act","bat","camp",

        "comb","boom","pact","atom","boot","cat"],

        ["of","at","or","to","caw","cow","how","who","calf","claw","flaw","flow",

        "fowl","wolf","crow","half","chart"],

        ["we","do","as","cap","caw","cop","cow","paw","cod","dew","pad","cape",

        "cope","crap","crew","crop","pace"]]

lives=5 # this stand for no.of chances

level=0 # no of levels

score=0 # score of user

while level<5:
    print(f'welcome to level{level+1}')
    print('Create three meaningfull words from the given characters')
    for i in letters[level]:
        print(i,end="") # for showing
    print()
    wordcount=0
    match=False
    word=''
    oldword=[]
    while wordcount==0 or wordcount<3:
        match=False
        word=input("")
        if word.lower() not in oldword:
            for i in words[level]:
                if word==i:
                    match=True
                    wordcount=wordcount+1
                    score=score+1
                    oldword.append(word)
                    break
        if not match:
            print('Wrong guess')
            lives=lives-1
        if lives==0:
            print('Game over better luck next time')
            print('Your score is ',score)
            break
    wordcount=0
    match=False
    word=''
    oldword=[]
        
    if lives==0:
        break
    if level==4:
        print("Thank you for playing the game")
        print("Your score is ",score)
        level=level+1
    else:
        choice=input('Do you want t continue to the next level (y/n):')
        if choice.lower()=='y':
            level+=1
        else:
            print('Thank you for playing the game')
            print('Your score is',score)
            break