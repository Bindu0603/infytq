######1111####
def find_product(num1,num2,num3):
    l=[num1,num2,num3]
    product=1
    product2=1
    for i in range(0,len(l)):
        if l[i]==7:
            p=l[(i+1):]
            for k in range(0,len(p)):
                product*=p[k]
            break
        else:
            product2*=l[i]
    if product==1:
        if 7 not in l:
            return product2
        else:
            return "-1"
    else:
        return product

product=find_product(7,6,2)
print(product)
#######222222######
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if num1<(num2+num3):
        a=1
    else:
        a=0
    if num2<(num1+num3):
        b=1
    else:
        b=0
    if num3<(num1+num2):
        c=1
    else:
        c=0
    if (a and b and c):
        return success
    else:
        return failure

    ########3333333#######
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=no_of_five
    s=rupees_to_make-no_of_five*5
    r=s/1
    if s==0:
        five_needed=no_of_five
        one_needed=0
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    elsif r=int(r) and r<=no_of_one:
        one_needed=r
        five_needed=no_of_five
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
