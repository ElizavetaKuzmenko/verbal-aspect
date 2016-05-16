library("ggbiplot")

# Загружаем данные
data <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/GP_relative.csv", header = T, sep = ",")
an_data <- data[c("praes", "fut", "praet", "inf", "imper", "gerund", 'partcp.act.past', 'partcp.act.nonpast', 'partcp.pass.past', 'partcp.pass.nonpast')]

# Проводим анализ
GP.princomp <- princomp(an_data, scores=TRUE)
summary(GP.princomp)

# Доля дисперсии
props = round((GP.princomp$sdev^2/sum(GP.princomp$sdev^2)), 3)
# На графике
plot(GP.princomp)

# Для абсолютных частотностей
data <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/GP_relative.csv", header = T, sep = ",")
dataAdjusted <- data[, 3:11] - apply(data[, 3:11], 1, mean)
rownames(dataAdjusted) <- paste(data$lemma,data$aspect)
GP2.princomp <- princomp(dataAdjusted)

# simple plot
plot(GP2.princomp$scores)
text(GP2.princomp$scores, rownames(dataAdjusted))

# colored plot
g <- ggbiplot(GP2.princomp, obs.scale = 1, var.scale = 1, ellipse = TRUE, circe = FALSE, groups=data$aspect)
g <- g + theme(legend.direction='horizontal', legend.position="top")
print(g)