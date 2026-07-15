with duplicados as (
    select a.cpf
    from assistido_pessoa a
    where a.desativado_em is null and length(a.cpf) > 1
    group by a.cpf
    having count(*) > 1
    order by count(*) desc
)
select t2.id as id_assistido
from duplicados t1
left join assistido_pessoa t2 on t1.cpf = t2.cpf
order by t2.id desc;