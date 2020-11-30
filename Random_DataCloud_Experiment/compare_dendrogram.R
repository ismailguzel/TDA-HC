if (!require("vegan")) install.packages("vegan")
if (!require("repr")) install.packages("repr")
if (!require("dendextend")) install.packages("dendextend")


library(vegan)
library(gtools)


setwd(".../Random_Experience/Outputs")
my_original_outputs <- Sys.glob("output_original_*.txt")
my_sage_outputs <- Sys.glob("output_sage_*.txt")
my_original_outputs <- mixedsort(my_original_outputs)
my_sage_outputs <- mixedsort(my_sage_outputs)


test_statistic = c()
test_significance = c()

for (fileno in seq(1:100) ){
  X = read.table(my_sage_outputs[fileno], header = FALSE, skip = 1, sep = ",", dec = ",")
  X = X[,2:length(X)]
  colnames(X) <- seq(1,length(X))
  homologydist <- as.dist(X)
  hc1 <- hclust(homologydist, "single")
  Y <- read.table(my_original_outputs[fileno], header = FALSE, skip =1 , sep = ",", dec = ",")
  Y <- Y[,2:length(Y)]
  euclideandist <- dist(Y, method = "euclidean")
  hc2 <- hclust(euclideandist, "single")
  
  manteltest <- mantel(cophenetic(hc1), cophenetic(hc2))
  test_statistic[fileno] <- manteltest$statistic
  test_significance[fileno] <- manteltest$signif
  
}

write.csv(test_statistic, file = "Mantel_outputs/test_statistic.csv")
write.csv(test_significance, file = "Mantel_outputs/test_significance.csv")

