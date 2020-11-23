# author: ismailguzel
library(TDA)
# Upload the dataset from Data directory
Dataset <- read.csv("Data/Original_Coordinates.csv", header = TRUE , sep = ",", dec = ",")
Dataset <- Dataset[-1]
Dataset <- Dataset[1:24,]
Dataset$x <- as.matrix(sapply(Dataset$x, as.character))
Dataset$x <- as.matrix(sapply(Dataset$x, as.numeric))
Dataset$y <- as.matrix(sapply(Dataset$y, as.character))
Dataset$y <- as.matrix(sapply(Dataset$y, as.numeric))

# Choose epsilon and maximum dimension
maxscale <- 0.30 # epsilon
maxdimension <- 2 # components and loops

# Construct the Rips Complex via GUDHI
Rips_Gudhi <- ripsFiltration(Dataset,
                             maxdimension,
                             maxscale,
                             dist = "euclidean",
                             library = "GUDHI")
# Construct the Rips Complex via Dionysus
Rips_Dionysus <- ripsFiltration(Dataset,
                             maxdimension,
                             maxscale,
                             dist = "euclidean",
                             library = "dionysus")
Filt_Gudhi <- filtrationDiag(Rips_Gudhi, maxdimension, library = "GUDHI")
Filt_Dionysus <- filtrationDiag(Rips_Dionysus, maxdimension, library = "dionysus")

# Save the diagrams outputs
write.csv(Filt_Gudhi$diagram,"Outputs/gudhi_bd.csv")
write.csv(Filt_Dionysus$diagram,"Outputs/dionysus_bd.csv")
