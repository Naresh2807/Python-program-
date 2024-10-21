num=0
bot_1=0
bot_2=0
while num!=100:
    print("The total number==",num)
    bot_1=int(input("bot_1:Enter the number1: "))  
    while bot_1>10:
        if bot_1 not in [1,2,3,4,5,6,7,8,9,10]:
            print("Please enter number between 1 to 10")
            bot_1=int(input("bot_1:Enter the number1: "))

    num=num+bot_1
    print("bot_1 :the total  is",num)
    if num==100:  
        print("bot_1 the winner is bot_1",num)  
        break;

    bot_2=int(input("bot_2 :Enter the number2: ")) 
    while bot_2>10:
        if bot_2 not in [1,2,3,4,5,6,7,8,9,10]:
            print("bot_1 :Please enter number between 1 to 10")
            bot_2 = int(input("bot_2 :Enter the number2: "))
            
    num =num+bot_2 
    print("bot_2 :total is ",num)
    if num==100:  
        print("the winner is bot_2",num)  
        break;
    if num>100:
        break;
 
