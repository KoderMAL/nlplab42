import embeddings

emb = embeddings.EmbeddingsDictionary(max_words = 100000)

#print(emb.dictionary['geek'])
print(emb.w2neighbors('geek'))
