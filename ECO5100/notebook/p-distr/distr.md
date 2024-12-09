
---

* chi-square distribution

* whats the difference between inference of numerical & categorical data?
* is the normal distribution for only categorical data or is it just better suited for that kind of data?

* "One-sample means with the t distribution" is just a method used when you are poor & only have access to small sample sizes.
    * what is a "sample mean"?
    * what is the "difference of two sample means"?
    * <!-- ! we are dealing with a special case of when we do not have enough samples, lets go back to when we do.  -->

* > Example 2.1 <br> Suppose your professor splits the students in class into two groups: students on the left and students on the right. If pˆL and pˆR represent the proportion of students who own an Apple product on the left and right, respectively, would you be surprised if pˆL did not exactly equal pˆR? 
    * the author is displaying that if you pick a random sample in the real world, it is natural to not have symmetry in the split.
        * consider that you walk into a stable with exactly 20 horses are equally black / white. it is highly unlikely that if you split them into 2 groups (*randomly*), that you will end up with the same proportions. -- for ex. $Group1(5w,5b)$, $Group2(5w,5b)$
            * rather what is more likely, is that on the first draw you will pick out:
                * i. $G1(3w,12b), G2(7w,8b)$
                * ii. $G1(4w,6b), G2(6w,4b)$
                * iii. $G1(1w,9b), G2(9w,1b)$
                * iv. etc.
    * this phenomena i

* how do Large Numbers Theorem & Central Limit Theorem differ? 00H 15M
    * isnt it that the > samples we have the > reliable our results are?
        * LNT:
            * flip a coin.
                1.  $results\set{H,H,T,H,T,H}$
                    * $H=4$, $T=2$, for a total of 6 rolls.
                    * of course, we know that chances of $H=0.5$ & $T=0.5$, so why does this happen?
                        * well, because they are *mutually exclusive* to each other (knowing the outcome of this roll will not ever help you predict the outcome of the next), we are unable to predict what will come next.
                            * if we observe that $results\set{...,H,H,H,}$, then we know that $(0.5)^3=0.125$. for the next flip to be H. $0.125*0.5=0.0625$. so we would be smart if we put our money on T ask a $1-0.063=0.94$ chance is pretty juicy.
                            * in fact, odds would be in our favour (on tails) if it were just ..,H,H, as $0.5*0.5=0.25$ chance is slim and $1-0.25=0.75$ looks like a easy win.
            * anyway, that had nothing to do with LNT and here i am back to defining it.
                * one important thing to note is that you are tracking a particular variable, that is part of the output space. & in simulation / re-doing the experiment you are tracking until the line probability is in some tiny region, where you have your satisfactory answer.
                    * in context of drawing an ace from a deck. $Aces=4/52$ (in deck), if you were to draw a random card from a deck, note it, reinsert it, shuffle and redraw. you are likely not to get $4/52$ on just one pass, or even two, or five... but you will need compute it many many times until convergence.
        * CLT:
            * more samples + more ? = guarenteed convergence. (00H 05M brainstorm)


* what is one / two sided hypothesis and how does it relate?
    * one-sided. you are reaching, trying to convice both yourself and the data that it indeed goes where you want it to.
    * two-sided. you are 

* how is it that a two-sided hypothesis is not bounded?
    * 

                
