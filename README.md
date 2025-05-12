
# Supporting Files

This is about formal models and code re the AKMA protocol's PCS proofs and implementation.

# ProVerif

Our ProVerif file models the  key-derivation chains as per the PCS framework.

Our ProVerif models here can be run in ProVerif versions built from commits after  commit  "2b7d52ede6598bf62b5dd59243297c8b9415b763" (25 April 2023). 
This means that the last release version of ProVerif 2.04, and the current release version of ProVerif 2.05 work.
(When we constructed our ProVerif model, we found a bug in early ProVerif 2.04 around the theory to do with integers, so one needs ProVerif versions newer than when the fix  was applied for the bug we found.) 

The current version of ProVerif is 2.05, so one can use that with general ease. If you do not use 'opam' or ready builts, then do

E.g.,

`git clone https://gitlab.inria.fr/bblanche/proverif.git`

`cd proverif`

`./build`

To run any ProVerif file, in the local installation of  ProVerif, in the  'proverif'  folder containing the build as per the above, do:
./proverif filename

E.g., 

`./proverif PCS_LISTS.pv`


To run our model, we recommend a machine with at least 32GB of RAM.

Note that for one goal, the translation in Horn clauses generates about 23,000  rules, but in ProVerif 2.04 or ProVerif 2.05, on a laptop 2.3 GHz Quad-Core Intel Core i7, with 32GB RAM, the whole verification finishes in less than 4 minutes.

# Tamarin

For our models, we used the latest release Tamarin, v.1.8.  See, [Tamarin](http://tamarin-prover.github.io/)

We provide the following Tamarin-relevant files:
 
 -- `PCS_LISTS_nats.spthy`:  this is our Tamarin model that includes a reference to an Tamarin oracle we built, to automate  our proofs
 
 This  file contains the  key-derivation chains for the  PCS model in the submitted paper, written in Tamarin. 
 
 -- `PCS_LISTS_nats_manual.spthy`: this is a saved, manual proof  of the lemma "leaks_can_happen" in the model above, without the oracle.
 
 -- `oracle_pcs.py`: this is the Tamarin oracle file, to support the proofs in the Tamarin model aforementioned. Ensure that the oracle is executable, i,e., if necessary execute `chmod +x oracle_pcs.py`


### Running the Tamarin Models


To prove all lemmas  automatically, using the above oracle (which is referenced from within the `PCS_LISTS_nats.spthy` file), type the below 
in a terminal:

`tamarin-prover PCS_LISTS.spthy --proof`


To either load the manual  proof of the lemma "leaks_can_happen" 
provided in our PCS_tamarin_nats_manual.spthy 
file or do the proof yourself in the PCS_LISTS_nats.spthy file, interactively, do this. In a terminal, go to the folder where you saved our files, 
and  type:

`tamarin-prover interactive . -Dmanual`

# reOpen5GCore

There are two files within the folder we submitted with this name. They contain the code for the 
experimentation that was carried out on the Fraunhofer 
[Open5GCore](https://www.open5gcore.org/), via our additions to the NEF 
containing the AKMA code. 

Unfortunately, due to copyright we cannot share 
the code for the Open5GCore. But, for these files to run, one 
would need an instance of the Open5GCore.

### 1) akma_experiments.py

This file was used to create the baseline timings for a number of AKMA 
calls made to the NEF.  To 
run this file, you can execute the following command in a terminal.

```python code
python akma_experiments.py
```

### 2) akmareg_experiment.py

Inside of this file contains experiments w.r.t. our new, so-called AKMAReg, where we  make an extra registration call for each AKMA call.  To run this file, you can execute the following command in a 
terminal.

```python code
python akmareg_experiment.py
```
