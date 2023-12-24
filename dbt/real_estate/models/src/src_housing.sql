WITH raw_housing_listing AS(
    SELECT * from {{ source('real_estate_db', 'HOUSE_LISTING_JSON_RAW') }}
)

SELECT * 
FROM 
    raw_housing_listing