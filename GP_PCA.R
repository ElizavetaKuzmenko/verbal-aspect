# Загружаем данные
data <- read.csv("/home/lizaku/PycharmProjects/verbal-aspect/GP_relative.csv", header = T, sep = ",")
n_data <- data[c("praes", "fut", "praet", "inf", "imper", "gerund", 'partcp.act.past', 'partcp.act.nonpast', 'partcp.pass.past', 'partcp.pass.nonpast')]

# Проводим анализ
GP.princomp <- princomp(an_data, scores=TRUE)
summary(GP.princomp)

# Доля дисперсии
props = round((GP.princomp$sdev^2/sum(GP.princomp$sdev^2)), 3)
# На графике
plot(GP.princomp)