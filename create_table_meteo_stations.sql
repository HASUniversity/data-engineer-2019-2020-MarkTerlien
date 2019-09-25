-- Table: public.meteo_stations

-- DROP TABLE public.meteo_stations;

CREATE TABLE public.meteo_stations
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default",
    altitude double precision,
    geom geometry,
    CONSTRAINT meteo_stations_pk PRIMARY KEY (id),
    CONSTRAINT meteo_stations_constraint_unique UNIQUE (name)

)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.meteo_stations
    OWNER to postgres;

-- Index: meteo_stations_index_geom

-- DROP INDEX public.meteo_stations_index_geom;

CREATE INDEX meteo_stations_index_geom
    ON public.meteo_stations USING gist
    (geom)
    TABLESPACE pg_default;

-- Index: meteo_stations_index_pk

-- DROP INDEX public.meteo_stations_index_pk;

CREATE INDEX meteo_stations_index_pk
    ON public.meteo_stations USING btree
    (id)
    TABLESPACE pg_default;