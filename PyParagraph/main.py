#import dependencies and txt file (paragraph_1.txt or paragraph_2.txt or paragraph_3.txt)

import os 
file = "paragraph_1.txt"

#Create counters
word_count = 0
sentence_count = 0
avg_letter_count = 0
avg_sentence_length = 0

#open file
with open(file, "r") as txtfile:
    
    for line in txtfile:
        words = line.split()
        word_count += + len(words)
        sentence_count += line.count('.') + line.count('!') + line.count('?')
        avg_letter_count +=  (+ len(line)- line.count(" "))/ word_count
        avg_sentence_length = word_count/sentence_count

#Print results
print("Paragraph Analysis")
print("-------------------------")
print("Approximate Word Count: {}".format(word_count))
print("Approximate Sentence Count: {}".format(sentence_count))
print("Average Letter Count: {:.1f}".format(avg_letter_count))
print("Average Sentence Length: {:.1f}".format(avg_sentence_length))