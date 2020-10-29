from daterbase import *

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')

def name():
    global nam
    nam = input('please input your name: ')

    if nam == '' or nam == ' ':
        print('you have inputed nothing try again')
        name()
    else:
        print('Thank you ',nam)
        print('''
        ''')
name()
def gender():
    global gend
    gend = input('''Are you:
    male(m)
    female(f)
    do not want to diclose(d)
    pls provide the replay here:''')
    global female
    female = 'lady'
    if gend == 'male' or gend == 'm':
        print('Thank you Lady',nam)
    elif gend == 'female' or gend == 'f':
        print('Thank you Mr.',nam)
    elif gend == 'diclose' or gend == 'do not want to diclose'or gend == 'd':
        print('Thank you ',nam,'! We respect your right to not tell us')
    elif gend == ' ' or gend == '':
        print('you have inputed nothing try again')
        gender()
    elif gend != 'male' or con != 'lady':
        print('you have inputed the wrong thing try agin')
        gender()

    print('''
    ''')    
gender()
def continues():
    
    gb = input('input E to continue or any anther key to quit the game: ')
    if gb == 'E' or gb == 'e':
        pass
    else:
        exit()
continues()
    

print('''
''')
def game():
    tem =input('''WHICH TEAM DO YOU WANT TO BE IN:
    team malli
    team nesh
    ''')
    if tem == 'malli':
        def red():
            print('Team Malli Motto: (Sisi ni watu wa alli mingi )')            
        red()
    elif tem == 'nesh':
        def blue():
            print('Team Nesh Motto: (Sisi ni watu wale wasee)')
            pass
        blue()
    print('welcome to team',tem)
    maingame = input('''To proced in the game choose an option:
    a.play
    b.lern rules
    ''')
    if maingame == 'a' or maingame == 'play':
        def main(re):
            return re == re [::-1]
        def main2():
            re = input('pls input a word to see if it can be reversable: ')
            if re == '' or re == ' ':
                print('you have inputed nothing try agin')
                main2()
            ans = main(re)

            if ans:
                print(re,'can be reversable.congratulation you have gotten 1 point')
                squares = []
                a = True
                while a == True:
                    squares.append(1)
                    print(squares)
                    sum = 0
                    for num in squares:
                        sum += num
                    print(sum)
                    break

            else:
                print(re,' cant be reversable.you do not have a point')
        main2()
        gbt = input('input E to go back to the menu of the game or any anther key to quit the game: ')
        if gbt == 'E' or gbt == 'e':
            pass
        else:
            exit()
        if tem == 'a':
            print('now its blue team tern')
            main()
        elif tem == 'b':
            print('now its red team tern')
            main()
    elif maingame =='b' or maingame == 'lern rools':
        print(''' 
        1. Enter word that you think can be read forwards and backwards
        2. if it is correct you will score 1 point.
        3. If it is wrong you get 0 points.''')
        gb = input('input E to go back to the menu of the game or any anther key to quit the game: ')
        if gb == 'E' or gb == 'e':
            game()
        else:
            print('bye')
            exit()
    elif maingame == '' or maingame == ' ':
        print('you have inputed nothing try again')
        game()
        
    elif maingame != 'a' or maingame != 'b':
        print('you have inputed the wrong thing try again')
        game()
game()