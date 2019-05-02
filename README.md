# CMPE-266

University Name: http://www.sjsu.edu/   
Course: Big Data Engineering and Analytics   
Professor: [Sanjay Garje](https://www.linkedin.com/in/sanjaygarje/)  
Students:  
[Manisha Shivshette](https://www.linkedin.com/in/manisha-shivshette-94632a136/)  
[Rakhee Singh](https://www.linkedin.com/in/rakhee-singh-51186954/)  
[Radhika Srinivasan](https://www.linkedin.com/in/radhikas08/)   
[Arshiya Pathan](https://www.linkedin.com/in/arshiya-pathan/)  
Project Introduction:  
In this project, we are analyzing AirBnb dataset which describes listing activities of homestays in New York. The idea is to gain insights into the large dataset by finding the price trends over a period, finding busiest times of the year analyzing reviews and neighborhood listings. This will help hosts to make the right business decisions. It will help them understand how to maximize profit and increase the occupancy rate.   
Features list: <br>
Big Data Storage Capability<br>
Easy and fast access to data <br>
Serverless architecture <br>
Fast performance<br>
Data security<br>
Interactive visualizations and dashboard <br>
Identify KPIs (Key Performance Indicator) and hidden insights<br>


<br>
Pre-requisite Setup

*First the dataset is stored in S3 bucket, inside a folder called ‘graphs’ named as listings.csv<br>
*The bucket is made public in order to be accessed from Quicksight.<br>
*Next, a manifest file is added in Quicksight to indicate the bucket which it has to refer to for accessing the dataset for analysis. This manifest file is a json format file as below:<br>

{
    "fileLocations": [
        {
            "URIs": [

                "https://cmpe266airbnb.s3.amazonaws.com/graphs/listings.csv"

            ]
        }
    ]}

This indicates the URI of the dataset that Quicksight needs to access.<br>
*Once done, a new analysis is created in Quicksight by choosing corresponding columns and formatting the visuals to obtain the required charts.<br>






References:
https://aws.amazon.com/blogs/machine-learning/detect-sentiment-from-customer-reviews-using-amazon-comprehend/
