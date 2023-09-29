gpaOne = 4
creditsOne = 6
weightedOne = gpaOne*creditsOne

gpaTwo = 3
creditsTwo = 5
weightedTwo = gpaTwo*creditsTwo


gpaThree = 2
creditsThree = 1
weightedThree = gpaThree*creditsThree

totalCredits  =  creditsOne+creditsTwo+creditsThree
totalWeighted = weightedOne+weightedTwo+weightedThree

finalGPA = round(totalWeighted/totalCredits,2) 
               
print ('Your Final GPA is', finalGPA)


# launch IDLE and run this file
# explain comments
# fix the error
# add line numbers
# better print line (concatenate it)
# round the result
# re-organize my code


finalGPA=round((weightedOne+weightedTwo+weightedThree)/(creditsOne+creditsTwo+creditsThree), 2)

print('Your final GPA is', finalGPA)

