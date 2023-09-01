import random
def random_word():
    list_of_words=[]
    with open("sowpods.txt","r") as f:
        line=f.readline()
        while line:
            list_of_words.append(line.strip())
            line=f.readline()
    word=random.choice(list_of_words)
    print(word)
    
random_word()