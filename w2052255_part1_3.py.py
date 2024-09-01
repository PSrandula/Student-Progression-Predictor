import sys
import w2052255_part4
import os
#Valid credits volumes variables
valid_credits_volume = [0,20,40,60,80,100,120]
multiples = ['y','q']
GraphList = []

#Credits data store the list 
credits_data_list=[]
if os.path.exists("credits.txt"):
        os.remove("credits.txt")
        
def loop_code():
        while True:
                user_input = input("\nDo you want to enter passes again? (y/q) :").lower()
                if user_input == 'y':
                        staff()
                        continue
                elif user_input != 'q':
                        user_input = input("\nplease tell you want to enter passes again? (y/q) :").lower()
                        if user_input=='y':
                                staff()
                                continue
                        elif user_input=='q':
                                for data in credits_data_list:
                                        print(f"{data['outcome']} - {data['pass']}, {data['defer']}, {data['fail']}")
                                print (w2052255_part4.histogram(GraphList))
                                print("good bye")
                                sys.exit()
                elif user_input == 'q':
                        print (w2052255_part4.histogram(GraphList))
                        for data in credits_data_list:
                                print(f"{data['outcome']} - {data['pass']}, {data['defer']}, {data['fail']}")
                        print("good bye")
                        sys.exit()
                        
def conditions(pass_credits,defer_credits,fail_credits):
                #Check the outcome based on credits value       
        if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
                outcome = "Progress"
                
        elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0:
                outcome = "Progress(module trailer)"
                
        elif pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
                outcome = "Progress(module trailer)"
                
        elif pass_credits == 80 and defer_credits == 40 and fail_credits == 0:
                outcome = "Module retriever"
               
        elif pass_credits == 80 and defer_credits == 20 and fail_credits ==20:
                outcome = "Module retriever"
                
        elif pass_credits == 80 and defer_credits == 0 and fail_credits == 40:
                outcome = "Module retriever"
                
        elif pass_credits == 60 and defer_credits == 60 and fail_credits == 0:
                outcome = "Module retriever"
                
        elif pass_credits == 60 and defer_credits == 40 and fail_credits == 20:
                outcome = "Module retriever"
                
        elif pass_credits == 60 and defer_credits == 20 and fail_credits == 40:
                outcome = "Module retriever"
                
        elif pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
                outcome = "Module retriever"
                
        elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
                outcome = "Module retriever"
                
        elif pass_credits == 40 and defer_credits == 60 and fail_credits == 20:
                outcome = "Module retriever"
                
        elif pass_credits == 40 and defer_credits == 40 and fail_credits == 40:
                outcome = "Module retriever"
                
        elif pass_credits == 40 and defer_credits == 20 and fail_credits == 60:
                outcome = "Module retriever"
                
        elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80:
                outcome = "Exclude"
                
        elif pass_credits == 20 and defer_credits == 100 and fail_credits == 0:
                outcome = "Module retriever"
                
        elif pass_credits == 20 and defer_credits == 80 and fail_credits == 20:
                outcome = "Module retriever"
                
        elif pass_credits == 20 and defer_credits == 60 and fail_credits == 40:
                outcome = "Module retriever"
               
        elif pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
                outcome = "Module retriever"
                
        elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
                outcome = "Exclude"
                
        elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
                outcome = "Exclude"
                
        elif pass_credits == 0 and defer_credits == 120 and fail_credits == 0:
                outcome = "Module retriever"
                
        elif pass_credits == 0 and defer_credits == 100 and fail_credits == 20:
                outcome = "Module retriever"
                
        elif pass_credits == 0 and defer_credits == 80 and fail_credits == 40:
                outcome = "Module retriever"
                
        elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
                outcome = "Module retriever"
                
        elif pass_credits == 0 and defer_credits == 40 and fail_credits == 80:
                outcome = "Exclude"
                
        elif pass_credits == 0 and defer_credits == 20 and fail_credits == 100:
               outcome = "Exclude"
               
        elif pass_credits == 0 and defer_credits == 0 and fail_credits == 120:
               outcome = "Exclude"
        print(outcome)

        if version == "1":
                print("Thank You!")
                sys.exit()
        elif version == "2":                                    #Append the data to the credits data value
                GraphList.append(outcome)
                credits_data_list.append({'pass':pass_credits, 'defer':defer_credits,'fail':fail_credits, 'outcome':outcome})

        #Store the outcome data to a file
                filename="credits.txt"
                with open (filename,'a')as file:
                        file.write(f'pass :{pass_credits}\n')
                        file.write(f'defer :{defer_credits}\n')
                        file.write(f'fail :{fail_credits}\n')
                        file.write(f'{outcome}\n')
                        file.write(f'____________________________\n')
                        file.close()
def staff():
        try:
                #Get inputs for pass,defer and fail credits
                pass_credits=int(input("please enter the pass credits :"))
                if not pass_credits in valid_credits_volume:
                        print("Out of range")
                        loop_code()
                defer_credits=int(input("please enter the defer credits :"))
                if not defer_credits in valid_credits_volume:
                        print("Out of range")
                        loop_code()
                fail_credits=int(input("please enter the fail credits :"))   
                if not fail_credits in valid_credits_volume:
                        print("Out of range")
                        loop_code()
                #Check if total eqal to 120
                total_credits = pass_credits+defer_credits+fail_credits
                if total_credits != 120:
                        print("Total incorrect")
                        loop_code()
                                
        except ValueError:
                print("Integer Required!, please enter the integer only")
                loop_code()
        conditions(pass_credits,defer_credits,fail_credits)

def student():
        try:
                #Get inputs for pass,defer and fail credits
                pass_credits=int(input("please enter the pass credits :"))
                if not pass_credits in valid_credits_volume:
                        print("Out of range")
                        sys.exit()
                defer_credits=int(input("please enter the defer credits :"))
                if not defer_credits in valid_credits_volume:
                        print("Out of range")
                        sys.exit()
                fail_credits=int(input("please enter the fail credits :"))   
                if not fail_credits in valid_credits_volume:
                        print("Out of range")
                        sys.exit()
                #Check if total eqal to 120
                total_credits = pass_credits+defer_credits+fail_credits
                if total_credits != 120:
                        print("Total incorrect")
                        sys.exit()
                                
        except ValueError:
                print("Integer Required!, please enter the integer only")
                sys.exit()
        conditions(pass_credits,defer_credits,fail_credits)
        
while True:
        print("Student: 1 | Staff: 2 ")
        version = input("Enter the 1 or 2: ")
        if version == "1":
             student()
        elif version == "2":
                staff()
                loop_code()
                
        
        


