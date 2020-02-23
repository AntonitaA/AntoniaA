#ανοίγουμε ένα αρχέιο, γράφουμε μέσα το απαραίτηο κειμένου και το κλείνουμε
doc = open("text.txt", "w")
doc.write("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.")
doc.close()

#ανοίγουμε το αρχείο, διαβάζει το περιεχόμενο του και το κλέινουμε
doc = open("text.txt", "r")
text = doc.read()
print(text)
doc.close()

#βάζουμε σε λίστα κάθε λέξη του κειμένου
word = ""
list1 = [ ]
for i in range(len(text)):
    if(text[i] != " " and text[i] != "/n" and text[i] != "," and text[i] != "."):
        word = word +text[i]
    else:
       list1.append(word)
       word = ""
       
#βγάζουμε τα κενά στοιχεία της λίστας list1
list1 = [y for y in list1 if y!=""]

#βρίσκουμε το μήκος της κάθε λέξης
for j in range(len(list1)):
    x = len(list1[j])
#χωρίζουμε τα γράμματα των λέξεων που έχουν πάνω από τρία γράμματα και τα βάζουμε σε μία λίστα, για κάθε λέξη
    if (x>3):
        word_list1 = list1[j]
        letter = ""
        list2 = []
        for k in range(x):
            letter = word_list1[k]
            list2.append(letter)
#ενώνουμε το πρώτο γράμμα κάθε λέξης με το ay
        first =list2[0]
        last = [first, "ay"]
        lastay = ''.join(last)
#αφαιρούμε το πρώτο γράμμα κάθε λέξης
        list2.remove(list2[0])
#προσθέτουμε στο τέλος το πρώτο γράμμα μαζί με το ay
        list2.insert(len(list2), lastay)
#μετατρέπουμε το κάθε στοιχείο της λίστας σε string και εμφανίζεται η κάθε λέξη ως string μετά από τις απαιτούμενες μορφοποιήσεις
        final_word = ''.join(str(z) for z in list2)
        print(final_word)
        final_word = ""