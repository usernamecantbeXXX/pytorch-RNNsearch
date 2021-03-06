# Neural Machine Translation by Jointly Learning to Align and Translate

This part of the repo contains my paper implementation and training code for german to english translation using the **RNNsearch** model. 

## Environment 

- OS System: Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-161-generic x86_64)
- CPU: 80C (2 * Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz)
- Memory: 256Gi
- GPU: 4 * NVIDIA A40
- Anaconda3
- Python 3.8
- Pytorch 1.9.1
- CUDA 11.1

## Training

Before you start training you should make sure, that you have installed all the packages from the `requirements.txt` and  downloaded the spacy tokenizers:
```shell
conda create -n pytorch-RNNsearch python=3.8 anaconda
conda activate pytorch-RNNsearch

conda install -c conda-forge spacy
conda install -c conda-forge cupy

python -m spacy download en_core_web_sm
python -m spacy download de_core_news_sm

pip install -U torch==1.9.1+cu111 torchvision==0.10.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/  --use-deprecated=legacy-resolver
```
The languages used in this implementation is in file `dataset.py`.

Hyperparameters configurations are in file`./config.py`. 

Execute the command below then start training the model.

```shell
python train.py --config="config.yaml"
```

## Trained Model

I've trained a small model for 50 epochs. And the training process recorded in the log file `./train.log`.

```shell
...
Epoch: 50 | Time: 17m 20s
        Train loss: 2.7758515714599787 | Train perplexity: 16.052290849710765
        Val loss: 4.9955442036901205 | Val perplexity: 147.7533314164854
Best model from epoch 33 is loaded for testing.
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1568/1568 [00:23<00:00, 67.80it/s]
| Test Loss: 4.218 | Test PPL:  67.925 |
```

And The model and the corresponding config file locations are `./experiments/2021-11-21_IWSLT2017/best.pth` and `./experiments/2021-11-21_IWSLT2017/config.yaml`.

## Quantitative Results

### Run the Results

Start the JupyterNote and Run the `demo.ipynb` file to get the results.

```shell
conda install -n pytorch-RNNsearch ipykernel
ipython kernel install --user --name=pytorch-RNNsearch
jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root
```

### Results

