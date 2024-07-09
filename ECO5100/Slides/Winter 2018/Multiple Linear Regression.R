
rm(list = ls())
dev.off()
library(MASS)
library(ISLR)
library(stargazer)

# Multiple Linear Regression

lm.fit=lm(medv~lstat+age,data=Boston)
summary(lm.fit)
lm.fit=lm(medv~.,data=Boston)
summary(lm.fit)
library(car)
vif(lm.fit)
lm.fit1=lm(medv~.-age,data=Boston)
summary(lm.fit1)
lm.fit1=update(lm.fit, ~.-age)

# Interaction Terms

summary(lm(medv~lstat*age,data=Boston))


# Non-linear Transformations of the Predictors

lm.fit2=lm(medv~lstat+I(lstat^2))
summary(lm.fit2)
lm.fit=lm(medv~lstat)
anova(lm.fit,lm.fit2)
par(mfrow=c(2,2))
plot(lm.fit2)
lm.fit5=lm(medv~poly(lstat,5))
summary(lm.fit5)
summary(lm(medv~log(rm),data=Boston))

dev.off()

# Qualitative Predictors

fix(Carseats)
names(Carseats)
lm.fit=lm(Sales~.+Income:Advertising+Price:Age,data=Carseats)
summary(lm.fit)
attach(Carseats)
contrasts(ShelveLoc)