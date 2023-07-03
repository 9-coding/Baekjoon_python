score = {'A+':4.5, 'A0':4, 'B+':3.5, 'B0':3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1, 'F':0}
tot_credit = 0
major = 0

for i in range(20):
    name, credit, grade = map(str, input().split())
    if grade == 'P':
        continue
    tot_credit += float(credit)
    major += float(credit) * score[grade]
    
print(major / tot_credit)