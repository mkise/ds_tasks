import math
#To give the user a summary of what they are about to do.

intro = 'Welcome to your finacial calculator. You have a choice between an investment and a home loan repayment calculator as defined below\n'

choice_info ='Investment - to calculate the amount of interest you\'ll have to earn on your investment\n'
choice_info2 ='Bond -to calculate the amount you\'ll have to pay on a home loan\n'


choice ='investment'
choice_1 ='bond'

print(intro)
print(choice_info)
print(choice_info2)

user_choice = input('Please enter which calculator you want to use, investment or bond:\n')

if user_choice.lower() == choice:
    
    amount= float(input('Enter the amount of money you want to invest:\n'))
    rate = int(input('Enter the interest rate % you want to gain:\n'))
    years= int(input('Enter the amount of years you plan to invest:\n'))
   
    interest = 'simple'
    interest2 = 'compound'
    user_interest= input('Enter whether you would be interested in \'simple\' or \'compound\' interest:\n')
    
    p= amount
    t= years
    r=rate/100
    sim_interest = p*(1+r*t)
    comp_interest =p*math.pow((1+r),t)
    
    if user_interest.lower()==interest :
     #interest Formula:
     # Simple interest A=p*(1+r*t)
    
        print(f'Simple Interest return for your £ {amount} investment after  {years} years will be:\n £  {round(sim_interest,2)}')

    #Compound interest formula
    #A=p*math.pow((1+r),t)
    
    
    elif user_interest.lower() == interest2:
       print(f'Compound Interest return for your £ {amount}  investment after {years} years will be: £ {round(comp_interest,2)}')


elif user_choice.lower()==choice_1:

    house_price =float(input('Enter the present value of the house: \n'))
    yearly_interest_rate=int(input('Enter the interest rate: \n'))
    time=int(input('Enter the amount months you want to repay: \n')) 

    #Bond repayment formular =(i*P)/(1-(1+i)**(n))
    i=(yearly_interest_rate/12)/100
    p=house_price
    n=time
    bond_rep= (i*p)/(1-(1+i)**(-n))
    
    print(f'Your Bond repayment on a home loan each month will be £ +{round(bond_rep,2)}')

#print this statement if the user input  selection is neither 'investmennt or bond '.
else:
    print('Invalid choice')
