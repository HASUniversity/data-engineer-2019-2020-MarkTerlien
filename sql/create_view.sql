-- View: public.meteo_station_vw

-- DROP VIEW public.meteo_station_vw;

CREATE OR REPLACE VIEW public.meteo_station_vw AS
 SELECT meteo_stations.id,
    meteo_stations.name,
    meteo_stations.altitude,
    meteo_stations.geom
   FROM meteo_stations
  WHERE meteo_stations.name::text = 'Schiphol'::text;

ALTER TABLE public.meteo_station_vw
    OWNER TO postgres;
