# TDA-HC
This repository contains all data and python, R and SageMath codes for the experiments to the following paper:"Hierarchical clustering and zeroth persistent homology"

### Programs versions:
* Python 3.7.8
* SageMath 9.1 Shell
* R 3.6.3

**The flow of codes as the follows:**

### 0_Degree2Radians.py
- On terminal, type
```
python 0_Degree2Radians.py
```
- It takes the data in latitude and longitude and returns it in radian form.

### 1_Data2Diagram_GUDHI_Dionysus.R
- On terminal, type
```
Rscript 1_Data2Diagram_GUDHI_Dionysus.R
```
- With two different libraries GUDHI and Dionysus2, we store intervals with persistent homology calculation from data.

### 2_Barcodes_GUDHI_Dionysus.py :
-- On terminal, type
```
python 2_Barcodes_GUDHI_Dionysus.py
```
- We use this code to visualize the output of persistent homology which is interval. The output of this code is  barcodes created according to outputs of two different libraries on the same data.

### 3_Data2Rips_Gudhi.py :
-
```
python 3_Data2Rips_Gudhi.py
```
- Here, we obtain the filtered Vietoris Rips complex with epsilon parameter by using GUDHI library.

### 4_Rips2Homological_Distance.sage
- On SageMath shell, type
```
sage 4_Rips2Homological_Distance.sage 24 0 0 0.30 0.01
```
  - sample size = 24 
  - degree of homology = 0
  - epsilon start = 0
  - epsilon end = 0.30
  - epsilon step = 0.01
- The output of this codes is homological distance matrix.

### 5_Compare_Dendrogram.R
- On terminal, type
```
Rscript 5_Compare_Dendrogram.R
```
- Hierarchical Clustering
- Mantel Test
- Tanglegram


