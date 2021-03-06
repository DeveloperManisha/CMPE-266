# CMPE-266

University Name: http://www.sjsu.edu/   
Course: Big Data Engineering and Analytics   
Professor: [Sanjay Garje](https://www.linkedin.com/in/sanjaygarje/)  
Students:  
[Manisha Shivshette](https://www.linkedin.com/in/manisha-shivshette-94632a136/)  
[Rakhee Singh](https://www.linkedin.com/in/rakhee-singh-51186954/)  
[Radhika Srinivasan](https://www.linkedin.com/in/radhikas08/)   
[Arshiya Pathan](https://www.linkedin.com/in/arshiya-pathan/)  
<br>
### Project Introduction:  
In this project, we are analyzing AirBnb dataset which describes listing activities of homestays in New York. The idea is to gain insights into the large dataset by finding the price trends in neighbourhood, finding prices according to property type, density of different types of properties in a region, number of reviews for listings. This will help hosts to make the right business decisions. It will help them understand how to maximize profit and increase the business in different neighbourhood areas. Along with it, we also created end to end flow to tackle the negative reviews posted for listings. AirBnb host is informed by email in case there is any negative review posted for his listing. With help of this immediate information, AirBnb host can acknowledge the issue and take necessary steps to prevent further damage.

### Technologies used
AWS Technologies: S3, Athena, Lambda, Comprehend, Simple Email Service, QuickSight

### Features list:
Review Sentiment analysis 
Big Data Storage Capability
Easy and fast access to data
Serverless architecture 
Fast performance (on queries)
Data security
Interactive visualizations and dashboard
Identify hidden insights


### Pre-requisite Setup

* First the dataset is stored in S3 bucket, inside a folder called ‘graphs’ named as listings.csv<br>
* The bucket is made public in order to be accessed from Quicksight.<br>
* Next, a manifest file is added in Quicksight to indicate the bucket which it has to refer to for accessing the dataset for analysis. This manifest file is a json format file as below:<br>

{
    "fileLocations": [
        {
            "URIs": [

                "https://cmpe266airbnb.s3.amazonaws.com/graphs/listings.csv"

            ]
        }
    ]}

This indicates the URI of the dataset that Quicksight needs to access.<br>
* Once done, a new analysis is created in Quicksight by choosing corresponding columns and formatting the visuals to obtain the required charts.

### Config settings for ML module
* Create S3 bucket sentiment-review-* to upload new review<br>
* Assign IAM role with S3 and Amazon Comprhend to lambda function to run sentiment analysis on review and write output to S3
* Use Athena to create table to store sentiment analysis result from S3
* Assign IAM role with Athena,SES and S3 access to lambda function that sends email in case of negative review.


## System Architecture
![image](https://user-images.githubusercontent.com/32425672/57059439-3ef3a980-6c6a-11e9-81f3-0dd916ddf52c.png)

## Demo Screenshots
### Data Analysis and Visualization
Density of property listings based on neighborhood
![image](https://user-images.githubusercontent.com/32425672/57059550-bcb7b500-6c6a-11e9-979f-0d8aadcf1cd1.png)

Average property prices from Highest to lowest
![image](https://user-images.githubusercontent.com/32425672/57060044-b7f40080-6c6c-11e9-9cb1-f087f73a6775.png)

Average price in a given neighborhood for all property types:
![image](https://user-images.githubusercontent.com/32425672/57060074-d659fc00-6c6c-11e9-97e1-ea24a0bf4c56.png)

Prediction of whether prices affect popularity:
![image](https://user-images.githubusercontent.com/32425672/57060098-01445000-6c6d-11e9-8cdb-bff27d9c67fa.png)
Comparison of popularity of properties for major neighbourhood groups
![image](https://user-images.githubusercontent.com/32425672/57060143-3355b200-6c6d-11e9-8cdc-a5f442b5343f.png)


References:
https://aws.amazon.com/blogs/machine-learning/detect-sentiment-from-customer-reviews-using-amazon-comprehend/
