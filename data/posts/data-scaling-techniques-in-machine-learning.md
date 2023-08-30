title: Data Scaling Techniques in Machine Learning
slug: data-scaling-techniques-in-machine-learning
pub: 2023-01-26 03:34:30
authors: parthshukla
tags: data science,machine learning,scaling
category: data science,machine learning

Data and its quality affect machine learning models and their accuracy, and the quality of the data can not be well in some types of problems which can be solved by machine learning. Here the scale of the data is also represented as the quality of the data, which needs to be expected while training the machine learning model. If the **scale** of the data is not normal then some techniques are applied to make it of the same scale.

Scaling is also a technique used to transform the data scale into the same scale to make it clearly understandable by machine learning algorithms and make it an easier task. This article will discuss data scaling techniques with their intuition and mathematical formulations. This will help one understand the data's scale property and make it of the same scale if needed.

Table of Content
================


* What is Data Scale?
* Standardization
* Normalization
* Min Max Scaling
* Mean Normalization
* Max Absolute Scaling
* Robust Scaling
* Key Takeaways
* Conclusion


What is Data Scale?
===================



The scale of the data is the **range of values** that every feature or column of the data has. The scale can be numerical numbers that represent data features and their values. Now here, in every case, it is not possible to have the same scale of the data ranging between the same range, and in such cases, it can cause problems like poor performance from the model.

For example, data having two columns, age and salary, where the age ranges between 0 to 100 and salary ranges between 10000 to 100,000 is having different scales, and it needs to be preprocessed before passing it to the machine learning algorithm.

Mainly two techniques are applied to achieve the same scale of the data:
1. Standardization
2. Normalization

Standardization
===============



Standardization is a technique where every sta point is taken, and a mathematical formula is applied to transform the particular data point.

This technique is also known as the mean centralization technique, as after applying this technique, the mean of the data points is **0**, and the standard deviation of the data is **1**.

