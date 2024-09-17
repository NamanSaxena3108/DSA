def count_word_frequency(words):
    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0)+1
    return word_count

words=['apple','orange','banana','apple','orange','apple']
print(count_word_frequency(words))

#Time Complexity=O(n)
#Space Complexity=O(n)