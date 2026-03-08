# Programming Assignment 2: Greedy Algorithms

## Student Information
- Name: Imaan Edhi
- UFID: 28443010

## Language Used
Python 3

## Repository Structure

src/
data/
tests/
README.md

## How to Run

From the project root folder, run:

python3 src/main.py data/example.in

You can also run the test files:

python3 src/main.py data/file1.in
python3 src/main.py data/file2.in
python3 src/main.py data/file3.in

## Input Format

Input files follow this format:

k m
r1 r2 r3 ... rm

Where:

k = cache capacity

m = number of requests

r1 ... rm = sequence of integer requests

## Output Format

The program prints:

FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>

## Written Component
## Question 1: Empirical Comparison

I tested the program on three input files containing at least 50 requests.

Input File	k	 m	FIFO LRU	OPTFF
file1.in	  3	 50	 44	  46	 29
file2.in	  4	 50	 43	  45	 25
file3.in	  3	 50	 35	  37	 23

Comments

OPTFF always produced the fewest cache misses. This is expected because OPTFF uses knowledge of future requests and is known to be optimal for offline caching.

FIFO generally performed worse than OPTFF because it evicts items based only on arrival order, which can remove items that will soon be requested again.

LRU attempts to approximate optimal behavior by evicting the least recently used item. In these experiments, LRU was slightly worse than FIFO for some inputs but still consistently worse than OPTFF.

## Question 2: Bad Sequence for FIFO

For k = 3, there exists a sequence where OPTFF incurs fewer misses than FIFO.

Example request sequence:

1 2 3 4 1 2 5 1 2 3 4 5

Results:

FIFO  : 9
LRU   : 10
OPTFF : 7

OPTFF performs better because it evicts the item whose next request is farthest in the future, while FIFO evicts the item that entered the cache earliest, regardless of future usage.

## Question 3: Proof that OPTFF is Optimal

Let OPTFF be the Farthest-in-Future cache eviction algorithm. Let A be any offline algorithm that knows the full request sequence.

Consider the first step where A and OPTFF choose different items to evict. Up to that point both algorithms have processed the same requests and therefore have identical cache contents.

Suppose OPTFF evicts item e and algorithm A evicts item f instead. By definition of OPTFF, item e is the one whose next request occurs farthest in the future or never occurs again. Therefore f must be requested no later than e.

If we modify algorithm A so that it evicts e instead of f, the number of misses cannot increase, because keeping f in the cache is always at least as useful as keeping e.

Using this exchange argument, we can transform algorithm A step by step so that it makes the same eviction decisions as OPTFF without increasing the number of misses.

Therefore OPTFF incurs no more misses than any other offline algorithm for the same request sequence. Hence OPTFF is optimal.