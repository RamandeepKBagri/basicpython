#calculate the pay


def calculateThePay(hours,regularpay):
    if (hours<=40):
        pay=hours*regularpay
    elif(hours<=60):
        pay=40*regularpay+((hours-40)*regularpay*1.5)
    else:
        pay=40*regularpay+((60-40)*regularpay*1.5)+((hours-60)*regularpay*2)
    return pay

pay1=calculateThePay(20,30)
print('your pay is',pay1)

pay2=calculateThePay(50,15.5)
print('Your Pay is',pay2)

pay3=calculateThePay(70.25,11)
print('your pay is',pay3)

userhours=input('How many hours did you work')
userhours=float(userhours)
userregularpay=input('How much is regular pay')
userregularpay=float(userregularpay)
print('your pay is',calculateThePay(userhours,userregularpay))
