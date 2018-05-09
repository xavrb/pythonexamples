def askAndCalculateAge():
    n = input("Give me a number!\n")
    age = input("Whats your age, fam?\n") 
    for x in range(int(n)):
        print("Time: {0} \tOh, man! In 100 years you'll be {1}".format(x,int(age)+100))
    return 0






askAndCalculateAge()
