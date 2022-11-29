from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


# Data processing
data = ... # Loads a vector of raw text documents
train_index = int(len(data) * 0.6)
train_data = data[:train_index,:]
validation_data = data[int(train_index*1/3):,:]
test_data = data[int(train_index) * 1/3:,:]


# Assume corresponding labels for each data subset
train_labels, test_labels, validation_labels = ...


# Vectorization
one_hot_vectorizer = CountVectorizer(tokenizer=tokenize_normalize,
binary=True, max_features=20)
train_features = one_hot_vectorizer.fit_transform(train_features)
validation_features = one_hot_vectorizer.fit_transform(validation_data)
test_features = one_hot_vectorizer.fit_transform(test_data)


# Classification
lr = LogisticRegression(solver="saga", max_iter=500)

lr_model = lr.fit(train_features, train_labels)
evaluation_summary("LR Train summary",lr_model.predict(train_features, train_labels)

#lr_model = lr.fit(validation_features, validation_features)
evaluation_summary("LR Validation summary",lr_model.predict(validation_features), validation_labels)

#lr_model = lr.fit(test_features, test_labels)
evaluation_summary("LR Test summary",lr_model.predict(test_features), test_labels)

