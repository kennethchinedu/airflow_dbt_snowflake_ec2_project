{{
    config(
        materialized='view'
    )
}}
WITH src_housing AS (
    SELECT * from {{ ref("src_housing")}}
    
)

SELECT 
    home_type,
    bedrooms,
    bathrooms,
    city,
    group_type,
    is_featured,
    state
FROM 
    src_housing
WHERE is_featured IS NOT NULL