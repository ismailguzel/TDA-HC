# TDA-HC
This repository contains all data and python, R and SageMath codes for the experiments to the following paper:"Hierarchical clustering and zeroth persistent homology"

The flow of codes as the follows:
Program versiyonları

* Python 3.7.8
* SageMath 9.1 Shell
* R scripting front-end version 3.6.3


### 0_Degree2Radians.py
python 0_Degree2Radians.py
Radyana dönüştürme işlemi

### 1_Data2Diagram_GUDHI_Dionysus.R
Rscript 1_Data2Diagram_GUDHI_Dionysus.R
Farklı iki kütüphane ile veri üzerinden persistent homology hesabı ile 
aralıkları saklarız.

***2_Barcodes_GUDHI_Dionysus.py :
python 2_Barcodes_GUDHI_Dionysus.py
Persistent homology çıktısı aralıkları görselleştiremk için kullanılır.
Gudhi library sinden elde edilen barcode verileri büyükten küçüğe sıralı gelir.
Dolayısyla doğum ölümlerin neye ait olduklarını takip edemeyiz.
Dionysus da ise veriler saklanırken okuma index sırasına göre saklar.

***3_Data2Rips_Gudhi.py :
python 3_Data2Rips_Gudhi
ilk olarak verileri okutup kaç veri kullanacağız karar verelim. Boyut ayarlaması lazım.,
diğer programlar için hazır formata getir
Sonra, gudhi kütüphanesi kullanarak  rips complex üreterek verileri sakla


***4_Rips2Homological_Distance.sage
sage 4_Rips2Homological_Distance.sage 24 0 0 0.30 0.01
24 boyutlu 0 homoloji, epsilonstart = 0, epsilonend=0.30 epsilonstep=0.01
homology distance matrisi üretelim

***5_Compare_Dendrogram.R
Rscript 5_Compare_Dendrogram.R
