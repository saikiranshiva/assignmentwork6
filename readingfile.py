f=open("file1.text","r")

no_of_lines=0
no_of_words=0
no_of_charecters=0
for i in f:
    i=i.strip()
    
    words=i.split()
    no_of_lines=no_of_lines+1
    no_of_words=no_of_words+len(words)
    no_of_charecters=no_of_charecters+len(i)

print("no of lines:",no_of_lines)
print("no of words:",no_of_words)
print("no of charecters:",no_of_charecters)
f.close()
