#ανοίγουμε ένα αρχείο, γράφουμε μέσα 10 τετράδες αριθμών και το κλείνουμε
f = open("numbers.txt", "w")
f.write("1523 6593 0000 1475 8964 5555 8460 9663 9850 4596 ")
f.close()

#ανοίγουμε το αρχείο, διαβάζει το περιεχόμενο του και το κλείνουμε
f = open("numbers.txt", "r")
nums = f.read()
print(nums)
f.close()

#βάζουμε σε λίστα κάθε τετραψήφιο αριθμό του αρχείου
number = ""
list1 = [ ]
x = len(nums) #το μήκος της list1, δηλαδή μετράει όλα τα ψηφία και τα κενά (49), δε μετρά ως ένα κάθε τετραψήφιο αριθμό
for i in range (x):
    if (nums[i] != " " and nums[i] != "/n"):
        number = number + nums[i]
    else:
        list1.append(number)
        number = ""

#μετατρέπουμε τα στοιχεία της list1 σε ακέραιους και τα βάζουμε στη λιστα integ1
integ1 = [int(x) for x in list1]

#ζητάμε από το χρήστη ένα εξαψήφιο αριθμό
number6 = input("Εισάγατε έναν εξαψήφιο αριθμό: ")

#βάζουμε σε λίστα κάθε ψηφίο του number6
digit = ""
list2 = [ ]
y = len(number6)
for i in range(y):
    digit = digit +number6[i]
    list2.append(digit)
    digit = ""
    
#μετατρέπουμε τα στοιχεία της list2 σε ακέραιους και τα βάζουμε στη λιστα integ2
integ2 = [int(x) for x in list2]

#κάνουμε τρεις τετράδες τον εξαψήφιο αριθμό
testnum1 = [int(list2[i] + list2[i+1] + list2[i+2] + list2[i+3]) for i in range(3)]

#συγκρίνουμε κάθε τετράδα αριθμών με τις διαθέσιμες τετράδες του αρχείου
k = 0
for i in range(len(testnum1)):
    for j in range(len(integ1)):
        if (testnum1[i] == integ1[j]):
            print("Υπάρχει διαθέσιμη τετράδα από τους έξι αριθμούς που εισάχθηκαν και είναι η: " + str(testnum1[i]))
            k += 1
            break #όταν βρε κατάλληλο συνδυασμό βγαίνει από το if
        else:
            continue
    break #όταν βρει κατάλληλο συνδυασμό βγαίνει από το loop
    
if (k==0):
    print("Δεν υπάρχει διαθέσιμη τετράδα από τους έξι αριθμούς που εισάχθηκαν")