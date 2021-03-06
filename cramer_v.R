# cramer's v

cv.test = function(x,y) {
  CV = sqrt(chisq.test(as.table(rbind(x, y)), correct=FALSE)$statistic /
              (length(x) * (min(length(unique(x)),length(unique(y))) - 1)))
  print.noquote("Cramér V / Phi:")
  return(as.numeric(CV))
}

cv.test(pf, ipf)