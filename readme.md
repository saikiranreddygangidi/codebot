- This is complete django project which is used to display code based search with code name. 
- This model I developed uses the package sklearnt TfidfVectorizer, cosine_similarity from sklearn.metrics.pairwise
- The package TfidfVectorizer which used to Transforms text to feature vectors that can be used as input to estimator. vocabulary_ Is a dictionary that converts each token (word) to feature index in the matrix, each unique todken gets a feature index. ... Each sentence is a vector, the sentences you've entered are matrix with 3 vectors. which further used as by cosine_similarity matches the query the user search with the file which contains all the codes 
- The return value of TfidfVectorizer class for the data i had provided for example is given below






```
(0, 88)	0.14035782120832418
  (0, 257)	0.1981398819372535
  (0, 415)	0.1981398819372535
  (0, 440)	0.1981398819372535
  (0, 91)	0.17943833177225554
  (0, 77)	0.396279763874507
  (0, 223)	0.1981398819372535
  (0, 238)	0.17943833177225554
  (0, 37)	0.17943833177225554
  (0, 117)	0.3717199615113806
  (0, 239)	0.16616937076441388
  (0, 38)	0.14746782059941596
  (0, 58)	0.33233874152882775
  (0, 169)	0.1981398819372535
  (0, 107)	0.16616937076441388
  (0, 350)	0.11549730942657635
  (0, 235)	0.15587716500996648
  (0, 110)	0.1981398819372535
  (0, 116)	0.14746782059941596
  (0, 61)	0.1981398819372535
  (0, 446)	0.1981398819372535
  (0, 291)	0.16616937076441388
  (1, 117)	0.20864714642799526
  (1, 350)	0.19448660169326332
  (1, 2)	0.3021572669801437
  :	:
  (49, 81)	0.29957893542387715
  (49, 170)	0.29957893542387715
  (49, 266)	0.29957893542387715
  (49, 414)	0.29957893542387715
  (50, 88)	0.30540673064300855
  (50, 454)	0.33917550826708953
  (50, 445)	0.33917550826708953
  (50, 423)	0.390442611511199
  (50, 191)	0.390442611511199
  (50, 105)	0.431135600649089
  (50, 205)	0.431135600649089
  (51, 208)	0.24831324663044868
  (51, 480)	0.24831324663044868
  (51, 50)	0.29608800433244364
  (51, 114)	0.29608800433244364
  (51, 269)	0.29608800433244364
  (51, 344)	0.29608800433244364
  (51, 92)	0.29608800433244364
  (51, 86)	0.29608800433244364
  (51, 314)	0.29608800433244364
  (51, 14)	0.29608800433244364
  (51, 280)	0.29608800433244364
  (51, 54)	0.29608800433244364
  (52, 189)	0.7071067811865476
  (52, 399)	0.7071067811865476
  ```
- cosine_similarity class matches the word as retrieve the relatent data accordingly
- The return value of cosine_similarity class for the data from TfidfVectorizer i had provided for example is given below




```
[[0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.27933564 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]
 ``` 
- And the result of retrieve is display in the interface 
- This is complete brief explanation of the project
