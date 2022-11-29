import random , _score
def py():
    def m():
        print("""


                        ####   #   #  #####  #   #   ###   #   #                       ###    #   #  #####   ####   #####  #####   ###   #   #
                        #   #   # #     #    #   #  #   #  ##  #                      #   #   #   #  #      #         #      #    #   #  ##  #
                        ####     #      #    #####  #   #  # # #                      #   #   #   #  ####    ####     #      #    #   #  # # #
                        #        #      #    #   #  #   #  #  ##                      # \\\#   #   #  #           #    #      #    #   #  #  ##  
                        #        #      #    #   #   ###   #   #                       ##\\\    ###   #####   ####     #    #####   ###   #   #
""")
    a1= ["The expression int(x) implies that the variable x is converted to integer","True"]
    a2= ["The value of the expressions 4/ (3*(2 - 1)) and 4/3*(2- 1) is the same","True"]
    a3= ["The value of the expressions 4/ (3*(4 - 2) and 4/3*(4-2) is the same","False"]
    a4= ["The expression 2**2**3 is evaluated as: (2**2) **3","False"]
    a5= ["A string can be surrounded by three sets of single quotation marks or by three sets of double quotation marks","True"]
    a6= ["Variables can be assigned only once","False"]
    a7= ["In Python, a variable is a placeholder for data","False"]
    a8= ["In Python, only if statement has else clause","False"]
    a9= ["Python loops can also have else clause","True"]
    a10= ["In a nested loop, a break statement terminates all the nested loops in one go","False"]
    a11= ["Do both the following represent the same list ['a', b, c'],['c', 'a', 'b']","False"]
    a12= ["A list may contain any type of objects except another list","False"]
    a13= ["There is no conceptual limit to the size of a list","True"]
    a14= ["All elements in a list must be of the same type","False"]
    a15= ["A given object may appear in a list more than once","True"]
    a16= ["The keys of a dictionary must be of immutable types","True"]
    a17= ["You can combine a numeric value and a string by using the + symbol","False"]
    a18= ["The clear( ) removes all the elements of dictionary but does not delete the empty dictionary","True"]
    a19= ["The max() and min() when used with tuples, can work if elements of the tuple are all of the same type","True"]
    a20= ["A list of characters is similar to a string type","False"]
    a21= ["For any index n, s [: n] + s [n :] will give you original string s","True"]
    a22= ["A dictionary can contain keys of any valid Python types","False"]
    a23= ["The two statements x int(22=0/7) and x=int(22/7=0) yield the same results","True"]
    a24= ["The given statement: x + 1 = x is a valid statement","False"]
    a25= ["List slice is a list in itself","True"]


    l=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25]
    random.shuffle(l)
    s=0
    print("\n"*11)
    for i in range(10):
        ch=0
        while ch!=1 or ch!=2:
            m()
            q=l[i]
            print("\n"*6)
            print(q[0].center(168," "))
            print("\n"*4)
            print("""
                                     #     #####  ####   #   #  #####                               ###     #####   ###   #      ####   #####
                                    ##       #    #   #  #   #  #                                  #   #    #      #   #  #     #       #
                                     #       #    ####   #   #  ####                                  #     ####   #####  #      ####   ####
                                     #       #    #   #  #   #  #                                    #      #      #   #  #          #  #
                                    ###      #    #   #   ###   #####                               ####    #      #   #  #####  ####   #####
    """)  
            print("\n"*9)
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

