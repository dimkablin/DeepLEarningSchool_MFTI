
def ngram(words=["Hello", "world"], n=[2, 3]):
    result = []

    for word in words:
        for length in n:
            for i in range(len(word)-length+1):
                result.append(word[i:i+length])

    return result


word = "язык"
ngrams = ngram([word])

for i in ngrams:
    print(i, end=" ")

