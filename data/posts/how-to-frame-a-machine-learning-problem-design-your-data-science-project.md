title: How to Frame a Machine Learning Problem | Design Your Data Science Project
slug: how-to-frame-a-machine-learning-problem-design-your-data-science-project
pub: 2022-12-09 06:45:58
authors: parthshukla
tags: data science,framing,machine learning,ml project
category: data science,machine learning

Machine learning is the concept that a computer program can learn and adapt to new data without human intervention. It is a sub-field of artificial intelligence that keeps a computer's built-in algorithms current regardless of changes in the worldwide economy. Currently, most companies and agencies are using machine-learning techniques to solve their business problem, these machine-learning techniques are capable of solving almost all kinds of real-world problems occurring in the industry.

Choosing a machine learning method to implement data is not the easiest of processes. It is essential first to understand the precise business problem and its objectives. For instance, understanding what needs to be predicted and understanding potential outcomes is critical. One also needs to know what data should be used to train a model, among other factors. Such considerations help with the framing of a machine-learning problem.
Problem framing is the process that requires analyzing the problem to isolate the individual elements that need to be addressed to solve it. It will help determine the project's technical feasibility and provides a clear set of goals and success criteria. When considering an ML solution, effective problem framing can determine whether or not your product ultimately succeeds.

Table of Content
================


1. Business problem to ML Problem
2. Types of Problem
3. Current Solution
4. Getting the data
5. Matrices to measure
6. Online ML vs Batch ML
7. Checking Assumptions
8. Key Takeaways
9. Conclusion


Framing the Problem
===================



Framing a business problem can be divided into two distinct steps:

1. Determining whether Machine-Learning is the right approach for solving a problem.
2. Framing the problem in Machine-Learning terms.



The first step while solving a business problem is to analyze and determine whether an existing problem can be solved using the machine-learning approach or not, If the current problem, is not a problem that can be solved via machine learning then it need to solved using some other techniques related to other domains, but if the problem is solvable using machine learning techniques then there are set of steps which can help to design pathways and solving the problem.

### Step 1: Business problem to ML Problem



