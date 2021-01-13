#!/usr/bin/env python

scores_by_student = {}

scores_set = set()

with open("../DATA/testscores.dat") as scores_in:

    for line in scores_in:
        name, raw_score = line.split(":")
        score = int(raw_score)
        # print("BEFORE:", scores_by_student)
        scores_by_student[name] = score  # add element to dict
        scores_set.add((name, score))  # add element to set
        # print("AFTER:", scores_by_student)

# for student, score in sorted(scores_by_student.items()):
for student, score in sorted(scores_by_student.items()):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    print("{:20s} {} {}".format(student, score, grade))
sum_of_scores = sum([v[1] for v in scores_set])
average = sum_of_scores/len(scores_set)
print("\naverage score is  {:.2f}\n".format(average))
