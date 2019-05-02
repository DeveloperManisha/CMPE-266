CREATE EXTERNAL TABLE IF NOT EXISTS default.ReviewSentimentAnalysis (
  `ImageLocation` string,
  `Timestamp` string,   
  `Sentiment` string,
  `Positive` string,
  `Negative` string,
  `Neutral` string,
  `Mixed` string
  )
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://review-sentiment-s3-ldhxvq8hqqfi/sentiment/'