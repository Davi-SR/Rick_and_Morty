SELECT
    id_localizacao,
    nome_localizacao,
    tipo_localizacao,
    dimensao
FROM {{ ref('stg_localizacoes') }}
