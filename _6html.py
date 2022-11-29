import random, _score
def ht():
    def m():
        print("""


                                              #   #   #####  #   #  #                 ###    #   #  #####   ####   #####  #####   ###   #   #
                                              #   #     #    ## ##  #                #   #   #   #  #      #         #      #    #   #  ##  #
                                              #####     #    # # #  #                #   #   #   #  ####    ####     #      #    #   #  # # #
                                              #   #     #    #   #  #                # \\\#   #   #  #           #    #      #    #   #  #  ##  
                                              #   #     #    #   #  #####             ##\\\    ###   #####   ####     #    #####   ###   #   #
""")
    a1=['Comments are visible on the browsers window.','False']
    a2=['<u> tag is used to mark the text italics.','False']
    a3=['<font> is has values from 1 to 10','False']
    a4=['<p> tag is used to give headings in the web page','False']
    a5=['<h5> is the highest level heading tag.','False']
    a6=['Link attribute is used to change the color of hyperlinks in a web page.','True']
    a7=['Web Browser is used to browse web pages.','True']
    a8=[ '<h1> tag is used to specify heading in a document.','True']
    a9=['Size attribute in <font> is has values from 1 to 10.','False']
    a10=['<p> tag is used to give headings in the web page.','False']
    a11=['The mailto: protocol in the href attribute can validate the email address provided.','False']
    a12=['You can use either  (single quote) or (double quote) to denote a string.','True']
    a13=['You need to use both height and width attributes to shrink your image by half.','False']
    a14=['<span> should be used anytime you want to make inline changes','False']
    a15=['HTML tags and HTML elements the same thing. True or false?','False']
    l=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15]
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
