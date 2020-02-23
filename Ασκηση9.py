#ζητάμε ένα αριθμό από το χρήστη
number1 = eval(input("Enter a number: "))

#συνάρτηση που προσθέτει τα ψηφία του number2 όταν είναι ακέραιος
def sum_digits_int(number2):
    s = 0
    while number2:
        s += number2 % 10 #γίνεται η πράξη s = s + number2 % 10, όπου % δίνει το υπόλοιπο της διαίρεσης
        number2 //= 10 #γίνεται η πράξη number2 = number2 // 10, όπου // δίνει το πηλίκο της διαίρεσης στρογγυλοποιημένο προς τα κάτω
    return s #το άθροισμα των ψηφίων
    
#συνάρτηση που προσθέτει τα ψηφία του number2 όταν είναι ακέραιος    
def sum_digits_float(number2):
    string = str(number2) #κάνουμε string τον αριθμό για να τον βάλουμε σε λίστα
    #βάζουμε τα ψηφία του αριθμού σε list1
    list1 = [ ]
    dig = ""
    for i in range(len(string)):
        if (string[i] != '.'):
            dig = string[i]
            list1.append(dig)
            dig = ""
    #κάνουμε τα στοιχεία της λίστας ακέραιους και έτσι προσθέτουμε τα ψηφία του αρχικού αριθμού        
    f = 0
    for i in range(len(list1)):
        integer = int(list1[i])
        f += integer
        integer = ""
    return f #το άθροισμα των ψηφίων
    
while True:
    number2 = (number1 * 3) + 1
    #ελέγχει αν ο αριθμός είναι ακέραιος ή δεκαδικός, έτσι ώστε να χρησιμοποιήσει τη σωστή συνάρτηση
    if (number2 == int(number2)):
        number4 = sum_digits_int(number2)
    else:
        number4 = sum_digits_float(number2)
    #ελέγχει αν ο number4 είναι μονοψήφιος    
    if len(str(number4)) == 1:
        break
    else: 
        number1 = number4
        continue
       
print(number4)