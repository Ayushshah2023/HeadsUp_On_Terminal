import random
def HeadsUp():
    easy=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    medium=[15,17,18,16,19,20,21,22,23,24,25,26,27,28,29]
    tough=[30,31,32,33,34,35,36]
    #Always see to it that the format for dictionary remains constant
    #here order-> {serial no:{Clue:Correct_ans:Difficulty}}
    #order will help in telling what to do will asking random orders*
    #To do list- Final Count and then mark them accordingly , work on tough and medium then code for medium and tough and then go onto further subjects like football ek aur random laga do warna pehle 6 easy and then 3 med and last tough and also remove the already traversed from the list
    main_table={1:{'Clue':'I know','Correct_ans':'Monica','Diff':'E'},2:{'Clue':'Moo\'s point','Correct_ans':'Joey','Diff':'E'},3:{'Clue':'You can\'t have S-E-X in front of the B-A-B-I-E','Correct_ans':'Joey','Diff':'E'},4:{'Clue':'Over the Line.. ,You are way so past the line that the line is a dot for you','Correct_ans':'Joey','Diff':'E'},5:{'Clue':'Homosapiens are people,….. I am not Judging them','Correct_ans':'Joey','Diff':'E'},6:{'Clue':'Well the fridge broke, so I had to eat everything','Correct_ans':'Joey','Diff':'E'},7:{'Clue':'Lobster','Correct_ans':'Phoebe','Diff':'E'},8:{'Clue':'I am not even Sorry','Correct_ans':'Joey','Diff':'E'},9:{'Clue':'Unagi','Correct_ans':'Ross','Diff':'E'},10:{'Clue':'Seven','Correct_ans':'Monica','Diff':'E'},11:{'Clue':'Pivot','Correct_ans':'Ross','Diff':'E'},12:{'Clue':'Could I be Wearing any more clothes','Correct_ans':'Chandler','Diff':'E'},13:{'Clue':'We were on a break','Correct_ans':'Ross','Diff':'E'},14:{'Clue':'How you Doin?','Correct_ans':'Joey','Diff':'E'},15:{'Clue':'Holiday  Armadillo','Correct_ans':'Ross','Diff':'M'},16:{'Clue':'Yemen','Correct_ans':'Chandler','Diff':'M'},17:{'Clue':'Apothecary','Correct_ans':'Rachel','Diff':'M'},18:{'Clue':'Huggsy','Correct_ans':'Joey','Diff':'M'},19:{'Clue':'Nooooooo','Correct_ans':'Monica','Diff':'M'},20:{'Clue':'My eyes','Correct_ans':'Phoebe','Diff':'M'},21:{'Clue':'Phalange','Correct_ans':'Phoebe','Diff':'M'},22:{'Clue':'Thursday-Third day of the week','Correct_ans':'Joey','Diff':'M'},23:{'Clue':'That is Brand New Infromation','Correct_ans':'Phoebe','Diff':'M'},24:{'Clue':'Sorry did my back hurt your knife','Correct_ans':'Rachel','Diff':'M'},25:{'Clue':'He is so preety, I wan\'t to cry','Correct_ans':'Rachel','Diff':'M'},26:{'Clue':'It\'s not what you said, It\'s the way you said it','Correct_ans':'Joey','Diff':'M'},27:{'Clue':'Occupation: ….. Dinasours','Correct_ans':'Joey','Diff':'M'},28:{'Clue':'I am Curvy and I like it','Correct_ans':'Joey','Diff':'M'},29:{'Clue':'Transponster','Correct_ans':'Rachel','Diff':'M'},30:{'Clue':'Vafanopoli','Correct_ans':'Joey','Diff':'T'},31:{'Clue':'Come on Ross, you’re a paleontologist, dig a little deeper.','Correct_ans':'Phoebe','Diff':'T'},32:{'Clue':'Paper…snow…..a ghost','Correct_ans':'Joey','Diff':'T'},33:{'Clue':'Well Maybe I don’t need your money,… I said Maybe','Correct_ans':'Rachel','Diff':'T'},34:{'Clue':'Salmon Skin Roll','Correct_ans':'Rachel','Diff':'T'},35:{'Clue':'I am A Human Doodle','Correct_ans':'Rachel','Diff':'T'},36:{'Clue':'Sup With The Wack Playstation Sup','Correct_ans':'Joey','Diff':'T'}}
    print("Here std instructions")
    print("Enter the Name of the character as Joey or Chandler i.e. first letter capital")
    print("Tell me various topics over which you want me cover "+"  mail it to avengers1999@gmail.com")
    level=str(input("Enter the level for the test, Enter e for easy, m for medium, t for tough:     "))
    print(level)

    #Idhar Easy Level Starts
    if(level=='e'):
        Temp_easy=easy
        Temp_medium=medium
        Temp_tough=tough
        final_count_e=0
        count_easy=6
        count_mid=3
        count_tough=1
        while(count_easy> 0):
            count=1
            k=int(random.choice(Temp_easy))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_easy.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_e=final_count_e+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_e))
                    break
                else:
                    count=count+1
                    final_count_e=final_count_e+1
            count_easy=count_easy-1
            

        while(count_mid> 0):
            count=1
            k=int(random.choice(Temp_medium))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_medium.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_e=final_count_e+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_e))
                    break
                else:
                    count=count+1
                    final_count_e=final_count_e+1
            count_mid=count_mid-1

        while(count_tough> 0):
            count=1
            k=int(random.choice(Temp_tough))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_tough.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_e=final_count_e+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_e))
                    break
                else:
                    count=count+1
                    final_count_e=final_count_e+1
            count_tough=count_tough-1
        if(final_count_e<=12):
            print("You have done very well---->Inshallah the boys played well")
            print("You should try the medium and tough level")
        '''q=str(input("IF you want to continue to tougher levels then press y"))
        if(q=='y'):
            level=str(input("Enter rhe level for the test, Enter m for medium, t for tough"))
    if(final_count_e>12):
        print("Inshallah the boys played well but we lacked the flair to proceed")'''

    #Idhar medium Level Starts
    if(level=='m'):
        Temp_medium=medium
        Temp_tough=tough
        Temp_easy=easy
        final_count_m=0
        count_easy=2
        count_mid=5
        count_tough=3
        while(count_easy> 0):
            count=1
            k=int(random.choice(Temp_easy))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_easy.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_m=final_count_m+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_m))
                    break
                else:
                    count=count+1
                    final_count_m=final_count_m+1
            count_easy=count_easy-1

        while(count_mid> 0):
            count=1
            k=int(random.choice(medium))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_medium.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_m=final_count_m+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_m))
                    break
                else:
                    count=count+1
                    final_count_m=final_count_m+1
            count_mid=count_mid-1

        while(count_tough> 0):
            count=1
            k=int(random.choice(tough))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_tough.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_m=final_count_m+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_m))
                    break
                else:
                    count=count+1
                    final_count_m=final_count_m+1
            count_tough=count_tough-1
        if(final_count_m<12):
            print("You have done very well---->Inshallah the boys played well")
            print("You should try the tough level")
        '''q=str(input("IF you want to continue to tougher levels then press y"))
        if(q=='y'):
            level=str(input("Enter rhe level for the test, Enter t for tough"))
    if(final_count_m>12):
        print("Inshallah the boys played well but we lacked the flair to proceed")'''


    #Idhar Tough Level Starts
    if(level=='t'):
        rand_choose=0
        Temp_easy=easy
        Temp_medium=medium
        Temp_tough=tough
        final_count_t=0
        count_easy=2
        count_mid=4
        count_tough=4
        while(count_easy> 0):
            count=1
            k=int(random.choice(Temp_easy))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_easy.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_t=final_count_t+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_t))
                    break
                else:
                    count=count+1
                    final_count_t=final_count_t+1
            count_easy=count_easy-1


        while(count_mid> 0):
            count=1
            k=int(random.choice(Temp_medium))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_medium.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_t=final_count_t+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_t))
                    break
                else:
                    count=count+1
                    final_count_t=final_count_t+1
            count_mid=count_mid-1


        while(count_tough> 0):
            count=1
            k=int(random.choice(Temp_tough))
            #prints here are to check the functionality of the code
            print(k)
            print(main_table[k]['Clue'])
            Temp_tough.remove(k)
            while(count>0):
                user_data=str(input("Enter what you think is the correct_Ans"))
                #here print is just to check the functionality of hte case
                #print(user_data==main_table[k]['Correct_ans'])
                if(user_data==main_table[k]['Correct_ans']):
                    final_count_t=final_count_t+1
                    print("Correct ans in "+str(count)+" guesses"+"                 "+str(final_count_t))
                    break
                else:
                    count=count+1
                    final_count_t=final_count_t+1
            count_tough=count_tough-1
        if(final_count_t<12):
            print("Kindly contact Hollywood to collect oyur prize")
            print("You have done very well---->Inshallah the boys played well")
    '''    
    if(final_count_t>12):
        print("Inshallah the boys played well but we lacked the flair to proceed to the final level")'''
    
print(HeadsUp())
            
