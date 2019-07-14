# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables (24 points), blockchain (12 points) and a short interview (20 points). There is also a stretch goal in the blockchain section which should only be attempted after the rest of the problems have been completed.

## Interview Questions

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following three questions:

  * 1. What is a blockchain and how does it work?
    Blockchain
      A blockchain is a growing list of records, called blocks, that are linked using cryptography. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data and its resistant to modification of the data.

    How it works
      Basically it's a way of passing information from A to B in a fully automated and safe manner. One party to a transaction initiates the process by creating a block. This block is verified by thousands, perhaps millions of computers distributed around the net. The verified block is added to a chain, which is stored across the net, creating not just a unique record, but a unique record with a unique history. Falsifying a single record would mean falsifying the entire chain in millions of instances. Bitcoin uses this model for monetary transactions, but it can be deployed in many other ways.

  * 2. What is an array and how does it work?
    An array 
      An array is a data structure, which can store a fixed-size collection of elements of the same data type. An array is used to store a collection of data, but it is often more useful to think of an array as a collection of variables of the same type.

    How it works
      All arrays consist of contiguous memory locations. The lowest address corresponds to the first element and the highest address to the last element. Once an array has been initialized the elements can have values assigned to them by using the array's index. The index defines the position of each element in the array. The first element is at 0, the second element at 1 and so on. It's important to note that the index of the first element is 0. It's easy to think that because an array has ten elements that the index is from 1 to 10 instead of from 0 to 9.

  * 3. What is a hash table and how does it work?
    Hash table
        A hash table is a data structure that is used to store keys/value pairs. It uses a hash function to compute an index into an array in which an element will be inserted or searched. By using a good hash function, hashing can work well.Under reasonable assumptions, the average time required to search for an element in a hash table is O(1). 

      How it works
        Hashing is implemented in two steps:
        An element is converted into an integer by using a hash function. This element can be used as an index to store the original element, which falls into the hash table.
        The element is stored in the hash table where it can be quickly retrieved using hashed key.


      Hash function
        A hash function is any function that can be used to map a data set of an arbitrary size to a data set of a fixed size, which falls into the hash table. The values returned by a hash function are called hash values, hash codes, hash sums, or simply hashes.
        To achieve a good hashing mechanism, It is important to have a good hash function with the following basic requirements:
        Easy to compute:
          It should be easy to compute and must not become an algorithm in itself.
        Uniform distribution: 
          It should provide a uniform distribution across the hash table and should not result in clustering.
        Less collisions: 
          Collisions occur when pairs of elements are mapped to the same hash value. in simple terms a collision or clash is a situation that occurs when two distinct pieces of data have the same hash value. To resolve this we use a method called linear probing



  


You will receive points at the PM's discretion based on the following criteria:

  * 20: Would love to have this person on my team!
  * 14: Wouldn't mind working with this person.
  * 10: Knowledge is lacking OR poor communication skills
  *  6: Knowledge is lacking AND poor communication skills
  *  2: You get 2 points for showing up



## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (ideally using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

You can earn 35 points from the main coding portion of the sprint challenge.  Be sure to budget your time wisely.  The Blockchain challenge is fun, but it is only 1/3 of the points availible for the coding portion of this challenge.  

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain) - 12 pts
  * ex1 - 12 pts

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-Theory/tree/master/hash-tables) - 24 pts
  * ex1 - 12 pts
  * ex2 - 12 pts

Both Hash Table problems will be graded as follows:
  * 1: Code attempted
  * 2: Code resembles the correct solution
  * 3: Tests pass
  * 4: Tests pass, using the existing hash table implementation, no flake8 complaints
  * 5: Tests pass, using the existing hash table implementation, no flake8 complaints, linear runtime complexity


### Grading

Students can receive up to 55 points in total for this Sprint Challenge (not including 4 extra credit points). 

  * __Challenge__: 35
  * __Interview__: 20

--------

The score distributions are as follows:

  * __3__: >= 48 points
  * __2__: >= 35 points
  * __1__: < 34 points 