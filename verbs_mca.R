library("devtools")
library("FactoMineR")
library("factoextra")

data <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/feature_matrix.csv", header = T, sep = ",")

# slice the data
part_data <- data[0:500, ][c("aspect", "form", "transitivity", "tense", "mood", "voice")]

mca <- MCA(part_data)

# plot
fviz_mca_ind(mca, col.ind="cos2", geom = "point", 
             jitter = list(width = 0.2, height = 0.2)) +
  scale_color_gradient2(low="white", mid="blue",
                        high="red", midpoint=0.4)+ theme_minimal() +
  labs(title = "MCA", x = "Dim.1", y ="Dim.2" )

# plot with difference shapes with regard to aspect
grp <- as.factor(part_data[, "aspect"])
fviz_mca_ind(mca, label="none", habillage=grp)

# top 20 contributions
fviz_mca_ind(mca, select.ind = list(contrib = 20))

# Select by names
fviz_mca_ind(mca,
             select.ind = list(name = c("44", "38", "53",  "39")))

# plot variables with contributions indication
fviz_mca_var(mca, col.var = "contrib")+
  scale_color_gradient2(low = "white", mid = "blue",
                        high = "red", midpoint = 2) +
  theme_minimal()

# Select the top 10 contributing variable categories
fviz_mca_var(mca, select.var = list(contrib = 10))