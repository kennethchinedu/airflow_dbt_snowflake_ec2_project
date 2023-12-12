WITH raw_housing AS(
    SELECT * from {{ source('real_estate', 'house_listing') }}
)

SELECT * 
FROM 
    raw_housing