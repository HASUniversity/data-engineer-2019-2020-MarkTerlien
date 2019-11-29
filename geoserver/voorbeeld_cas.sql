select sum(id), st_union(geom)
from
(
select id 
, st_intersection(geom, st_transform(st_buffer(st_setsrid(ST_MakePoint(140570,516299),28992), 50000),4326))  geom
from provincie where st_intersects(st_transform(geom,28992),st_buffer(st_setsrid(ST_MakePoint(140570,516299),28992), 50000))
)	as tab	