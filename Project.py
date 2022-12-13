#THE TRIO ICE CREAM PARLOUR

#ADD PRODUCT
def add():
    
    import pickle
    f=open("product.dat","ab")
    ans=1
    
    while (ans!=0):
        
        rec=[]
        pid=int(input("Enter PRODUCT ID :"))
        rec.append(pid)
        name=input("Enter PRODUCT NAME :")
        rec.append(name)
        price=float(input("Enter PRICE :"))
        rec.append(price)
        qty=int(input("Enter QUANTITY : "))
        rec.append(qty)
        pickle.dump(rec,f)
        ans=int(input("Do you want to enter more? (0 for NO and 1 for YES) :"))
    
    f.close()
    
#LIST OF PRODUCTS
    
def display():
    import pickle
    f=open("product.dat","rb")
    
    class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
        
    print(color.BLUE+ color.BOLD+"\n\n\t\t\t\tLIST OF PRODUCTS ")
    print("*************************************************************************************************\n\n")
    print(color.RED+ color.BOLD+"{}\t\t{}\t\t\t\t{}\t\t\t{}".format('PROD ID.','PROD.NAME','PRICE','QUANTITY')+color.END)
    print("________________________________________________________________________________________________")
    print(color.BOLD)
    
    
    try:
        while True:
            y=pickle.load(f)
            print("\n{}\t\t\t{}\t\t\t\t{}\t\t\t{}".format(y[0],y[1],y[2],y[3]))
            
    
    except EOFError:
        pass
    b=input()
    f.close()


#DELETE PRODUCT
def deleteproduct():
    
    import pickle
    rf=open("product.dat","rb")
    wf=open("temp.dat","wb")

    r=int(input("Enter the PRODUCT ID of the product you want to delete :"))
    f=0
    
    try:
        while True:
            y=pickle.load(rf)
            
            if(y[0]!=r):
                pickle.dump(y,wf)
            else:
                f=1
        
    except EOFError:
        pass
    rf.close()
    wf.close()
    wf=open("product.dat","wb")
    rf=open("temp.dat","rb")
    
    try:
        while True:
            y=pickle.load(rf)
            pickle.dump(y,wf)
        
    except EOFError:
        pass
    wf.close()
    rf.close()
    
    if(f==0):
        print("\n\n\t\t THIS ID DOSEN'T EXIST !!!!!!")
    else:
        print("\n\n\t\t THE PRODUCT IS DELETED!!!!!")
        ans=int(input("Do you want to enter more? (0 for NO and 1 for YES) :"))
    B=input()
    
    wf.close()

#MODIFY PRODUCT
def modify():
    
    import pickle
    rf=open("product.dat","rb")
    wf=open("temp.dat","wb")

    r=int(input("Enter the PRODUCT ID of the product you want to modify:"))
    f=0
    
    try:
        while True:
            y=pickle.load(rf)
            
            if(y[0]!=r):
                pickle.dump(y,wf)
            else:
                f=1
                print("\n\nENTER NEW DETAILS :\n\n")
                rec=[]
                pid = int(input("Enter PRODUCT ID :"))
                rec.append(pid)
                name=input("Enter PRODUCT NAME :")
                rec.append(name)
                price=float(input("Enter PRICE :"))
                rec.append(price)
                qty=int(input("Enter QUANTITY :"))
                rec.append(qty)
                pickle.dump(rec,wf)
    
    except EOFError:
        pass
    rf.close()
    wf.close()
    wf=open("product.dat","wb")
    rf=open("temp.dat","rb")
    
    try:
        while True:
            y=pickle.load(rf)
            pickle.dump(y,wf)
        
    except EOFError:
        pass
    wf.close()
    rf.close()
    
    if(f==0):
        print("\n\n \t\t THIS ID DOSEN'T EXIST !!!!!!")
    else:
        print("\n\n\t\t THE PRODUCT IS MODIFIED!!!!! ")
    
    B=input()
    rf.close()

