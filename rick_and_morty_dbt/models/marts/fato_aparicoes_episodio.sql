WITH aparicoes AS (
    SELECT
        id_episodio,
        personagem.id_personagem
    FROM {{ ref('stg_episodios') }}
    LEFT JOIN LATERAL UNNEST(array_id_personagens) AS personagem(id_personagem) ON true
    WHERE personagem.id_personagem IS NOT NULL
)

SELECT * FROM aparicoes
