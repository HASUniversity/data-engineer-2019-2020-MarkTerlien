-- SEQUENCE: public.observation_id_seq

-- DROP SEQUENCE public.observation_id_seq;

CREATE SEQUENCE public.observation_id_seq;

ALTER SEQUENCE public.observation_id_seq
    OWNER TO postgres;

-- Table: public.observation

-- DROP TABLE public.observation;

CREATE TABLE public.observation
(
    datum date NOT NULL,
    mean_temperature real,
    max_temperature real,
    sunshine_duration real,
    global_radiation real,
    precipitation real,
    mean_sea_level_pressure real,
    mean_humidity real,
    max_humidity real,
    potential_evapotranspiration real,
    meteostationid integer NOT NULL,
    id bigint NOT NULL DEFAULT nextval('observation_id_seq'::regclass),
    CONSTRAINT observation_pkey PRIMARY KEY (datum, meteostationid),
    CONSTRAINT meteostationid_fkey FOREIGN KEY (meteostationid)
        REFERENCES public.meteo_stations(id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.observation
    OWNER to postgres;

-- Index: fki_meteostationid_fkey

-- DROP INDEX public.fki_meteostationid_fkey;

CREATE INDEX fki_meteostationid_fkey
    ON public.observation USING btree
    (meteostationid)
    TABLESPACE pg_default;