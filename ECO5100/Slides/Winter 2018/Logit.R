
rm(list = ls())


# The Stock Market Data

library(ISLR); library(stargazer)
names(Smarket)
dim(Smarket)
summary(Smarket)
stargazer(Smarket)

pairs(Smarket)
cor(Smarket)
round(cor(Smarket[,-9]),2)
attach(Smarket)
plot(Volume)

# Logistic Regression

glm.fit=glm(Direction~Lag1+Lag2+Lag3+Lag4+Lag5+Volume,data=Smarket,family=binomial)
summary(glm.fit)
coef(glm.fit)
summary(glm.fit)$coef
summary(glm.fit)$coef[,4]

# odds ratios and 95% CI
exp(cbind(OR = coef(glm.fit), confint(glm.fit)))


glm.probs=predict(glm.fit,type="response")
glm.probs[1:10]
contrasts(Direction)
glm.pred=rep("Down",1250)
glm.pred[glm.probs>.5]="Up"


table(glm.pred,Direction)
(507+145)/1250

mean(glm.pred==Direction)



train=(Year<2005)
Smarket.2005=Smarket[!train,]

dim(Smarket.2005)

Direction.2005=Direction[!train]

glm.fit=glm(Direction~Lag1+Lag2+Lag3+Lag4+Lag5+Volume,data=Smarket,family=binomial,subset=train)
glm.probs=predict(glm.fit,Smarket.2005,type="response")

glm.pred=rep("Down",252)
glm.pred[glm.probs>.5]="Up"

table(glm.pred,Direction.2005)
mean(glm.pred==Direction.2005)
(77+45)/252

mean(glm.pred!=Direction.2005)
(34+97)/252


glm.fit=glm(Direction~Lag1+Lag2,data=Smarket,family=binomial,subset=train)
summary(glm.fit)
glm.probs=predict(glm.fit,Smarket.2005,type="response")
glm.pred=rep("Down",252)
glm.pred[glm.probs>.5]="Up"
table(glm.pred,Direction.2005)
mean(glm.pred==Direction.2005)
106/(106+76)
(35+106)/252
predict(glm.fit,newdata=data.frame(Lag1=c(5,-3),Lag2=c(4,-6)),type="response")

predict(glm.fit,newdata=data.frame(Lag1=c(1.2),Lag2=c(1.1)),type="response")
predict(glm.fit,newdata=data.frame(Lag1=c(5),Lag2=c(4)),type="response")
