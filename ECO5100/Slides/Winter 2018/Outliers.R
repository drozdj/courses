
rm(list = ls())
dev.off()
library(MASS)
library(ISLR)
library(stargazer)

data(Boston)

lm.fit=lm(medv~lstat,data=Boston)
summary(lm.fit)

plot(predict(lm.fit), rstudent(lm.fit))
plot(hatvalues(lm.fit))
which.max(hatvalues(lm.fit))
