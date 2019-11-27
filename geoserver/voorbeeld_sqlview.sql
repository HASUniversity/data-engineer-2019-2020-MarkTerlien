select id, name, altitude, st_transform(geom,28992) from meteo_stations
where st_intersects(st_transform(geom,28992),st_buffer(st_setsrid(ST_MakePoint(140570,516299),28992), 50000))
union 
select -1, '',-1, st_buffer(st_setsrid(ST_MakePoint(140570,516299),28992), 50000)