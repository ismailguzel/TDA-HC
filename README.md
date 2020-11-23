# TDA-HC
This repository contains all data and python, R and SageMath codes for the experiments to the following paper:"Hierarchical clustering and zeroth persistent homology"

The flow of codes as the follows:

### Programs versions:
* Python 3.7.8
* SageMath 9.1 Shell
* R 3.6.3


### 0_Degree2Radians.py
- From Anaconda Prompt type
```
python 0_Degree2Radians.py
```
- Radyana dönüştürme işlemi

### 1_Data2Diagram_GUDHI_Dionysus.R
- From Anaconda Prompt type
```
Rscript 1_Data2Diagram_GUDHI_Dionysus.R
```
- Farklı iki kütüphane ile veri üzerinden persistent homology hesabı ile  aralıkları saklarız.

### 2_Barcodes_GUDHI_Dionysus.py :
- python 2_Barcodes_GUDHI_Dionysus.py
- Bu kodu persistent homology çıktısı aralıkları görselleştirmek için kullanırız.Aynı veri üzerinden iki farklı kütüphanenin persistent diagram çıktılarına göre oluşturulan barkodlar

### 3_Data2Rips_Gudhi.py :
- python 3_Data2Rips_Gudhi
- Veri içerisinde kaç şehir alalım burda söylemeliyiz.Sonraki kodlar için de boyut ayarlanması lazım.,
Sonra, gudhi kütüphanesi kullanarak  rips complex üreterek simpleksleri oluşum epsilon değerleri ile birlikte saklayalım.

### 4_Rips2Homological_Distance.sage
- sage 4_Rips2Homological_Distance.sage 24 0 0 0.30 0.01
- 24 boyutlu 0 homoloji, epsilonstart = 0, epsilonend=0.30 epsilonstep=0.01
- homology distance matrisi üretelim

### 5_Compare_Dendrogram.R
- Rscript 5_Compare_Dendrogram.R
- Hierarchical Clustering
- Mantel Test
- Tanglegram


