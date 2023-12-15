# kh-polarity
Polarity Classification for Khmer

***Please wait. We are preparing ...  

## Corpus Information

Below is the tree structure of the corpus folder:  

```
$ tree ./corpus/
./corpus/
├── exp
│   ├── csv_format
│   │   ├── test.csv
│   │   └── train.csv
│   └── fasttext_format
│       ├── test.sentence.fasttext
│       └── train.sentence.fasttext
└── version-1
    └── kh-polar.ver1.0.txt

4 directories, 5 files
```

In the exp/ folder, you will find the training and test datasets used in our experiments. These datasets are formatted as comma-separated values (CSV) and are located under the exp/csv_format/ folder. We applied traditional machine learning methods such as K-nearest Neighbors (KNN), Decision Tree, Random Forest, Support Vector Machine (SVM), and Stochastic Gradient Descent (SGD) for Khmer polarity classification. The CSV format is as follows:   

```
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/csv_format$ head -n 3 train.csv
text,label
▁រដ្ឋ ម ន្ត រី ប រ ិ ស្ថាន អ ៊ ុយ ក្រ ែន បាន បញ្ជា ក់ កាល ពី ថ ្ ង ៃ ច ន្ទ ទី ▁៣ ▁ខែ ត ុល ា ថា ▁ការ ខ ូ ច ខាត ប រ ិ ស្ថាន ក្នុង ប្រ ទេស អ ៊ ុយ ក្រ ែន ដែ ល ប ណ្តាល មក ពី ការ ឈ ្ល ាន ព ាន រ ប ស់ រ ុ ស្ ស៊ី ត្រ ូវ បាន គេ ប៉ ាន់ ប្រ មា ណ ថា ▁មាន ទ ំ ហ ំ ជា ង ▁៣ ៥ ៣ ព ាន់ ល ាន ដ ុល ្ល ារ ▁ជាមួយ នឹង ត ំ ប ន់ អ ភ ិ រ ក្ស ធ ម្ ម ជាតិ រ ាប់ ល ាន ហ ិក តា ទ ៀ ត ស្ ថ ិត ន ៅ ក ្រោម ការ គ ំ រា មក ំ ហ ែង ▁។,negative
▁ខ្ញុំ ច ង់ ច ាប់ ផ្តើម ប្រ ើ ផ ា ស ពិសេស ស ំ រ ាប់ អ ្ន ក ធ្វើដំណើរ,neutral
```

```
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/csv_format$ head -n 3 test.csv
text,label
▁ នេះ ប ើ តា ម ប្រ សា ស ន៍ រ ប ស់ ▁ឯក ឧ ត្ត ម ▁ ន េ ត្រ ▁ភ ក ្ត រា ▁រដ្ឋ លេខ ា ធ ិ ការ ▁និង ជា អ ន ុ ប្រ ធាន អ ច ិ ន្ត រ ៃ យ ៍ ក្រ ុ ម ការ ង ារ ប្រឆាំង ការ ស ម្ អា ត ប្រ ាក់ នៃ ក្រ ស ួង ប រ ិ ស្ថាន ▁កាល ថ ្ ង ៃ ទី ៥ ▁ខែ ត ុល ា ▁ឆ្នាំ ២ ០ ២ ២ ▁។,negative
▁ចំណ ែក ▁ម ន្ត រី ▁ សិទ្ធិ ម ន ុ ស្ស ▁និង ▁អ្នក វិ ភ ា គ ▁យល់ ▁ថា ▁អ្វី ▁ដែល ▁លោក ▁ ហ៊ុន ▁ស ែន ▁លើក ▁ឡើង ▁មក ▁នោះ ▁ជា ▁វ ោ ហា រ សា ស្ត រ ▁ ន យោប ាយ ▁ដើម្បី ▁ប ន ្ល ំ ▁ការ ▁ពិ ត ▁ប៉ុណ្ណ ោះ ។,negative
```

For experiments utilizing the FastText approach, a specific data format is required. FastText is a library for efficient learning of word representations and sentence classification. It is particularly useful for applications that benefit from understanding the nuances and meanings of words within large datasets. To accommodate FastText's requirements, we prepared our data in a format that is compatible with this library. This formatted data can be found under exp/fasttext_format/. The FastText format is structured as follows:  

