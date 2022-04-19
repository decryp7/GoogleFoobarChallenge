# Google Foobar Challenge

Recently while I was brushing up on my python knowledge using Google search, I received a surprise message whether I want to take up an interesting challenge. It was the famous Google Foobar Challenge. I have heard about this interesting way that Google is using to hire engineers very long ago but I have never experienced it myself. So I was very surprised and very excited to try this challenge when I received it. It is said that up to now, no one know the magic steps to trigger this magical challenge. **:O**  

In this repository, I document my experience solving the Google Foobar Challenge. All my solutions are coded using python.  

If you have any comments/improvements about my solutions, please feel free to contact me at my email (decrypt at decryptology.net).  
I would absolutely love to learn more! **:)**  

![Google foobar challenge](https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/GoogleFoobarChallenge.png)  

## Level 1 - 1 Challenge

### I Love Lance & Janice
Pretty easy challenge. Just need to decipher the encrypted text and understand how to convert the alphabets into its encrypted equivalent.  


## Level 2 - 2 Challenges

### Elevator Maintenance
Basically we need to sort the version numbers. Recursion is used here. It is my first time implementing merge sort which is a Divide and Conquer algorithm.  

### Ion Flux Relabeling
Tree traversal. I have never implemented binary tree in my work. Recursion is also used here. This took me a while because I have to switch back to learning mode and understand the binary tree. I used the brute force method here which is populating the number one by one starting from 1 to max node value(2^h-1). *h is height of tree* Actually after drawing a few binary trees, I noticed that I can recursively generate the tree from top to bottom. Left child node is always (parent node value - 2^h) and right child node is always (parent node value -1). Definitely there is a lot of room for improvement in my current solution.  

My thought was only to pass all the test cases and submit. **:P**  

<img src="https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/ion_flux_relabeling.PNG" width="50%" height="50%">  

*Received an invitation code which I can refer a friend to this challenge after completing level 2.*  

## Level 3 - 3 Challenges (Notice that the number of challenges matches the level number, I cannot imagine 4 or 5 questions later per level. **:(** )

### The Grandest Staircase Of Them All
Recursion again. Took me a while to figure out the "pattern". I also noticed that in this level it is not enough just to have a solution which provides the correct answer. If your solution is not fast enough, it will fail the test cases. I was stumped for a while because my code was able to provide the correct value but it failed all the test cases. After trying with a hard coded solution (if n == 3: return 1) **:P**, it passes one of the test case which leads me to believe that speed is one of the hidden requirement in this level. Cleaned up the code by reducing unecessary logic and added caching. And managed to passed all the test cases this time round. **:)**  

But I wondered if my solution is correct. Looked like some complicated formula may be involved. **:(**  

<img src="https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/the_grandest_staircase_of_them_all_1.PNG" width="50%" height="50%">
<img src="https://dev.decryptology.net/decryp7/GoogleFoobarChallenge/raw/branch/master/the_grandest_staircase_of_them_all_2.PNG" width="50%" height="50%">
