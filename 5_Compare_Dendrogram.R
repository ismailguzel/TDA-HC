# author: ismailguzel
if (!require("vegan")) install.packages("vegan")
if (!require("repr")) install.packages("repr")
if (!require("dendextend")) install.packages("dendextend")
library(vegan)       
library(repr)
library(dendextend)

Y <- read.table("Data/Original_Coordinates.csv", header = FALSE, skip =1 , sep = ",", dec = ",")
rownames(Y) <- Y$V1
Y <- Y[-1]
Y <- Y[1:24,]
euclideandist <- dist(Y, method = "euclidean")
hc2 <- hclust(euclideandist, "single")

X = read.table("Outputs/homological_distance.txt", header = FALSE, skip = 1, sep = ",", dec = ",")
X = X[,2:length(X)]
colnames(X) <- rownames(Y)
rownames(X) <- rownames(Y)
homologydist <- as.dist(X)
hc1 <- hclust(homologydist, "single")


#To get nice representation dendrogram
png("Outputs/Dendrograms.png", width = 200, height = 110, units='mm', res = 300)
options(repr.plot.width=12, repr.plot.height=4)
par(mfrow = c(1,2))
dend1 <- as.dendrogram(hc1)
dend1 %>% 
  set("leaves_pch", 19) %>% 
  set("leaves_cex", 1) %>% 
  set("leaves_col", "blue") %>%
  set("hang_leaves", -1) %>%
  set("labels_cex", 0.8) %>%
  plot(ylab = "Epsilon" ,main = "Homological Distance", ylim=c(0.,0.1))

dend2 <- as.dendrogram(hc2)
dend2 %>%
  set("leaves_pch", 19) %>%
  set("leaves_cex", 1) %>%
  set("leaves_col", "blue") %>%
  set("hang_leaves", -1) %>%
  set("labels_cex", 0.8) %>%
  plot(ylab = "Distance" ,main = "Euclidean Distance", ylim=c(0.,0.1))
dev.off()

#To get horizontal dendrogram like barcodes
png("Outputs/Hierarchical_Barcodes.png", width = 130, height = 146, units='mm', res = 300) 
options(repr.plot.width=12, repr.plot.height=10)
dend1 %>% 
  set("leaves_pch", 19) %>%
  set("leaves_cex", 1) %>%
  set("leaves_col", "blue") %>%
  set("hang_leaves", -1) %>%
  set("labels_cex", 1) %>%
  ladderize(right = TRUE) %>%
  plot_horiz.dendrogram(horiz = TRUE, xlim=c(0.1,0.))
dev.off()

#Create a list to hold dendrograms
dend_list <- dendlist(dend1, dend2)

# To visually compare two dendrograms
png("Outputs/Tanglegram.png", width = 250, height = 110, units='mm', res = 300)
options(repr.plot.width=12, repr.plot.height=8)
nice_tanglegram <-dend_list %>% 
		untangle() %>%
		tanglegram(highlight_distinct_edges = FALSE,
        	common_subtrees_color_lines = TRUE,
        	common_subtrees_color_branches = TRUE,
        	margin_inner = 5,
        	margin_outer = 3
    		)
dev.off()

# To get entanglement of nice_tanglegram
round(entanglement(nice_tanglegram, L=2), 2 )


#For a confidence level, use the "Mantel Test" from package vegan.
manteltest <- mantel(cophenetic(hc1), cophenetic(hc2)) 
#to get output.file
out <- capture.output(manteltest)
cat("Test Result", out, file="Outputs/testresult.txt", sep="\n")
