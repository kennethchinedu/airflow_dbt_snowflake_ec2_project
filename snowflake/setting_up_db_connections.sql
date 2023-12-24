Create or replace database real_estate_db;

use real_estate_db;

Create schema raw;
Use raw;

CREATE OR REPLACE TABLE house_lisiting_raw(
        bathrooms int,
        bedrooms int,
        city string,
        homeStatus string,
        homeType string,
        livingArea int,
        price int,
        rentZestimate int,
        zipcode int        
);


Create schema Analytics;

// creating storage integration to connect aws to snowflake
create or replace storage integration s3_int
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = S3
    ENABLED = TRUE 
    STORAGE_AWS_ROLE_ARN = '***'
    STORAGE_ALLOWED_LOCATIONS = ('s3://cleaned-zillow-data-csv/lagos/', 's3://copy-of-zillow-raw-data/lagos')
    COMMENT = 'creating integration connection with s3';


// Getting external ID and updating in IAM
DESC integration s3_int;





