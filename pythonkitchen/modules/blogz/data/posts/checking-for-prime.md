title: Checking For Prime
slug: checking-for-prime
pub: Sat, 29 Dec 2018 15:00:00 +0000


prime numbers are surprisingly easy to check for. to check if a number is prime, we divide it by it's factors. 1 is not prime





```python
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                return False
        return True

```



we take all numbers from 2 to the num and we start dividing by 2, 3, 4, 5, ...




but really we need only to go to half the numbers, upto n//2 + 1





```python
def is_prime(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if num%i == 0:
                return False
        return True

```



then we can use it like that:





```python
for i in range(100):
    prime = is_prime(i)
    if prime: print(i)

```



for primes upto 100. pretty easy.




checking for the first time there is a difference of 100
--------------------------------------------------------





```python
primes = []
for i in range(10000):
    prime = is_prime(i)
    if prime: 
        primes.append(i)

def first_100_diff(primes):
    for primeA in primes:
        for primeB in primes:
            if abs(primeA - primeB) == 100:
                print(primeA, primeB)
                return

first_100_diff(primes)

```



the above checks the first time there is a difference of 100. modify the loop to check for the next 10 occurances.