```
Length of vocab [de - IWSLT2017]: 16713
Length of vocab [en - IWSLT2017]: 14016


Load model checkpoint: /home/domp/pytorch-RNNsearch/experiments/2021-11-21_IWSLT2017/best.pth

Seq2Seq(
  (encoder): Encoder(
    (embedding): Embedding(16713, 256)
    (rnn): GRU(256, 512, bidirectional=True)
    (fc): Linear(in_features=1024, out_features=512, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
  (decoder): Decoder(
    (attention): Attention(
      (attn): Linear(in_features=1536, out_features=512, bias=True)
      (v): Linear(in_features=512, out_features=1, bias=False)
    )
    (embedding): Embedding(14016, 256)
    (rnn): GRU(1280, 512)
    (fc_out): Linear(in_features=1792, out_features=14016, bias=True)
    (dropout): Dropout(p=0.5, inplace=False)
  )
)

============================================================
SRC:	Vor einigen Jahren , hier bei TED , stellte Peter unk einen unk namens " Die unk " vor .
TGT:	Several years ago here at TED , Peter unk   introduced a design challenge   called the marshmallow challenge .
------------------------------------------------------------
PRED:	A couple years ago , at TED TED , Peter Peter unk a unk called " The unk unk . "
============================================================
SRC:	Die Idee ist ziemlich einfach . unk müssen die unk unk Struktur mit 20 unk , ca. 1 m Klebeband , ca. 1 m Faden und einem Marshmallow bauen .
TGT:	And the idea 's pretty simple :   unk of four have to build the tallest free - standing structure   out of 20 sticks of spaghetti ,   one yard of tape , one yard of string   and a marshmallow .
------------------------------------------------------------
PRED:	And the idea is pretty simple . unk , to have to unk the unk unk structure of 20 - 20 - , , about a a mile , about a a of a .
============================================================
SRC:	Der Marshmallow muss oben drauf sein .
TGT:	The marshmallow has to be on top .
------------------------------------------------------------
PRED:	The the needs to be be on top .
============================================================
SRC:	Und , obwohl es wirklich einfach scheint , ist es tatsächlich richtig schwer , weil es Leute drängt sehr schnell zusammenzuarbeiten .
TGT:	And , though it seems really simple , it 's actually pretty hard   because it forces people   to collaborate very quickly .
------------------------------------------------------------
PRED:	And even though it 's really simple , it 's really really hard really hard , because it 's very very close to people very quickly .
============================================================
SRC:	Und so dachte ich , dass dies eine interessante Idee ist und ich habe es in einen unk verwandelt .
TGT:	And so , I thought this was an interesting idea ,   and I unk it into a design workshop .
------------------------------------------------------------
PRED:	And so I thought that this is an interesting idea , and I 've turned into a unk . .
============================================================
SRC:	Es war ein riesiger Erfolg .
TGT:	And it was a huge success .
------------------------------------------------------------
PRED:	It was a huge success .
============================================================
SRC:	Seitdem habe ich ungefähr 70 Workshops weltweit durchgeführt , mit Studenten , unk und Architekten , sogar mit unk der unk und da ist etwas an dieser Aufgabe , was tiefe Eindrücke in die Natur der Zusammenarbeit ermöglicht und ich möchte einige davon mit Ihnen teilen .
TGT:	And since then , I 've conducted   about 70 design workshops across the world   with students and designers and architects ,   even the unk of the Fortune 50 ,   and there 's something about this exercise   that reveals very deep lessons   about the nature of collaboration ,   and I 'd like to share some of them with you .
------------------------------------------------------------
PRED:	Since since I 've done about 70 around the world , students students , unk and architects , even with the unk of the , and there 's something of creating a deep - of - of nature of the and and I want to share some of those of you .

TRANSLATION
==================================================
SOURCE: Mein Name ist Johann Gerberding und ich programmiere sehr gern und trainiere gern Machine Learning Modelle . <eos>
--------------------------------------------------
PREDICTION: My name is unk unk , and I love like very unk and unk unk to unk models .
```
![png](demo_files/demo_16_1.png)
```
TRANSLATION
==================================================
SOURCE: Er liebt Bücher und gutes Essen mehr als alles andere . <eos>
--------------------------------------------------
PREDICTION: He loves books and and food food more than anything else .
```
![png](demo_files/demo_18_1.png)

```
TRANSLATION
==================================================
SOURCE: Mathematik und Physik waren seine liebsten Fächer in der Schule . <eos>
--------------------------------------------------
PREDICTION: unk and physics were the most unk in school school .
```
![png](demo_files/demo_19_1.png)
```
TRANSLATION
==================================================
SOURCE: Peter liebt es mit dem Fahrrad zur Arbeit zu fahren . <eos>
--------------------------------------------------
PREDICTION: Peter was trying to work with the bicycle .
```
![png](demo_files/demo_20_1.png)
```
TRANSLATION
==================================================
SOURCE: Künstliche Intelligenz und programmieren macht einfach Spaß . <eos>
--------------------------------------------------
PREDICTION: unk intelligence and and simply simply fun .
```
![png](demo_files/demo_21_1.png)

# Bleu Score

Down below I evaluate the model on the test set based on the Bleu Score (https://aclanthology.org/P02-1040.pdf) using two different ngram values, 3 & 4. The Bleu Score is often used for evaluation in Neural Machine Translation.

```
bleu4
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1568/1568 [14:45<00:00,  1.77it/s]
16.33

bleu3
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1568/1568 [15:02<00:00,  1.74it/s]
25.19
```


## References

Here are some references I used:

* [Original Paper](https://arxiv.org/pdf/1409.0473.pdf)
* [PyTorch Seq2Seq](https://github.com/bentrevett/pytorch-seq2seq.git)
* [johanngerberding-machine-learning-playground](https://github.com/johanngerberding/machine-learning-playground.git)
