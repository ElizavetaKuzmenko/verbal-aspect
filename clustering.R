# cluster verbs after PCA on grammatical profiles
PCA.dist <- dist(GP2.princomp$scores)
cl_PCA <- hclust(PCA.dist)
plot(cl_PCA)
groups <- cutree(cl, k=3)
GP_groups <- cbind(data[, 3:12], groups)
x1 <- subset(GP_groups, groups==1)