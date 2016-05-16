absGP <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/macro_GP_absolute_overlap.csv", header = T, sep = ",")
pf <- unlist(c(macro_GP[1,2:10]))
ipf <- unlist(c(absGP[2,2:10]))
chisq.test(as.table(rbind(pf,ipf)))