#ADD QUANTITY
def qty():
    
    import pickle
    rf=open("product.dat","rb")
    wf=open("temp.dat","wb")

    r=int(input("\n\nEnter the PRODUCT ID of the product of which you want to add quantity :"))
    f=0
    
    try:
        while True:
            y=pickle.load(rf)
            if(y[0]!=r):
                pickle.dump(y,wf)
            else:
                f=1
                q=int(input("\n\nEnter the new quantity entered in the shop :"))
                y[3]=y[3]+q
                pickle.dump(y,wf)
    
    except EOFError:
        pass
    rf.close()
    wf.close()
    wf=open("product.dat","wb")
    rf=open("temp.dat","rb")
    
    try:
        while True:
            y=pickle.load(rf)
            pickle.dump(y,wf)
        
    except EOFError:
        pass
    wf.close()
    rf.close()
    
    if(f==0):
        print("\n\n \t\t THIS ID DOSEN'T EXIST !!!!!!")
    else:
        print("\n\n\t\t THE PRODUCT IS MODIFIED!!!!! ")
    
    B=input()
    rf.close()

#DISPLAY MENU 
def menu():
    
    import pickle
    f=open("product.dat","rb")
    
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        
    print(color.BLUE+ color.BOLD+"\n\n\t\t\t\tMENU ")
    print("*********************************************************************\n\n")
    print(color.RED+ color.BOLD+"{}\t{}\t{}".format('SNo.','ICE CREAM FLAVOR','PRICE')+color.END)
    print("_____________________________________________________________________")
    print(color.BOLD)
    
    
    #Price
    a=850
    b=300
    c=500
    d=350
    e=600
    f=450
    g=550
    h=650
    i=700
    j=750
    k=800
    l=380
    m=900

    
    #Menu code
    print("1      ","Vanilla                  ",b)
    print("2      ","Strawberry               ",d)
    print("3      ","Butterscotch             ",l)
    print("4      ","Chocolate                ",f)
    print("5      ","Tutti Frooty             ",c)
    print("6      ","Oreo                     ",d)
    print("7      ","Chocochip                ",e)
    print("8      ","Red velevet              ",h)
    print("9      ","Rainbow sherbet          ",j)
    print("10     ","Caramel                  ",f)
    print("11     ","Belgium chocochip        ",k)
    print("12     ","Frappuccino              ",a)
    print("13     ","Mint chocochip           ",d)
    print("14     ","Cookie dough             ",e)
    print("15     ","Cookies and creme        ",m)
    print("16     ","Mango                    ",b)
    print("17     ","Cotton candy             ",c)
    print("18     ","Green Tea                ",j)
    print("19     ","Choco almond             ",e)
    print("20     ","Irish coffee             ",m)
    print("21     ","Peanut butter            ",c)
    print("22     ","Nutella                  ",k)
    print("23     ","Kaju Kishmish            ",e)
    print("24     ","Black currant            ",g)
    print("25     ","Coffee walnut fudge      ",a)
    print("26     ","Fruit overloaded         ",m)
    print("27     ","Hide n seek              ",e)
    print("28     ","Cassata                  ",k)
    print("29     ","Brownie                  ",i)
    print("30     ","Hazelnut                 ",e)
    

#PLACE ORDER & GENERATE BILL
def bill():
    
    import pickle
    rf=open("product.dat","rb")
    wf=open("temp.dat","wb")
    
    #Values
    a=850
    b=300
    c=500
    d=350
    e=600
    f=450
    g=550
    h=650
    i=700
    j=750
    k=800
    l=380
    m=900


    z=0
    x=1
    while x!=0:
        o=int(input("Enter your choice:"))


#VANILLA ICECREAM
        if o==1:
            bill=b
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)
    

