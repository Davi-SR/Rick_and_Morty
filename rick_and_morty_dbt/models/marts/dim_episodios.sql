SELECT
    id_episodio,
    nome_episodio,
    data_lancamento,
    codigo_episodio
FROM {{ ref('stg_episodios') }}
