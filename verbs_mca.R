data <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/feature_matrix.csv", header = T, sep = ",")
library("devtools")
library("FactoMineR")
library("factoextra")
part_data <- data[0:500, 3:10]
mca <- MCA(data[0:500,])
fviz_mca_ind(mca, col.ind="cos2", geom = "point", 
             jitter = list(width = 0.2, height = 0.2)) +
  scale_color_gradient2(low="white", mid="blue",
                        high="red", midpoint=0.4)+ theme_minimal() +
  labs(title = "MCA", x = "Dim.1", y ="Dim.2" )