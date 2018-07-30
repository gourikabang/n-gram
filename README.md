# n-gram
Obtained the top 30% n-grams based on frequency of their occurrences.

## Objective
1. Obtain the frequency of occurences of all the unique 3-grams, 5-grams and 7-grams system call sequences in the Training data for both Attack data (across all categories of attack) and Normal data.
2. Obtain the top 30% n-gram terms with the highest frequency of all the unique n-gram terms in the training data to create a data set.(This will be final training data used to train various classifiers)
3. Applying similar procedure to obtain final Test data set.

## Overview
Host-based intrusion detection systems (HIDSs), especially anomaly-based, have received much attention over the past few decades. Over time, however, the existing data sets used for evaluation of a HIDS have lost most of their relevance due to the substantial development of computer systems. To fill this gap, ADFA Linux data set (ADFA-LD) is recently released. Six types of attacks occur in ADFA-LD including two brute force password guessing attempts on the open ports enabled by FTP and SSH respectively, an unauthorised attempt to create a new user with root privileges through encoding a malicious payload into a normal executable, the uploads of Java and Linux executable Meterpreter payloads for the remote compromise of a target host, and the compromise and privilege escalation using C100 webshell. These types are termed as Hydra-FTP, Hydra-SSH, Adduser, Java-Meterpreter, Meterpreter and Webshell respectively.

Once we obtain the Training and Test data sets for unique n-gram we implement a simple k nearest neighbour (kNN) to develop new host-based anomaly detection systems (HADSs).

## Methodology
#### To implement the above goals , the following methodology was followed: 
1. For each Attack category we split the data set into two parts(Training and Test).
2. All the training files for a particular class of attack are concatenated.
3. Frequency of each unique n-gram term is calculated using the concept of hashing in linear time.
4. Using the above obtained data the top 30% n-gram terms is obtained using "Blum's Algorithm."
5. These 30% terms(comprises the features of the final training data set) are concatenated.
6. With the help of dictionary interface which held the previous data the frequencies for each class of attack for all the features is obtained.
7. Similar methodology is followed for Test data set.
