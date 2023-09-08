import random
#questions upto 5 are in this file
while True:
    question_number = float(input('enter question number and 0 to quit'))
    if question_number == 2.1:
        name = input('enter name')
        print('hello',name)

    if question_number == 2.2:
        radius = int(input('enter radius'))
        print('area = ', 3.14*radius*radius)
    if question_number == 2.3:
        length = int(input('enter length'))
        side = int(input('enter width'))
        perimeter = 2*(length+side)
        area = length*side
        print('area and perimeter are:', area, perimeter)
    if question_number == 2.4:
        number_1 = int(input('enter number'))
        number_2 = int(input('enter 2nd number'))
        number_3 = int(input('enter 3rd number'))
        sum = number_3 + number_2 + number_1
        product = number_3 + number_2 + number_1
        average = sum / 3
        print('the sum, product and average are:', sum, product, average)
    if question_number == 2.5:
        talents = int(input('enter talents:'))
        pounds = int(input('enter pounds:'))
        lots = float(input('enter lots:'))
        kg = (talents*20*32*13.3) + (pounds*32*13.3) + (lots*13.3)
        print('The weight in modern units:', kg//1000,'kg',kg%1000,'gm')
    if question_number == 2.6:
        unit = random.randint(0,9)
        tens = random.randint(0,9)
        hundreths = random.randint(0,9)
        code_1 = hundreths*100 + tens*10 + unit
        print(code_1)
        ones = random.randint(0,6)
        ten = random.randint(0,6)
        hundreds = random.randint(0,6)
        thousands = random.randint(0,6)
        code_2 = thousands*1000 + hundreds*100 + ten*10 + ones
        print(code_2)
    if question_number == 3.3:
        gender = input('enter male or female')
        hb = int(input('enter hb count'))
        if gender == 'male':
            if hb<167 and hb>134:
                print('normal')
            elif hb>167:
                print('high')
            elif hb<134:
                print('low')
            else:
                print('invalid input')
        elif gender =='female':
            if hb<155 and hb>117:
                print('normal')
            elif hb>155:
                print('high')
            elif hb<117:
                print('low')
            else:
                print('invalid input')
        else:
            print('invalid gender')
    if question_number == 3.1:
        zander = int(input('enter the lenght of zander in cm'))
        if zander>41:
            print('fish has been caught')
        else:
            difference = 42-zander
            print('the line was short by:',difference,'cm')
    if question_number == 3.2:
        type = input('enter room type')
        if type == 'LUX':
            print('upper-deck cabin with a balcony.')
        elif type == 'A':
            print('above the car deck, equipped with a window.')
        elif type == 'B':
            print('windowless cabin above the car deck.')
        elif type == 'C':
            print('windowless cabin below the car deck.')
        else:
            print('invalid entry')
    if question_number == 3.4:
        year = int(input('enter year'))
        if year%100 == 0:
            if year%400 == 0:
                print('leap year')
            else:
                print('not leap year')

        elif year%4 == 0:
            print('leap year')

        else:
            print('not leap year')
    if question_number == 4.1:
        for i in range(1001):
            if i%3==0:
                print(i)
    if question_number == 4.2:
        while True:
            inches = int(input('enter inches'))
            if inches>0:
                cm = inches * 2.54
                print(cm)
            elif inches<0:
                break
            else:
                print('invalid input ')
    if question_number == 4.3:
        l=[]
        while True:
            ch = (input('enter number'))
            if ch !='':
                l.append(int(ch))
            else:
                break
        l.sort()
        print('largest',l[-1])
        print('smallest',l[0])
    if question_number == 4.4: #need to check
        random = random.randint(1,10)
        while True:
            number = int(input('enter ur guess'))
            if random>number:
                print('to low')
            elif number>random:
                print('too high')
            else:
                print('correct the number was:',random)
                break
    if question_number == 4.5:
        username = input('enter username')
        password = input('enter password')
        i=0
        while True:
            if i==5:
                print('too many trie failed')
                break
            if username == 'python' and password == 'rules':

                print('welcome')
            else:
                print('incorrect try again')
                username = input('enter username')
                password = input('enter password')
                i=i+1
    if question_number == 4.6:
        print('work in progress')
    if question_number == 5.1:
        dice = int(input('enter how many dice'))
        sum = 0
        for i in range(dice):
            sum = sum + random.randint(1,7)
        print(sum)
    if question_number == 5.2:
        l=[]
        while True:
            x = input('enter number')
            if x == '':
                break
            else:
                l.append(int(x))
        y=l.sort()
        print(y[-6:-1])
    if question_number == 5.3:
        k=0
        no = int(input('enter number'))
        for i in range(2,no):
            if no%i==0:
                print('non prime')
                break
            else:
                k=1
        if k==1:
            print('prime number')
    if question_number == 5.4:
        city_list=[]
        for i in range(5):
            city = input('enter city name:')
            city_list.append(city)
        for i in city_list:
            print(i)

















