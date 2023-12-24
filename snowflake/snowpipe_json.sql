// Creating file format for csv files
CREATE OR REPLACE file format json_format
    type = json; 
   

// Creating  stage to hold data
CREATE OR REPLACE STAGE aws_s3_json
    URL = 's3://copy-of-zillow-raw-data/lagos/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = json_format;


// creating stage table to stor
CREATE OR REPLACE TABLE RAW_JSON_TABLE(raw_file variant);



-- Create a pipe to copy raw data into stage table
CREATE OR REPLACE PIPE raw_json_pipe
    AUTO_INGEST = TRUE
AS
COPY INTO REAL_ESTATE_DB.RAW.RAW_JSON_TABLE
FROM @REAL_ESTATE_DB.RAW.AWS_S3_JSON
PATTERN = '.*response.*'
FILE_FORMAT = (FORMAT_NAME = REAL_ESTATE_DB.RAW.JSON_FORMAT);


--Creating snowflake task to load data from stage table to raw table
CREATE or REPLACE TASK load_json_data
    WAREHOUSE = COMPUTE_WH
    SCHEDULE =  'USING CRON * * * * * Africa/Lagos'   
AS
CREATE OR REPLACE TABLE house_listing_json_raw(
    bedrooms INT,
    bathrooms INT,
    city STRING,
    country STRING,
    currency STRING,
    days_on_zillow INT,
    group_type STRING,
    home_status STRING,
    home_status_for_hdp STRING,
    home_type STRING,
    img_src STRING,
    is_featured BOOLEAN,
    is_non_owner_occupied BOOLEAN,
    is_preforeclosure_auction BOOLEAN,
    is_premier_builder BOOLEAN ,
    is_showcase_listing BOOLEAN,
    is_unmappable BOOLEAN,
    is_zillow_owned BOOLEAN,
    latitude FLOAT,
    is_new_home BOOLEAN,
    living_area INT,
    longitude FLOAT,
    new_construction_type STRING,
    price INT ,
    price_for_hdp INT ,
    price_suffix STRING,
    provider_listing_id STRING,
    rent_zestimate INT,
    should_highlight BOOLEAN,
    state STRING ,
    street_address STRING,
    unit STRING,
    zestimate INT,
    zipcode STRING ,
    zpid INT 

)
AS 
SELECT
    value:bedrooms::INT,
    value:bathrooms::INT,
    value:city::STRING,
    value:country::STRING,
    value:currency::STRING,
    value:days_on_zillow::INT,
    value:group_type::STRING,
    value:home_status::STRING,
    value:home_status_for_hdp::STRING,
    value:home_type::STRING,
    value:img_src::STRING,
    value:is_featured::BOOLEAN,
    value:is_non_owner_occupied::BOOLEAN,
    value:is_preforeclosure_auction::BOOLEAN,
    value:is_premier_builder::BOOLEAN,
    value:is_showcase_listing::BOOLEAN,
    value:is_unmappable::BOOLEAN,
    value:is_zillow_owned::BOOLEAN,
    value:latitude::FLOAT,
    value:is_new_home::BOOLEAN,
    value:living_area::INT,
    value:longitude::FLOAT,
    value:new_construction_type::STRING,
    value:price::INT,
    value:price_for_hdp::INT,
    value:price_suffix::STRING,
    value:provider_listing_id::STRING,
    value:rent_zestimate::INT,
    value:should_highlight::BOOLEAN,
    value:state::STRING,
    value:street_address::STRING,
    value:unit::STRING,
    value:zestimate::INT,
    value:zipcode::STRING,
    value:zpid::INT
FROM
    RAW_JSON_TABLE,
    LATERAL FLATTEN(INPUT => PARSE_JSON(raw_file):results) AS result;


-- seeing pipe details 
DESC PIPE raw_json_pipe;
SHOW PIPES LIKE 'raw_json_pipe';
ALTER PIPE raw_json_pipe RESUME;


-- validating sql codes 
select count(*) from HOUSE_LISTING_JSON_RAW;
select * from @AWS_S3_JSON;
select * from RAW_JSON_TABLE;
--truncate table RAW_JSON_TABLE;
    
-- checking task status 
SHOW TASKS LIKE 'load_json_data';
ALTER TASK load_json_data RESUME;
ALTER TASK load_json_data SUSPEND;

