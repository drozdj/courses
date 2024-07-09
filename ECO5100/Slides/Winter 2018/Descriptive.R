


# Scatterplot
rm(list = ls())

library(openintro)
data(email50);  attach(email50)

myPDF("scatterplot.pdf")
plot(num_char, line_breaks, 
     xlab="# of Characters (in thousands)", ylab="# of Lines")

dev.off()

# Mean
mean(num_char)


# Histogram
myPDF("Histogram.pdf")
hist(num_char, breaks=12, col="red")
dev.off()


# Sample Variance and Standard Deviation
var(num_char)
sd(num_char)

# Boxplot
median(num_char)
IQR(num_char)
boxplot(num_char, col="yellow")

# Barplot
t <- table(email$number)
barplot(t)
barplot(t/sum(t))        

# Pie
pie(t) 


# Contingency Table
rm(list = ls())

data(email);  attach(email)
tb<-table(spam, number); addmargins(tb)



prop.table(tb,1) # row  percentages
  
round(prop.table(tb,2),2) # column %







data(email);  attach(email)
tb<-table(spam, number); tb


prop.table(tb,1) # row  percentages

round(prop.table(tb,2),2) # column percentages

