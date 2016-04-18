library("ca")

# slice the data
part_data <- data[0:500, 3:10]

# different lambdas; this is for JCA
jca <- mjca(part_data, nd = 2, lambda = "JCA")

# eigenvalues
jca$sv^2

# data frame for ggplot
cats <- apply(part_data, 2, function(x) nlevels(as.factor(x)))
jca_vars = data.frame(jca$colcoord, Variable = rep(names(cats), cats))
rownames(jca_vars) = jca$levelnames

# plot
ggplot(data = jca_vars, 
       aes(x = X1, y = X2, label = rownames(jca_vars))) +
  geom_hline(yintercept = 0, colour = "gray70") +
  geom_vline(xintercept = 0, colour = "gray70") +
  geom_text(aes(colour = Variable)) +
  ggtitle("MCA plot of variables using R package ca")