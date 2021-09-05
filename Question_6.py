# Question 6
# Festival budget for 2000 is announced INR 10000/- and every year it will increase by 10%. write a recursive function to calculate total festival expense till 2020.

def fes(year,budget):
    if year == 2020:
        return budget
    else:
        year +=1
        return fes(year,budget + 10)
    
print(fes(2000,10000))



