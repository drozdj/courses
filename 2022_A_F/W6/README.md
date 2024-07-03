# Week 6: Interpretability 

* how do we visualize the features represented by individual neurons?
    * <!-- todo: -->
* how do neural circuits build up representations fo high-level features out of lower-level features?
    * <!-- todo: -->
* how can we use interpretability to modify neural weights in meaningful ways?
    * <!-- todo: -->
* how can we use interpretability to understand AlphaZero's development of human chess concepts?
    * <!-- todo: -->
<!-- ! these are the key questions to pickup in this topic -->
---

* visualizing features of individual neurons
    * why are we not visualising connections between multiple neurons but only focused on one?
        * <!-- todo: -->
    * neuron-level mechanistic interpretability
        * <!-- todo: -->
    * concept-based interpretability
        * <!-- todo: -->
* feature visualization
    * features
        * low level
            * edges, vertical/horizontal lines
        * high level (speculative, community is split between believing these exist) <!-- [ ] find resource on this -->
            * ears, noses, eyes
* regularization
    * highlights the neurons that we can extract most value out of (most comprehensable, dense with information) <!-- [ ] encode this well on mindmap -->
* factual associations
    * <!-- todo: -->
    * localization
        * traceable through the NN.
            * likely because we don't want neurons that trigger *alot* as it can get confusing to pinpoint what is really happening.   
            * (kinda like in markov decision processes, if you have the current state & previous state, then they contain all of information of previous states.) <!-- [ ] how does that work actually? is the previous state holding onto information of *all* previous states? -->
* circuits
    * collection of model components
        * attention heads
        * neurons
        * feed-forward layers