import inflect
def check_shower_thoughts(target):
    p = inflect.engine()
    for i in range(1,target):
        word  = p.number_to_words(i)
        sum = 0
        for c in word:
            if c.isalpha():
                sum += ord(c) - ord('a') + 1
        if (i == sum):
            print "OK :) found!!*** " + str(i) + ' = ' + word
