import _1welc , _2topic ,_3physic , _4maths , _5python , _6html

_1welc.main()
a=input("press enter to select topic")

m=0
while m != 5:
    _2topic.topic()
    try :
        m=int(input("Enter your choice between 1 to 5 only ::>> "))
    except:
        pass
    if m==1:
        _3physic.ph()
    elif m==2:
        _4maths.mat()
    elif m==3:
        _5python.py()
    elif m==4:
        _6html.ht()
    elif m==5:
        print("thank you")

    
     
    
