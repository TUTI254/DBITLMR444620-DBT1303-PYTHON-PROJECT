loopy =1
print("Traffic Control simulation project")
while True: 
    #if loopy ==1:
        print("Input signal to run program:")
        print("Input red for : STOP")
        print("Input amber for : GET READY")
        print("Input green for : GO")
        print("Input exit for : TERMINATION OF PROGRAMME ")
        print("------------------------------------------")
    #else:
        print("Input signal run program  :")
        print("-------------------------------")
        signal = input()
        if signal == "red":
            print("Color = RED")
            print("stop behind the line")
            print("Next 60 seconds")
            print("----------------------------")
        elif signal == "amber":
            print("Color = AMBER")
            print("Get ready")
            print("Next 60 seconds")
            print("----------------------------")
        elif signal == "green":
            print("Color = GREEN")
            print("GO, DRIVE ON!!")
            print("Next 60 seconds")
            print("----------------------------")
        elif signal == "exit":
            print(" you choose to Terminate programme.")
            print("-----------------------------------")
            break
        else:
            print(" PLEASE INSERT THE CORRECT SIGNAL TO RESPOND!!! (red, amber, green and exit) ONLY!!!!!!")
            print("---------------------------------------------------------------------------------------")
            
            
        #if not(signal != "exit"): break   #Exit loop
        #    print("END SIMULATION PROGRAMME") */