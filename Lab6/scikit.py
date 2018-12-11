from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

bandwidth_list=[]
p2p_list=[]

file_list=[("p2pdata/1-labeled.dat", "p2pdata/1-unlabeled.dat"), ("p2pdata/2-labeled.dat", "p2pdata/2-unlabeled.dat"),
           ("p2pdata/3-labeled.dat", "p2pdata/3-unlabeled.dat"),("p2pdata/4-labeled.dat", "p2pdata/4-unlabeled.dat")]

#for i in range(len(file_list)-1):
with open(file_list[0][0], 'r') as f:
        line = f.readline()
        while line != "":
            #result = [x.strip() for x in line.split(',')]
            ip, conn, bandwidth, packet, time, p2p = [x.strip() for x in line.split(',')]
            bandwidth_list.append(bandwidth)
            p2p_list.append(p2p)
            line = f.readline()


bandwidth_train, bandwidth_test, p2p_train, p2p_test = train_test_split(bandwidth_list,p2p_list,test_size=0.5)

vectorizer = TfidfVectorizer(use_idf=False)
trainvec = vectorizer.fit_transform(bandwidth_train)
testvec = vectorizer.transform(bandwidth_test)

classifier = MultinomialNB()

classifier.fit(trainvec, p2p_train)
classes = classifier.predict(testvec)

print(metrics.accuracy_score(p2p_test, classes))
print(metrics.classification_report(p2p_test, classes))
print(metrics.confusion_matrix(p2p_test, classes))