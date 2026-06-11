WITH source AS (
    SELECT * FROM {{ source('api_rick_morty', 'characters') }}
),

renomeando_colunas AS (
    SELECT
        id AS id_personagem,
        name AS nome_personagem,
        status AS status_vida,
        species AS especie,
        gender AS genero,
        image AS imagem,
        "location.name" AS localizacao
    FROM source
)

SELECT * FROM renomeando_colunas