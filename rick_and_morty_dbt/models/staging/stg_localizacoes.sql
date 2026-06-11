WITH source AS (
    SELECT * FROM {{ source('api_rick_morty', 'locations') }}
),

renomeando_colunas AS (
    SELECT
        id AS id_localizacao,
        name AS nome_localizacao,
        type AS tipo_localizacao,
        dimension AS dimensao,
        CAST(
            REPLACE(REPLACE(REPLACE(REPLACE(residents, 'https://rickandmortyapi.com/api/character/', ''), '''', ''), '[', '{'), ']', '}') 
            AS INTEGER[]
        ) AS array_id_residentes
    FROM source
)

SELECT * FROM renomeando_colunas
