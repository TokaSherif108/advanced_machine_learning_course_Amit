def reverse_words(s):
    
    word=s.split(" ")
    new=word[::-1]
    sentence=" "
    for i in new:
        sentence += i + " "
    print(sentence)
s=input("please enter words ")   
reverse_words(s)

