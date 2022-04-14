# Google Foobar Challenge

Recently while I was brushing up on my python knowledge using Google search, I received a suprise message which appears under the search bar.
It was the famous Google Foobar Challenge.
In this repository, I document my experience and the solutions to the challenges.

If you have any comments/improvements about the code, please feel free to contact me at my email (decrypt at decryptology.net).
I would absolutely love to learn more! :)

![Google foobar challenge](https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/GoogleFoobarChallenge.png)

## Level 1 - 1 Challenge

### I Love Lance & Janice
Pretty easy challenge. 
Just need to decipher the encrypted text and understand how to convert the alphabets into its encrypted equivalent.


## Level 2 - 2 Challenges

### Elevator Maintenance
Basically we need to sort the version numbers. Recursion is used here.
It is my first time implementing merge sort which is a Divide and Conquer algorithm.

### Ion Flux Relabeling
Tree traversal. I have never implemented binary tree in my work. Recursion is also used again.
This took me a while because I have to switch back to learning mode and understand the binary tree.
I used the brute force method here which is populating the number one by one starting from 1 to max node value(2^h-1)
This took a lot of unnecessary scanning to insert the value sequentially although I do not continue to populate once I get the answer.
Actually after drawing a few binary trees, I notices that I can recursively generate the tree from top to bottom.
Left child node is always (2^3-1) and right child node is always (parent node value -1).
<img src="https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/ion_flux_relabeling.PNG" width="20%" height="20%">


## Level 3 - 3 Challenges (Notice that the number of challenges matches the level number)

### The Grandest Staircase Of Them All
Recursion again. Took me a while to figure out the "pattern".
I also notice that in this level it is not enough just to have a solution which provide the correct answer.
If your solution is not fast enough, it will fail the test cases.
I was stumped for a while because my code was able to provide the correct value but it failed all the test cases.
After trying with a hard coded solution (if n == 3: return 1) :P, it passes one of the test case which leads me to believe that speed is one of the hidden requirement in this level.
Cleaned up the code by reducing unecessary logic and add caching. Manage to passed all the test cases. :)

