import embeddings

emb = embeddings.EmbeddingsDictionary(max_words = 100000)

#print(emb.dictionary['geek'])
print(emb.w2neighbors('geek'))

def word2vec(word):
    vec = emb.emb[emb.dictionary[word]]
    return vec

def analog_find(s1, s2, s3):
    tokyo = word2vec(s1)
    spain = word2vec(s2)
    japan = word2vec(s3)
    madrid = tokyo + spain - japan
    return (madrid)

def vec2word(vec):
    word = emb.emb2neighbors(vec, 1)[1][0]
    return word

def answer(s1, s2, s3):
    vanswer = vec2word(analog_find(s1,s2, s3))
    answer = emb.words[vanswer]
    return answer

print(answer('Tokyo', 'Spain', 'Japan'))
