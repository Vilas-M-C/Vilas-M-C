


import  numpy as np
a=["delhi","chennai","bangalore","mumbai"]
 from sklearn.preprocessing import LabelEncoder
 lEncoder=LabelEncoder()
 
 lEncoder=fit(a)
 b=lEncoder.transform(a)
 c=["delhi","mumbai"]
 lEncoder.fit(c)
 lEncoder.transform(c)
 lEncoder.inverse_transform([1])