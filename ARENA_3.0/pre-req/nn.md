# Neural Networks

---
NOTE: this is primarily for Artificial NN, not the biological ones.


(Answer questions on NN. 00M 30M)
* what are they used for? *forecasting* 
    * machine learning
        * supervised learning
            * we would like to feed in some input without a label and have the machine tell is the label. 
                in which case: we have some data w/ labels. we have some data w/o labels. we feed in the latter, and cross our fingers for it to predict it well. (after awefully many examples)
        * unsupervised learning
    * llm's
        * predicting the next word in a sequence of words
            * fun fact: the machine isn't actually thinking... rather what it is doing it looking back at all of the examples that *look* similar to the one it is currently facing and gives the one that is most likely to come next (given a probability distribution). this is why you may notice that when you ask *(older)* GPT arithmatic it completely outputs gibberish. 
                * what is GPT?
                    * it is a transformer model that was introduced in the paper Attention is all we need (by DeepMind) just before 2020.
                    * some interesting properties to note:
                        * residual strean: this is the main flow of information, thing of it as a river travelling $A \to B$. on occasion, some rocks are taken out of that river and tampered with, but they always get thrown back in (potentially a tad altered).        
* why do we need them?
    * they speed up (otherwise *very* monotonous) computation -- albeit very elementary atm. 
        * give an example ^.
            * think that
        * how do they do this?
            * by brute-forcing their way to success
            * they pick up on *features*
* how do they apply to ai?
    * when it comes to foreseeing  
* why are we covering them in this course?
    * we will be using llms
* what is their history? how did they come to be?
* are there any alternative approaches?
    * reinforcement learning
        * it should be noted. in envs. that involve constanly changing states (such as video games, robotics irl, etc.), NNs suffer. in this case, we will always pick RL b
* do we understand their internals?
* are they anything like the human brain?
    * in terms of their difficulty, yes. in terms of their learning process, we still lack understanding in both neuroscience & ANN to consider this 
* who invented them?
    * did they have any issues? any pushback when first introduced?
* do they have limitations?
    * have we reached them?
* are they similar to any other phenomena in terms of their growth?
* can they be applied to areas that haven't yet been explored?
* can we regulate them?
    * considering that Yampolsky published a paper{link}, that detailed their ability to register as LLCs (meaning they have personal rights)