def sort(sentence):
    words=sentence.split(" ")
    words.sort()
    sen=" ".join(words)
    return sen
sentence="abc degg bcd yzx abb"
print (sort(sentence))