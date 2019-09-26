# Haal alle meteostations op
select * from meteo_stations
select id, name, altitude, st_astext(geom) from meteo_stations

# Tel het aantal meteostations
select count(*) from meteo_stations

# Wat is de hoogte van meteostation Schiphol?
select altitude from meteo_stations where name = 'Schiphol'
select name, altitude from meteo_stations where upper(name) like upper('SChip%') 

# Welke meteostations liggen onder NAP? 
select * from meteo_stations where altitude < 0 order by altitude desc

# Wat is de maximale hoogte van alle meteostations?
select * from meteo_stations order by altitude desc
select max(altitude) from meteo_stations 

# Welk meteo station ligt het hoogst?
select name, altitude from meteo_stations where altitude = (select max(altitude) from meteo_stations) 

# Wat is de gemiddelde hoogte van alle meteostations?
select avg(altitude) from meteo_stations

# Welke meteostations liggen in de provincie Zuid-Holland?
select meteo_stations.name, provincie.provnaam
from meteo_stations, provincie 
where upper(provincie.provnaam) like upper('zuid%holland')
and   st_within(meteo_stations.geom, provincie.geom) 

# Tel het aantal meteostations per provincie
select provincie.provnaam, count(1), avg(meteo_stations.altitude)
from meteo_stations, provincie 
where st_within(meteo_stations.geom, provincie.geom) 
group by provnaam
order by 2 desc