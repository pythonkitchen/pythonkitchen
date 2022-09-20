title: Armstrong Numbers
slug: armstrong-numbers
pub: Thu, 27 Dec 2018 19:27:39 +0000
authors: Abdur-RahmaanJ

we start the problem series on PMC (Python Members Club) with Armstrong Numbers. 




definition
----------




**an armstrong number is a number such that the sum of the digits in the number raised to the number of digits equals the number itself**




breaking down




*sum of the digits in the number*




let us take number abc, sum is 




a + b + c




*raised to the number of digits*




num of digits in abc is 3




a^3 + b^3 + c^3




*equals the number itself*




a^3 + b^3 + c^3 == abc




examples
--------




1 - 123, number of digits: 3, hence risen to power 3




1^3 + 2^3 + 3^3 -> 36, not equals 123




2 - 153 , number of digits: 3, hence risen to power 3




1^3 + 5^3 + 3^3 ->1 + 125 + 27 -> 153, sum same as number




3 - 8208, number of digits, hence risen to power 4




8^4 + 2^4 + 0^4 + 8^4 ->4096 + 16 + 0 + 4096-> 8208, sum same as number




**our code**
------------





```python

for i in range(1000000):
     num = str(i)
     sumcube = 0
     for n in num:
         sumcube += (int(n) ** len(num))
     if i == sumcube:
         print(i, 'is an armstrong number')

```



the logic
---------




for i in ... spits out a number each time for us to deal with




 num = str(i) transform the integer into string ...




... which allows us a neat python trick: iterating over a string. that way we instantly get the 3 1 9 of 319. the conventional approach would have been to divide by 100 10 and 1 to get 3 1 9




nothing spooky, out of reach eh ...




anything? drop a word below ^^



