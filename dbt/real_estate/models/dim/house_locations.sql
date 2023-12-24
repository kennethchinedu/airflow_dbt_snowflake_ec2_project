WITH src_housing AS (
    SELECT * from {{ ref("src_housing")}}
    
)

SELECT 
    home_type,
    city,
    state,
    latitude,
    longitude,
    street_address,
    zipcode

FROM 
    src_housing