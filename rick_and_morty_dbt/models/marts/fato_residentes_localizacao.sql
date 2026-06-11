WITH residentes AS (
    SELECT
        id_localizacao,
        residente.id_personagem
    FROM {{ ref('stg_localizacoes') }}
    LEFT JOIN LATERAL UNNEST(array_id_residentes) AS residente(id_personagem) ON true
    WHERE residente.id_personagem IS NOT NULL
)

SELECT * FROM residentes