The business problem to ML Problem step consists of a process in which the current business problem is transformed into a machine-learning problem. Now let's understand the problem by taking an example of the famous OTT platform Netflix. Let's suppose that the current business problem is to increase the revenue of the company. Now, several ways can help to increase the revenue of the company like increasing the cost, focusing on marketing to bring in new customers, and decreasing the churn rate of the problem, where the churn rate is the rate of customers leaving the platform monthly or yearly basis. Here the churn rate should be decreased by using some machine learning methods. So the business problem of increasing revenue is converted into an ML problem(decreasing churn rate).
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf1-300x300.png)
[Image Source](https://www.google.com/search?q=solutionin+ml+buiness&tbm=isch&ved=2ahUKEwjWsb2tldr6AhV8itgFHSEMCdQQ2-cCegQIABAA&oq=solutionin+ml+buiness&gs_lcp=CgNpbWcQAzoECCMQJ1DFCFjFCGCXCmgAcAB4AIABpwGIAcICkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=imxGY9bECvyU4t4PoZikoA0&bih=579&biw=1204&rlz=1C1CHBD_enIN933IN933&hl=en-GB#imgrc=Gp5yMzyydlYjSM "Image Source")
### Step 2: Types of Problem



After transforming a business problem into an ML problem, the next task is to analyze the types of ML problems. here we want to decrease the churn rate which will be reducing the number of customers leaving the platform. So here the actual problem is not to predict the churn rate of the company, it is a separate classification task that falls under supervised machine learning, but the main thing which should be considered in the problem is to identify the customers who are going to leave the platform.
Once the customers who are likely to leave the platform are identified the next task is to stop them from leaving the platform. Now there are some ways to stop them from leaving the platform like offering them discounts, Identifying the problem due to which they are leaving the problem, and solving the problem. Here we solved our first problem of identifying whether a customer will leave the platform or not which was a classification task, but here by general understanding we know that every person will not have the same probability of leaving the problem, some will have a very high chance of leaving the platform whereas some customers will have a very low chance. So it is a better idea if we solve the task using a regression problem and predict the customer leaving probability, and then offer a high discount t the customers who have a very high probability of leaving the problem.
So this is how we can think about the ML problem and classify them into tasks and problems based on our domain knowledge.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf2.jpg)
[Image Source](https://www.google.com/search?q=types+of+problem+in+ml+buiness&tbm=isch&ved=2ahUKEwiM47yAldr6AhW6gGMGHUKwAFgQ2-cCegQIABAA&oq=types+of+problem+in+ml+buiness&gs_lcp=CgNpbWcQAzoECCMQJ1DkBVi3EGCXEWgAcAB4AIABowKIAaILkgEFMC43LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=K2xGY8yhMLqBjuMPwuCCwAU&bih=579&biw=1204&rlz=1C1CHBD_enIN933IN933&hl=en-GB#imgrc=S4W6OtYtn7C5IM "Image Source")
### Step 3: Current Solution



After classifying the problem into tasks and sub-problem, the next step is to think and analyse about the current solution available. Let's suppose we have a Machine learning model in our company that has been designed to forecast the churn rate of the company. So here we can take the help of the current existing churn rate prediction model and get a basic idea of how it works and what should be implemented in our next solution. So this is how the currently available solution can help to get a basic idea of the problem and there is no need to start the problem from scratch, which can help reduce the cost and efforts required to solve the problem.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf3-300x165.jpg)
[Image Source](https://www.google.com/search?q=solutionin+ml+buiness&tbm=isch&ved=2ahUKEwjWsb2tldr6AhV8itgFHSEMCdQQ2-cCegQIABAA&oq=solutionin+ml+buiness&gs_lcp=CgNpbWcQAzoECCMQJ1DFCFjFCGCXCmgAcAB4AIABpwGIAcICkgEDMC4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=imxGY9bECvyU4t4PoZikoA0&bih=579&biw=1204&rlz=1C1CHBD_enIN933IN933&hl=en-GB#imgrc=Gp5yMzyydlYjSM "Image Source")
### Step 4: Getting the data



Getting the data for the machine learning problems is the most crucial and time-consuming part but as well an important step also. It is said that good data can help achieve higher accuracy on bad-performing models also. If we can get accurate data related to the machine problem the output model will be best performing and the purpose will be satisfied easily. The features which data contains should be best represented. For example, if the person's watch time is less and searching time on the platform is higher then it is possible that a customer is not able to get the right content on the platform. So the features representing the data and behavior of the customer should be informative and effective. The data can be accessed through any public data available or APIs or web scraping. For our Netflix example, the data will be made available from the database in which the platform stores the data of the customers and their actions.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf4-300x181.png)
[Image Source](https://www.google.com/search?q=databaset+features+in+ml&tbm=isch&ved=2ahUKEwieqoT9ldr6AhX6KbcAHf5xDpsQ2-cCegQIABAA&oq=databaset+features+in+ml&gs_lcp=CgNpbWcQAzoECCMQJzoGCAAQCBAeOgcIABCABBAYUJcKWNMlYNMmaABwAHgAgAHYAogB6RGSAQgwLjEwLjEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=MW1GY95N-tPctQ_-47nYCQ&bih=579&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=vne9SCMlzQTsHM "Image Source")
### Step 5: Matrices to measure



Once the data is available and the model is built, It is essential to know whether the model is performing well or not, Some matrices can be used to get an idea about the performance of the model. So in this step, some metrics should be defined to get an idea about the performance of the model. For example, the measurement of the actual churn rate and predicted churn rate can be compared, predicted customer leaving the platform and actual whether the customer left the platform or not.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf5-300x244.png)
[Image Source](https://www.google.com/search?q=databaset+features+in+ml&tbm=isch&ved=2ahUKEwieqoT9ldr6AhX6KbcAHf5xDpsQ2-cCegQIABAA&oq=databaset+features+in+ml&gs_lcp=CgNpbWcQAzoECCMQJzoGCAAQCBAeOgcIABCABBAYUJcKWNMlYNMmaABwAHgAgAHYAogB6RGSAQgwLjEwLjEuMZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=MW1GY95N-tPctQ_-47nYCQ&bih=579&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=vne9SCMlzQTsHM "Image Source")
### Step 6: Online vs Offline ML



The next step is to think about whether to make the model online or offline. both of the approaches have their advantages and disadvantages. the best fit solution can vary with different problem statements. It should be discussed among the team and then the final action is taken on whether to make the model online and make changes in the live model where the model will train online, whereas in the offline ML the model will be trained on a local machine and if any changes required to the model then it will be taken out of the server, retrained and then again make it online to the server.
For example, The best approach for the Netflix model will be an Online approach as how much time the customers will spend time on the platform, the churn rate, and the likeliness of the customers are very volatile concepts. For this type of problem where the new incoming data is generated and fed to the model, the online ML would be a great approach where the model will continuously be trained using incoming new data and trained on the live data available.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf6-300x169.png)
[Image Source](https://www.google.com/search?q=online+vs+offline+ml+photo+&tbm=isch&ved=2ahUKEwjv492Zl9r6AhXtKbcAHffGBJsQ2-cCegQIABAA&oq=online+vs+offline+ml+photo+&gs_lcp=CgNpbWcQAzoECCMQJ1CjCVijF2CyI2gAcAB4AIAB_wGIAfoLkgEFMC42LjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=eW5GY6_DJu3T3LUP942T2Ak&bih=579&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=bK9Ad0yZ07uy-M "Image Source")
### Step 7: Check Assumptions



the last step while framing the machine learning problem is to check for assumptions. here in this step, we try to check whether the assumptions which are taken to build the model are available or not. If it is available then it is used and if not then it needs some more study,
For example, some features and data can not be used for all customers belonging to different countries. Also, the featured and data of the customers which are taken into consideration are available on the database of the company or not.
These are some primary steps that should be considered while framing a machine-learning problem, it is not like that it should be always considered and always true, but having an idea of these steps can help frame a better pathway for solving a machine-learning problem.
![](https://mail.pythonkitchen.com/wp-content/uploads/2022/12/mlf7-300x186.png)
[Image Source](https://www.google.com/search?q=ml+poblem+statements&tbm=isch&ved=2ahUKEwjG_s6ImNr6AhVmkNgFHTpTDRIQ2-cCegQIABAA&oq=ml+poblem+statements&gs_lcp=CgNpbWcQAzoECCMQJzoLCAAQgAQQsQMQgwE6CAgAELEDEIMBOgUIABCABDoHCAAQsQMQQzoHCAAQgAQQAzoICAAQgAQQsQM6BAgAEENQAFiZJmD6JmgBcAB4AIAB4gGIAdgckgEGMC4xNi40mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Ym9GY8bFCuag4t4Puqa1kAE&bih=579&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=jTOzaebGddCsTM "Image Source")
Key Takeaways
=============


1. Framing a machine learning problem can ease the process of solving the same problem.
2. Primary steps of framing a machine learning problem include deep study and analyses of the problem.
3. Secondary stage of framing and solving a machine learning problem is to try different combinations and find the best fit solution for the same.
4. The last step while framing and working on the machine-learning problem is to check the whether designed solutions can be implemented or not and work on them.


Conclusion
==========



In this article, the primary steps which are essential and should be taken into consideration while solving a machine learning problem are discussed. A primary understanding of the way of looking at the problem statement and techniques to find the best fit solution for the problem is required for solving any kind of business problem with the help of a machine learning approach. With the example of actual real-world problem statements, all of the steps are discussed briefly which will help one not only design the solution pathway to the problem but also help one from understanding the problem to building an actual solution.