#SRAWBERRY ICECREAM
        if o==2:
            bill=d
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#BUTTERSCOTCH ICECREAM
        if o==3:
            bill=l
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#CHOCOLATE ICECREAM
        if o==4:
            bill=f
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#TUTTI FROOTY ICECREAM   
        if o==5:
            bill=c
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#OREO ICECREAM
        if o==6:
            bill=d
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#CHOCOCHIP ICECREAM
        if o==7:
            bill=e
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#RED VELVET ICECREAM
        if o==8:
            bill=h
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#RAINBOW SHERBET ICECREAM
        if o==9:
            bill=j
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#CARAMEL ICECREAM
        if o==10:
            bill=f
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#BELGIUM CHOCOCHIP ICECREAM
        if o==11:
            bill=k
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#FRAPPUCCINO ICECREAM
        if o==12:
            bill=a
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#MINT CHOCOCHIP ICECREAM
        if o==13:
            bill=d
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#COOKIE DOUGH ICECREAM
        if o==14:
            bill=e
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#COOKIES AND CREME ICECREAM
        if o==15:
            bill=m
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#MANGO ICECREAM
        if o==16:
            bill=b
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#COTTON CANDY ICECREAM
        if o==17:
            bill=c
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#GREEN TEA ICECREAM
        if o==18:
            bill=j
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#CHOCO ALMOND ICECREAM
        if o==19:
            bill=a
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#IRISH COFFEE ICECREAM
        if o==20:
            bill=m
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#PEANUT BUTTER ICECREAM
        if o==21:
            bill=c
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#NUTELLA ICECREAM
        if o==22:
            bill=k
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#KAJU KISHMISH ICECREAM
        if o==23:
            bill=e
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#BLACK CURRANT ICECREAM
        if o==24:
            bill=g
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#COFFE WALNUT FUDGE ICECREAM
        if o==25:
            bill=a
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#FRUIT OVERLOADED ICECREAM
        if o==26:
            bill=m
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#HIDE N SEEK ICECREAM
        if o==27:
            bill=e
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#CASSATA ICECREAM
        if o==28:
            bill=k
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#BROWNIE ICECREAM
        if o==29:
            bill=i
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)


#HAZELNUT ICECREAM
        if o==30:
            bill=e
            print("\n\nYour order amount=",bill)
            print("gst=",0.02*bill)
            print("\nYour total bill=",(0.02*bill)+bill)

        
        
        print("\nDo you want more scoops ?")
        x=int(input("0 for NO 1 for YES:"))
        z=z+bill
    print("\nFinal bill=",(0.02*z)+z)
        
    B=input()
    rf.close()


while True :
    print("\n\n\n\t\tWELCOME TO THE TRIO ICE CREAM PARLOUR!!")
    print("******************************************************************")
    print()
    print()
    print("1.\t Administrator\n2. \t Customer\n3.\t Exit\n\n")
    
    ch=int(input("\n\n\tEnter your choice :  "))
    
    if(ch==1):
        
        ans=1
        while (ans!=0):
            
            print("\n\n\n\t\tWELCOME ADMININSTRATOR !!!!!!!!!!!!\n\n\n")
            print("\t\t 1. ADD A NEW PRODUCT\n\t\t 2. DELETE A PRODUCT\n\t\t 3. MODIFY A PRODUCT \n\t\t 4. ADD NEW QUANTITIES \n\t\t 5. LIST OF ALL THE PRODUCTS \n\t\t 6. exit")
            
            ach=int(input("\n\n Enter your choice :"))
            
            if (ach==1):
                add()
            elif(ach==2):
                deleteproduct()
            elif(ach==3):
                modify()
            elif(ach==4):
                qty()
            elif(ach==5):
                display()
            elif(ach==6):
                break
          
    
    if (ch==2):
        
        ans=2
        while(ans!=0):
            
            print("\n\n\n\t\tWELCOME CUSTOMER !!!!!!!!!!!!\n\n\n")
            print("\t\t 1. DISPLAY MENU\n\t\t 2. PLACE ORDER & GENERATE BILL\n\t\t 3. EXIT")
            
            ach=int(input("\n\n Enter your choice :"))
            
            if(ach==1):
                menu()
            elif(ach==2):
                bill()
            elif(ach==3):
                break
            
    
    if ch==3:
        break
    
    
    else:
        
        print("\n\n\n YOU HAVE ENTERED A WRONG CHOICE!!")
        b=input()

