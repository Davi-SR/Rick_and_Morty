WITH source AS (
    SELECT * FROM {{ source('api_rick_morty', 'episodes') }}
),

renomeando_colunas AS (
    SELECT
        id AS id_episodio,
        name AS nome_episodio,
        air_date AS data_lancamento,
        episode AS codigo_episodio,
        CAST(
            REPLACE(REPLACE(REPLACE(REPLACE(characters, 'https://rickandmortyapi.com/api/character/', ''), '''', ''), '[', '{'), ']', '}') 
            AS INTEGER[]
        ) AS array_id_personagens
    FROM source
)

SELECT * FROM renomeando_colunas
