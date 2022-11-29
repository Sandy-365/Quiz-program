import random , _score
def ph():
    def m():
        print("""


                        ####   #   #  #   #   ####   #####   ####   ####             ###    #   #  #####   ####   #####  #####   ###   #   #
                        #   #  #   #   # #   #         #    #      #                #   #   #   #  #      #         #      #    #   #  ##  #
                        ####   #####    #     ####     #    #       ####            #   #   #   #  ####    ####     #      #    #   #  # # #
                        #      #   #    #         #    #    #           #           # \\\#   #   #  #           #    #      #    #   #  #  ##  
                        #      #   #    #     ####   #####   ####   ####             ##\\\    ###   #####   ####     #    #####   ###   #   #
""")
    a1=["Inertia is a vector quantity. It has both magnitude and direction.","False"]
    a2=["Inertia is directly proportional to an object's mass.","True"]
    a3=["Inertia is directly proportional to an object's velocity.","False"]
    a4=["Friction is a force that opposes motion.","True"]
    a5=["Mass and weight are the same.","False"]
    a6=["An object at rest has no inertia.","False"]
    a7=["In an object is not moving, no forces are acting upon it.","False"]
    a8=["If an object is moving, a net force must be acting upon it.","False"]
    a9=["F=ma and a=F/m are both mathematical representations of Newton's 2nd Law.","True"]
    a10=["At terminal velocity, all motion stops.","False"]
    a11=["Your mass on Earth is different than your mass on Mars.","False"]
    a12=["A rocket is propelled through space by the exhaust gases pushing against air.","False"]
    a13=["Any object falling toward Earth will accelerate until impact.","False"]
    a14=["In a vacuum, all objects fall toward the center of the Earth with the same acceleration.","True"]
    a15=["Three skydivers tied together fall faster than a single skydiver.","False"]
    a16=["Friction is a force that retards motion.","True"]
    a17=["Centrifugal force exists only in rotating objects.","False"]
    a18=["Linear momentum is always conserved.","True"]
    a19=["Angular momentum is always conserved.","True"]
    a20=["Padding decreases the effect of a collision by increasing the contact time.","True"]
    a21=["Simple machines like pulleys increase the amount of work we can do.","False"]
    a22=["Centrifugal force really exists.","False"]
    a23=["A rocket is propelled through space due to the escaping gases pushing against air.","False"]
    a24=["Conservation of momentum is the same as Newton's Second Law.","False"]
    a25=["displacement is vector quantity.","True"]

    l=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25]
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










































        
