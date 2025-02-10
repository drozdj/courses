
## A Comprehensive Survey on Pre-trained Foundational Models
### Challenges and Open Problems (in PFM research)
- ⬜️how do *Qiu et al.* [5](https://arxiv.org/abs/2003.08271)recognize that DNNs can be attacked by adversarial samples, which potentially leads the model to produce false predictions.

- ⬜️how does a tiny interference of the original input potentially mislead the pretraining model to produce specific false predictions?

- ⬜how did *Jin et al.* [262](https://arxiv.org/abs/1907.11932) successfully attack BERT, CNN and RNN via generation of natural adversarial examples?

- ⬜️how do humans false statistical information in the dataset contribute the PFM to make wrong predictions? ie how is BERT in *Niven et al.* [33](https://arxiv.org/abs/1907.07355) limited in reasoning tasks and thus *dramitically* affected in its performance?

- ⬜️how does *Kurita et al.* [266](https://arxiv.org/abs/2004.06660) weight-poisoning attack (where pretrained weights are injected), thus after the pre-training stage, the backdoor is exposed?

- ⬜️how does *Schuster et al.* [267](https://arxiv.org/abs/2001.04935) show that the "meaning" of new words can be controlled via changing weight parameters?

- ⬜️how has the human-in-the-loop method (*Wallace et al.* [31](https://arxiv.org/abs/1809.02701), *Nie et al.* [32](https://arxiv.org/abs/1910.14599)) been used to generate natural and more efficient adversarial samples?

- ⬜how can we query massive LMs to recover specific training examples?

- ⬜how are we going about creating multimodel datasets?

- ⬜️primary method driving model design is scaling: -- how do we make the trade-off for performance?
    - i) increase data
    - ii) improve computation power
    - iii) design training procedure

- ⬜how do the 'linear characteristics' in DNNs make them vulnerable to adversarial inputs?

- ⬜️how can we improve the robusntness of PFMs in NLP?

- ⬜️how might we perform an model anti-attack for adversarial examples in NLP which are aimed to produce specific false predictions?

- ⬜️why does the *Saturation Phenomena* as demonstrated by Goole Research in *Abnar et al.*[274](https://arxiv.org/abs/2110.02095) exist? -- that better higher training accuracy with more data on upstream tasks doesn't translate to better performance on target downstream tasks.

- ⬜️whats the issue with addressing the relationship between pretext tasks and downstream tasks?

- ⬜️essentially, all task-based graph for pretrained models are independent, such that nodes aren't reused, thus making it impossible to pretrain (by adding more data). How do we address this?

- ⬜️why do the authors find it crucial that we utilize graph data for multimodal pretraining (in addition to text and image)?

- ⬜️why do the authors conclude that single-transformer models attract more foucus that other types of unified PFMs?

- ⬜️how has BEiT-3 in *Wang et al.* [29](https://arxiv.org/abs/2208.10442) shown that multi-modal between vision-language tasks is a promising research direction?

- ⬜️other than ChatGPT which uses RLHF fine-tuning in NLP, what are similar directions in the fields of CV and GL?