```
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/fasttext_format$ head -n 3 train.sentence.fasttext
__label__negative ▁រដ្ឋ ម ន្ត រី ប រ ិ ស្ថាន អ ៊ ុយ ក្រ ែន បាន បញ្ជា ក់ កាល ពី ថ ្ ង ៃ ច ន្ទ ទី ▁៣ ▁ខែ ត ុល ា ថា ▁ការ ខ ូ ច ខាត ប រ ិ ស្ថាន ក្នុង ប្រ ទេស អ ៊ ុយ ក្រ ែន ដែ ល ប ណ្តាល មក ពី ការ ឈ ្ល ាន ព ាន រ ប ស់ រ ុ ស្ ស៊ី ត្រ ូវ បាន គេ ប៉ ាន់ ប្រ មា ណ ថា ▁មាន ទ ំ ហ ំ ជា ង ▁៣ ៥ ៣ ព ាន់ ល ាន ដ ុល ្ល ារ ▁ជាមួយ នឹង ត ំ ប ន់ អ ភ ិ រ ក្ស ធ ម្ ម ជាតិ រ ាប់ ល ាន ហ ិក តា ទ ៀ ត ស្ ថ ិត ន ៅ ក ្រោម ការ គ ំ រា មក ំ ហ ែង ▁។
__label__neutral ▁ខ្ញុំ ច ង់ ច ាប់ ផ្តើម ប្រ ើ ផ ា ស ពិសេស ស ំ រ ាប់ អ ្ន ក ធ្វើដំណើរ
__label__neutral ▁ក្រោយ ពេល ដែ ល វា បាន ហ ែ ល ប ត់ ច ុះ ប ត់ ឡើង គ ្រ ប់ ៗ ក ន ្ល ែង វា ទៅ ដល់ ស្រ ុក ខ ោ ន ហើយ វា ស ំ ច ត ន ៅ ទី នោះ ២ . ២ ថ ្ ង ៃ ទ ើ ប វា ហ ែ ល ច ុះ មក វិញ ។
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/fasttext_format$
```

```
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/fasttext_format$ head -n 3 test.sentence.fasttext
__label__negative ▁ នេះ ប ើ តា ម ប្រ សា ស ន៍ រ ប ស់ ▁ឯក ឧ ត្ត ម ▁ ន េ ត្រ ▁ភ ក ្ត រា ▁រដ្ឋ លេខ ា ធ ិ ការ ▁និង ជា អ ន ុ ប្រ ធាន អ ច ិ ន្ត រ ៃ យ ៍ ក្រ ុ ម ការ ង ារ ប្រឆាំង ការ ស ម្ អា ត ប្រ ាក់ នៃ ក្រ ស ួង ប រ ិ ស្ថាន ▁កាល ថ ្ ង ៃ ទី ៥ ▁ខែ ត ុល ា ▁ឆ្នាំ ២ ០ ២ ២ ▁។
__label__negative ▁ចំណ ែក ▁ម ន្ត រី ▁ សិទ្ធិ ម ន ុ ស្ស ▁និង ▁អ្នក វិ ភ ា គ ▁យល់ ▁ថា ▁អ្វី ▁ដែល ▁លោក ▁ ហ៊ុន ▁ស ែន ▁លើក ▁ឡើង ▁មក ▁នោះ ▁ជា ▁វ ោ ហា រ សា ស្ត រ ▁ ន យោប ាយ ▁ដើម្បី ▁ប ន ្ល ំ ▁ការ ▁ពិ ត ▁ប៉ុណ្ណ ោះ ។
__label__positive ▁ការងា រ មាន ស្ ថ ិ រ ភាព ▁ហើយ អ ្ន ក អា ច ទ ទ ួល បាន ស ម ិទ្ធ ផល ជ ាក់ ល ាក់ ក្នុង អា ជ ី ព រ ប ស់ អ ្ន ក ▁ ធាន ា ជ ី វ ិត រ ប ស់ អ ្ន ក ។
(base) ye@lst-gpu-3090:~/tmp/kh-polarity/corpus/exp/fasttext_format$
```

### Version 1.0

## Code Information

### for Preprocessing

