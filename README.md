# multiple_sequence_alignment_genetic_algorithm



MULTIPLE SEQUENCE ALIGNMENT 
WITH
 GENETIK ALGORITHM



Problem:
in genetics we try to find the relation between two or more sequences of DNA or Proteins, but it is not always easy to see the relation between sequences because there is a huge number of combination of alignments that can be observed.
Also the similarity between codons or neuclutids in the sequences are calculated according to an adjacency matrix called PAM which is a score matrix used here.
Let us consider this example for explanation:
(a)   AIWQH
      :  ::
      AL-QH

(b)   AIWQH
      :  ::
      A-LQH

For first glance we would assume that the score of matching of this two alignments is the same, because there are three matches; A, Q and H in both. nevertheless, the alignment a is better because isoleucine (I) and leucine (L) are similar sidechains and will have a higher score in PAM matrix, on the contrary of tryptophan (W) and leucine (L) which has a very different structure. [1]
This example was for a two sequences, and it is easy to observe or calculate the similarity of it, usually dynamic programming is used with pair sequence alignment with an optimal solution.
But with the increasing number of sequences the complexity of dynamic programming becomes nk where k is number of sequences.
And therefore we use genetic algorithm as a solution to this problem, knowing that it does not guarantee an optimal solution.




The Algorithm: [2]
1-generate a k number of random alignments.
2-sequences might be different in lengths so add a ‘-‘ symbol to represent a       mismatch to the terminal of sequences making all sequences of the same length of the longest sequence.
3-The gaps are added randomly to the start and the end of the sequences
---WGKVNVDEVGGEAL-
--WDKVNEEEVGGEAL--
-WGKVGAHAGEYGAEAL-
--WSKVGGHAGEYGAEAL

Evaluation:
the evaluation of the alignment is done according to the PAM250 matrix using the method of sum of pairs, and that is by comparing the letters(codons) in each two sequences of all combination and then summing the scores. [3]
 
also considering gap penalty which is a hyper parameter.
4- after calculating the score for each alignment in the population, we select the best 50% of the population directly for reproduction. The other 50% are selected stochastically according to their score; higher score means higher probability to be selected.



Reproduction:
Reproduction are done slightly different for this algorithm, after selecting best individuals from population we reproduce by changing the gaps place in the sequences randomly, after doing this for all alignments we calculate the alignment score and repeat this operation for a specified number of generations.
does not work with simple mutation & crossover!
We do consider regions that resembles each other and try to keep these regions in the next generations. [2]
 
For each generation we select the best scored alignment, after the termination condition is met we select the best scored alignment among the best alignments to be our best solution but not the optimal.

Examples of application:
4 sequences with population size of 20 and 10000 generation:
SMGATSIMGAT
GATGAT
ACTGATACTGATACT
CGATCCGAT

after alignment:
 
the score:  129


5 sequences with population size of 20 and 10000 generation:
SMGATSIMGAT
GATGAT
ACTGATACTGATACT
CGATCCGAT
LGATSMICGAT
after alignment:
 
the score:  257

6 sequences with population size of 20 and 10000 generation:
SMGATSIMGAT
GATGAT
ACTGATACTGATACT
CGATCCGAT
LGATSMICGAT
ISGATMYSAT
after alignment:
 



Kaynakça

[1] 	www.bioinformatics.org/, "www.bioinformatics.org/," [Online]. Available: https://www.bioinformatics.org/wiki/Scoring_matrix.
[2] 	Koza, «Multiple sequence alignment by genetic algorithm,» W.Shreiner, 2005. 
[3] 	D. a. Katoh, «Scoring function: Sum-of-Pairs,» 2008. [Çevrimiçi]. Available: www.cs.cmu.edu/~durand/03-711/2012/Lectures/MSA2-12.pdf.



