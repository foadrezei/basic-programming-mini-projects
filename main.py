import number_1
import number_2
import number_3
import number_4
import number_5
import number_6
import number_7
import number_8
import number_9
import number_10
while True:
    print("type 0 to eixt the program")
    question = int(input('Which question do you want to solve : '))
    if question == 1:
        number_1.UserInput()
    elif question == 2:
        number_2.UserInput()
    elif question == 3:
        number_3.UserInput()
    elif question == 4:
        number_4.UserInput()
    elif question == 5:
        number_5.UserInput()
    elif question == 6:
        print("this question was very chalenching for me ... ")
        print("to get better result it's better to look at the code itself")
        number_6.UserInput()

    elif question == 7:
        number_7.UserInput()
    elif question == 8:
        number_8.UserInput()
    elif question == 9:
        number_9.UserInput()
    elif question == 10:
        number_10.UserInput()
    elif question == 0:
        exit()
    else:
        print(f'there is no question number {question} to be solved!!!!!!')
        print()
        print('Try a again')