![](/assets/ds2-300x125.png)
[Image Source](https://www.google.com/search?q=standardization+formula&rlz=1C1CHBD_enIN933IN933&sxsrf=AJOqlzURVqJHGB12q7-XL3RhUz382aNCXg:1673833807943&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-hKTs_Mr8AhWyVHwKHZ15B8MQ_AUoAXoECAEQAw&biw=1220&bih=547&dpr=1.12#imgrc=VeeioC_xQ7SaAM "Image Source")

Here, 

> Z = New Datapoint

> X = data point which is to be transformed

> Meu = Mena of the data

> Sigma = Standard deviation of the data

As we can see in the above image, every data point referred to as “x” is taken. The mean of the data is substituted from the same and divided by the standard deviation of the data, the quantity obtained from the same is a new observation, and this will now be taken as the new data point.

Normalization
=============



The standardization technique is mostly preferred for scaling the data and performs well. Still, in some cases, normalization techniques are also used for **transforming the scale of the data**.

In this method, various techniques are used for scaling the data:
1. Min-Max Scaling
2. Mean Normalization
3. Max Absolute Scaling
4. Robust Scaling

Min-Max Scaling
---------------



Min-max scaling is a normalization technique when we know the uppermost and lowermost limit of the data points’ values. This transformation technique converts the data points into new values ranging from **0 to 1**.

![](/assets/ds3-300x76.png)
[Image Source](https://www.google.com/search?q=min+max+scaling+formula&rlz=1C1CHBD_enIN933IN933&sxsrf=AJOqlzXP-mfS1O1DYPYT7biyUjqGBjXKMw:1673834302230&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj15_zX_sr8AhVD7TgGHYVHA_YQ_AUoAXoECAEQAw&biw=1220&bih=547&dpr=1.12#imgrc=LfU210iNThIcvM&imgdii=mbkvPAkidevLTM "Image Source")

Here, 

> X’ = New Datapoint

> X = Datapoint, which is to be transformed

> min(x) = Minimum value from the data

> max(x) = Maximum value from the data

As we can see in the above image, the maximum and minimum value of the data is taken, and a new data point is generated, which will have a value between **0 and 1**.

Mean Normalization
------------------



Mean normalization is also a normalization technique that uses the mean of the data while transforming the data point into its new value. The mean normalization is the same as the min-max scaling techniques, which differs when it uses the mean of the data distribution instead of the data's minimum value in the formula's numerator.

![](/assets/ds4-300x67.png)
[Image Source](https://www.google.com/search?q=mean+normalization%27+scaling+formula&tbm=isch&ved=2ahUKEwio5-Le_sr8AhX0itgFHTg_CMMQ2-cCegQIABAA&oq=mean+normalization%27+scaling+formula&gs_lcp=CgNpbWcQAzoECCMQJzoHCAAQgAQQGFCqC1jrH2CUJ2gAcAB4AIAB5AGIAbYbkgEGMC4xOS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=TK_EY6iRHfSV4t4PuP6gmAw&bih=547&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=qclWWPviPA85fM "Image Source")

Here,

> X’ = New Datapoint

> X = Datapoint, which is to be transformed

> min(x) = Minimum value from the data

> max(x) = Maximum value from the data

> mean(X) = Mean of datapoints values

As we can see in the above image, the mean of the data is used instead of the minimum value of the data; hence, the mean normalization transforms the data points values between **-1 and 1**.

Max Absolute Scaling
--------------------



Max absolute scaling is a normalization technique that uses the absolute value of the maximum value of the dataset. This technique is not much used as the other methods are mostly enough to transform the data into its normal distribution.

![](/assets/ds5.png)
[Image Source](https://www.google.com/search?q=max+abs+normalization%27+scaling+formula&tbm=isch&ved=2ahUKEwiC5pLX_8r8AhU_k9gFHShDBYQQ2-cCegQIABAA&oq=max+abs+normalization%27+scaling+formula&gs_lcp=CgNpbWcQAzoECCMQJ1CID1jmFmDNF2gAcAB4AIAB1wGIAagKkgEFMC42LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=SLDEY4KiOL-m4t4PqIaVoAg&bih=547&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=regMugh1tyYfAM&imgdii=Sv4g-rOsqBNwuM "Image Source")

Here, 

> Xscaled = New datapoint

> X = Datapoints which is to be transformed

> max(|x|) = Absolute value of datapoint having a maximum value from the data

Robust Scaling
--------------



As the name suggests, robust scaling is a type of data scaling technique that is very robust to the outliers and is used in case of the data having outliers. This technique transforms the data into its normal distribution without having the effect of outliers and their values.

This technique uses the Interquartile range and median of the data, which makes it **robust to the outliers**.

![](/assets/ds6-300x149.png)
[Image Source](https://www.google.com/search?q=robust+normalization%27+scaling+formula&tbm=isch&ved=2ahUKEwiMoc2tgcv8AhWChNgFHTt8BM8Q2-cCegQIABAA&oq=robust+normalization%27+scaling+formula&gs_lcp=CgNpbWcQAzoECCMQJ1DiBVioD2C-EmgAcAB4AIAB1AGIAdwFkgEFMC4zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=CrLEY4z0KIKJ4t4Pu_iR-Aw&bih=547&biw=1220&rlz=1C1CHBD_enIN933IN933#imgrc=6w8NlMSYUqFxoM&imgdii=7p6nM4AWejSyjM "Image Source")

As we can see in the above image, the technique uses the median in its numerator and the IQR in its denominator, making it robust to the outliers as the median and IQR do not have any relationship with outliers and their value in any way.

Key Takeaways
=============


* The data points and their value should be appropriately scaled before feeding them to the machine learning algorithms to avoid poor performance.
* The standardization techniques are the most frequently used technique that transforms the data to have **zero mean and one standard deviation** after transformation.
* The min-max scaling transforms the data between **0 to 1** by using maximum and minimum values of the data.
* The mean normalization technique transforms the data between **-1 to 1** by using the mean of the data.
* The maximum absolute technique is not much used, but sometimes it may help with data that does not fit with other cling techniques.
* The robust scaling would be used in case of outliers present where it transformers the data without any **effect of outliers** and their values.


Conclusion
==========



In this article, we discussed data scaling and its techniques to transform the data into the same scale to make the model training more straightforward and efficient. This will help one to understand the scale f the data and apply an appropriate technique to bring the scale of the data into the correct format.
