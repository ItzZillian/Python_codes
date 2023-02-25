'''
There are “n” candidates participating in the online quiz competition. The questions, answer key
and mark allocation are given below:
QUESTION- 1 2 3 4 5
ANSWER- A B B A C
Each question carries 2 marks. For every wrong answer, 25 % of a mark should be reduced. There
is no mark deduction for every unanswered question.
'''

n = int(input())
Answer = ['A', 'B', 'B', 'A', 'C']
l2 = []
l3 = []
l4 = []
d1 = {}
for i in range(0, n):
    l1 = []
    marks = 0
    m = input()
    l1 = m.split()
    for i in range(0, 5):
        if l1[i] == Answer[i]:
            marks += 2
        elif l1[i] == 'X':
            marks += 0
        else:
            marks -= 0.5
    l2.append(marks)
for i in range(0,n):
    d1['C'+str(i+1)] = l2[i]
increasing_marks= sorted(d1.items(), key=lambda x: x[1], reverse=True)
for i, j in increasing_marks:
    l3.append(i)
    l4.append(j)
print('Rank', 'Candidates', 'Total')
i = 0
while i < n:
    if l4[i] == l4[i+1:i+2]:
        print(i+1, l3[i]+','+l3[i+1], l4[i])
        i += 2
    else:
        print(i+1, l3[i], l4[i])
        i += 1