# TDA-HC
This repository contains all data and python, R and SageMath codes for the experiments to the paper "Hierarchical clustering and zeroth persistent homology" by myself and Atabey Kaygun.

### Programs versions:
* Python 3.7.8
* SageMath 9.1 Shell
* R 3.6.3

### 1_Data2Diagram_GUDHI_Dionysus.R

Burada program ne yapiyor onu yazman lazim. Ayni asagidaki gibi.

* On terminal, type
```
Rscript 1_Data2Diagram_GUDHI_Dionysus.R
```

### 2_Barcodes_GUDHI_Dionysus.py 

This code is for visualizing the output of persistent homology as intervals. The output consists of barcodes created by two different libraries on the same data.

* On terminal, type
```
python 2_Barcodes_GUDHI_Dionysus.py
```

### 3_Data2Rips_Gudhi.py 

Here, we obtain the filtered Vietoris Rips complex with epsilon parameter by using GUDHI library.

- On terminal, type
```
python 3_Data2Rips_Gudhi.py
```

### 4_Rips2Homological_Distance.sage

This code calculates the homological distance matrix.

* On SageMath shell, type
```
sage 4_Rips2Homological_Distance.sage 24 0 0 0.30 0.01
```
  - sample size = 24 
  - degree of homology = 0
  - epsilon start = 0
  - epsilon end = 0.30
  - epsilon step = 0.01

### 5_Compare_Dendrogram.R

Here, this code compares the two dendrograms, one from the hierarchical clustering and one from the zeroth persistent homology. 
The output is the result of Mantel Test.

* On terminal, type
```
Rscript 5_Compare_Dendrogram.R
```


