// Creating file format for csv files
CREATE OR REPLACE file format csv_format
    type = csv 
    field_delimiter = ','
    skip_header = 1
    empty_field_as_null = TRUE;

// Creating  stage to hold data
CREATE OR REPLACE STAGE aws_s3_csv
    URL = 's3://cleaned-zillow-data-csv/lagos/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = csv_format;

// Listig fils under s3 bucket
list @aws_s3_csv;


//Setting up snowpipe
CREATE OR REPLACE pipe raw_csv_pipe
AUTO_INGEST = TRUE 
AS
copy into REAL_ESTATE_DB.RAW.HOUSE_LISITING_RAW
from @REAL_ESTATE_DB.RAW.AWS_S3_CSV
pattern = '.*response.*';



select * from REAL_ESTATE_DB.RAW.HOUSE_LISITING_RAW;
// Describing pipe to get ARN
DESC pipe raw_csv_pipe;

// Confirming pipe function with query 
select * from REAL_ESTATE_DB.RAW.HOUSE_LISITING_RAW;

