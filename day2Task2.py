# Challenge 

career_options = ['Education', 'Engineering']

Education_advice = ['1.Education careers are always in demand', '2.It is what defines you']
Engineering_advice = ['1.Be ready to learn', '2.Be always active ']
career_questions = ['1.Do you like physics(yes/no)?','2.Do you like helping others solve problems(yes/no)?']

print('Answer the questions below,to get your career match')
print()
print(career_questions[0])
answer_1 = input()
print()
print(career_questions[1])
answer_2 = input()
print()
print('Here are the career sudgestions;')
print()

if answer_1 == 'yes' and answer_2 == 'no':
    print('Consider taking a career in {}'.format(career_options[1]))
    print('Our advice for you:')
    print(Engineering_advice[0])
    print(Engineering_advice[1])

elif answer_1 == 'no' and answer_2 == 'yes':
    print('Consider taking a career in {}'.format(career_options[0]))
    print('Our advice for you:')
    print(Education_advice[0])
    print(Education_advice[1])



elif answer_1 == 'no' and answer_2 == 'no':
    print('NO MATCH FOUND')

else: 
    print('Oops!  wrong input, use small letters only')