[1]. [khnormal](https://github.com/sillsdev/khmer-character-specification/blob/master/python/scripts/khnormal), The original or active code for Khmer Normalization.    
[2]. [khnormal.2.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/khnormal.2.py), This code was used for Khmer Normalization.    
[3]. [cut-column.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/cut-column.pl), This code was used to fix the number of class errors.    
[4]. [print-codepoint.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/print-codepoint.pl), This code was used for printing the code points (decimal, Unicode) of each Khmer character.  
[5]. [check-empty-field.pl](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/check-empty-field.pl), This code was used to clean blank fields in the Khmer polarity corpus.  
[6]. [train-sentencepiece.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/train-sentencepiece.py), This code was used to train [SentencePiece](https://github.com/google/sentencepiece) model.  
[7]. [break.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/break.py), This code was used for [SentencePiece](https://github.com/google/sentencepiece) segmentation.   

### for Modeling

[1]. [knn-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/knn-classifier.py): K Nearest Neighbor (KNN) Classifier  
[2]. [dtree-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/dtree-classifier.py): Decision-Tree Classifier  
[3]. [rforest-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/rforest-classifier.py): Random-Forest Classifier  
[4]. [svm-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/svm-classifier.py): Support Vector Machine (SVM) Classifier  
[5]. [sgd-classifier2.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/sgd-classifier2.py): Stochastic Gradient Descent (SGD) Classifier   
[6]. [sgd-tune-classifier.py](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/code/sgd-tune-classifier.py): Tuning with Stochastic Gradient Descent (SGD) Classifier    

## Experiment Logs

In this section, you will find detailed logs of our experiments. File No. 1 includes data cleaning and various preprocessing steps. File No. 2 details the results obtained using the first version of our classifiers. The results presented in our paper are primarily derived from log files No. 3 and the latter part of No. 4.

1. [kh-polarity-exp1](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp1.md): This log file pertains to Experiment 1, focusing on data cleaning and preprocessing.
2. [kh-polarity-exp2](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp2.md): This log file corresponds to Experiment 2, featuring the initial classifier results.
3. [kh-polarity-exp3](https://github.com/ye-kyaw-thu/error-overflow/blob/master/kh-polarity-exp3.md): This log file is for Experiment 3, which significantly contributes to the results discussed in our paper.
4. [testing-tabpfn.md](https://github.com/ye-kyaw-thu/error-overflow/blob/master/testing-tabpfn.md): This log file documents an experiment involving [TabPFN](https://github.com/automl/TabPFN) and [FastText](https://fasttext.cc/), with its latter part being crucial for our paper's findings.

## Presentation Slide

### At the 4th NLP/AI Workshop 2022

- [WS-12_SentimentPolarityClassificationForKhmer.pdf](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/slides/NLP_AI_workshop_2022/WS-12_SentimentPolarityClassificationForKhmer.pdf): This is the presentation slide for the 4th NLP/AI Workshop 2022, held in Chiang Mai, Thailand.    
  
### At the iSAI-NLP Conference 2023

- [kh_polarity_talk.pdf](https://github.com/ye-kyaw-thu/kh-polarity/blob/main/slides/iSAI-NLP2023_conference/kh_polarity_talk.pdf): This is the presentation slide for the 18th iSAI-NLP 2023 conference, held in Bangkok, Thailand.    

## Citation

If you plan to use any code snippets or the kh-polarity corpus in your research, we kindly ask that you acknowledge and cite the following paper:   

Sokheng Khim, Ye Kyaw Thu and Sethserey Sam, "Sentiment Polarity Classification for Khmer", In Proceedings of the 18th International Joint Symposium on Artificial Intelligence and Natural Language Processing (iSAI-NLP 2023), Nov 27 to 29, 2023, Bangkok, Thailand, pp. xx-xx  

## References

[1]. Pandey, A., & Jain, A. (2017). Comparative analysis of KNN algorithm using various normalization techniques. International Journal of Computer Network and Information Security, 9(11), 36.  
[2]. Uddin, S., Haque, I., Lu, H., Moni, M. A., & Gide, E. (2022). Comparative performance analysis of K-nearest neighbour (KNN) algorithm and its different variants for disease prediction. Scientific Reports, 12(1), 1-11.  
[3]. Quinlan, J. R. (1996). Learning decision tree classifiers. ACM Computing Surveys (CSUR), 28(1), 71-72.  
[4] Song, Y. Y., & Ying, L. U. (2015). Decision tree methods: applications for classification and prediction. Shanghai archives of psychiatry, 27(2), 130.   
[5]. Gao, D., Zhang, Y. X., & Zhao, Y. H. (2009). Random forest algorithm for classification of multiwavelength data. Research in Astronomy and Astrophysics, 9(2), 220. 
[6]. Bhavsar, H., & Panchal, M. H. (2012). A review on support vector machine for data classification. International Journal of Advanced Research in Computer Engineering & Technology (IJARCET), 1(10), 185-189.  
[7]. Sharma, A. (2018). Guided stochastic gradient descent algorithm for inconsistent datasets. Applied Soft Computing, 73, 1068-1080.
[8]. Wang, J., & Joshi, G. (2021). Cooperative SGD: A unified framework for the design and analysis of local-update SGD algorithms. Journal of Machine Learning Research, 22.
[9]. A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, Bag of Tricks for Efficient Text Classification
