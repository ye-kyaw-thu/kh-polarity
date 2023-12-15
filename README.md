# kh-polarity
Polarity Classification for Khmer

***Please wait. We are preparing ...  

## Corpus Information

### Version 1.0

## Code Information

### for Preprocessing

[1]. [khnormal](https://github.com/sillsdev/khmer-character-specification/blob/master/python/scripts/khnormal), The original or active code for Khmer Normalization.    
[2]. [khnormal.2.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/khnormal.2.py), This code was used for Khmer Normalization.    
[3]. [cut-column.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/cut-column.pl), This code was used to fix the number of class errors.    
[4]. [print-codepoint.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/print-codepoint.pl), This code was used for printing the code points (decimal, Unicode) of each Khmer character.  
[5]. [check-empty-field.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/check-empty-field.pl), This code was used to clean blank fields in the Khmer polarity corpus.  
[6]. [break.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/break.py), This code was used for [SentencePiece](https://github.com/google/sentencepiece) segmentation.   

### for Modeling

[1]. [knn-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/knn-classifier.py): K Nearest Neighbor (KNN) Classifier  
[2]. [dtree-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/dtree-classifier.py): Decision-Tree Classifier  
[3]. [rforest-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/rforest-classifier.py): Random-Forest Classifier  
[4]. [svm-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/svm-classifier.py): Support Vector Machine (SVM) Classifier  
[5]. [sgd-classifier2.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/sgd-classifier2.py): Stochastic Gradient Descent (SGD) Classifier   
[6]. [sgd-tune-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/sgd-tune-classifier.py): Tuning with Stochastic Gradient Descent (SGD) Classifier    

## Experiment Logs

In this section, File No. 1 contains data cleaning and various preprocessing steps. The results presented in our paper are derived from the log files No. 2 and No. 3.    

[1]. [kh-polarity-exp1](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp1.md): This is the log file for Experiment 1.   
[2]. [kh-polarity-exp2](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp2.md): This is the log file for Experiment 2.   
[3]. [kh-polarity-exp3](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp3.md): This is the log file for Experiment 3.    

## Citation

If you plan to use any code snippets or the kh-polarity corpus in your research, we kindly ask that you acknowledge and cite the following paper:   

Sokheng Khim, Ye Kyaw Thu and Sethserey Sam, "Sentiment Polarity Classification for Khmer", In Proceedings of the 18th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP 2023), Nov 27 to 29, 2023, Bangkok, Thailand, pp. xx-xx  
