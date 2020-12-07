# TDA-HC
This repository contains all data and code for the experiments for the paper "Hierarchical clustering and zeroth persistent homology" by myself and Atabey Kaygun.

### Programming Language Versions We Used:
* Python 3.7.8
  - Numpy 1.18.5
  - Scipy 1.5.4
  - Pandas 1.0.4
  - Matplotlib 3.2.1
  - GUDHI 3.2.0
  
* SageMath 9.1 Shell
* R 3.6.3
  - TDA 1.6.9
  - vegan 2.5.6
  - repr 1.1.0
  - dendextend 1.13.4

### 1_Data2Diagram_GUDHI_Dionysus.R

This code is for obtaining topological features (intervals) of point clouds by using different algorithm such as GUDHI and Dionysus2

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

Here, we obtain the filtered Vietoris Rips complex by using GUDHI library.

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

Here, this code compares the two dendrograms one from the hierarchical clustering and one from the zeroth persistent homology. 
The output is the result of the Mantel Test.

* On terminal, type
```
Rscript 5_Compare_Dendrogram.R
```


