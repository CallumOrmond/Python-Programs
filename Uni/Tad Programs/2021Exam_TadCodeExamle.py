from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


# Data processing

data = ... # Loads a vector of raw text documents
train_index = int(len(data) * 0.6)
test_index = int(len(data) * 0.2)


train_data = data[:train_index,:]
validation_data = data[train_index:test_index,:]
test_data = data[train_index+test_index:,:]


# Vectorization

one_hot_vectorizer = CountVectorizer(tokenizer=tokenize_normalize,
binary=True,
max_features=20000) # Reasonable number > 1k

train_features = one_hot_vectorizer.fit(train_data)
train_features = one_hot_vectorizer.transform(train_features)
validation_features = one_hot_vectorizer.transform(validation_data)
test_features = one_hot_vectorizer.transform(train_data)


# Classification

lr = LogisticRegression(solver="saga", max_iter=500)
lr_model = lr.fit(test_features, test_labels)

evaluation_summary("LR Train summary",lr_model.predict(train_features), train_labels)

evaluation_summary("LR Validation summary",lr_model.predict(validation_features), validation_labels)

evaluation_summary("LR Test summary",lr_model.predict(test_features), test_labels)

