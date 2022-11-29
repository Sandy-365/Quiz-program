import random, _score
def mat():
    def m():
        print("""


                                             #   #   ###   #####  #   #   ####         ###    #   #  #####   ####   #####  #####   ###   #   #
                                             ## ##  #   #    #    #   #  #            #   #   #   #  #      #         #      #    #   #  ##  #
                                             # # #  #####    #    #####   ####        #   #   #   #  ####    ####     #      #    #   #  # # #
                                             #   #  #   #    #    #   #       #       # \\\#   #   #  #           #    #      #    #   #  #  ##  
                                             #   #  #   #    #    #   #   ####         ##\\\    ###   #####   ####     #    #####   ###   #   #
""")
    a1=['((2**2)**3) = 2**5.','False']
    a2=['The slope of a vertical line is undefined.','True']
    a3=['Two lines with positive slopes can be perpendicular.','False']
    a4=[ '5 > 10 or 5 < 7.','True']
    a5=['The set of ordered pairs {(6,4),(2,-5),(-2,4),(6,-4)} is a function.','False']
    a6=['The additive inverse of -10 is 10.','True']
    a7=['The product of two positive numbers is NOT positive.','False']
    a8=[ 'x + 2 = 7 is called an inequality.','False']
    a9=['The associative property is used to write 4x + 8y = 4(x + 2y).','False']
    a10=['The absolute value of a real negative number is negative.','False']
    a11=['-2**3 = (-2)**3.','True']
    a12=['30% of x is equal to 0.03x','False']
    a13=['x is at most equal to 9 is written mathematically as x < 9.','False']
    a14=['3**20 + 3**20 + 3**20 = 3**21','True']
    a15=['1.5 × 10**(-5) is the scientific notation of the number 0.0000015.','False']
    a16=['1000/0 = 0.','False']
    a17=['0/1000 = 0.','True']
    a18=['0.00000010 = 1.','True']
    a19=['1 / (( -2 )** (-4)) = 16.','True']
    a20=['x = 7 DOES NOT satisfy the inequality x - 7 < 0','True']
    l=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20]
    random.shuffle(l)
    s=0
    print("\n"*11)
    for i in range(10):
        ch=0
        while ch!=1 or ch!=2:
            m()
            q=l[i]
            print("\n"*3)
            print(q[0].center(168," "))
            print("\n"*4)
            print("""
                                     #     #####  ####   #   #  #####                               ###     #####   ###   #      ####   #####
                                    ##       #    #   #  #   #  #                                  #   #    #      #   #  #     #       #
                                     #       #    ####   #   #  ####                                  #     ####   #####  #      ####   ####
                                     #       #    #   #  #   #  #                                    #      #      #   #  #          #  #
                                    ###      #    #   #   ###   #####                               ####    #      #   #  #####  ####   #####
    """)  
            print("\n"*11)
            try:
                ch=int(input("enter your choice ::>> "))
            except:
                pass
            if ch==1:
                a="True"
                break
            elif ch==2:
                a="False"
                break


        if a==q[1]:
            print("\n"*15)
            _score.cr()
            print("\n"*15)
            a=input()
            s+=1
        else:
            print("\n"*15)
            _score.wr()
            print("\n"*15)
            a=input()       
    _score.sco()
    if s==1:
        _score._1()
    if s==2:
        _score._2()
    if s==3:
        _score._3()
    if s==4:
        _score._4()
    if s==5:
        _score._5()
    if s==6:
        _score._6()
    if s==7:
        _score._7()
    if s==8:
        _score._8()
    if s==9:
        _score._9()
    if s==10:
        _score._10()


    a=input("press enter to go main menu ::>> ")
