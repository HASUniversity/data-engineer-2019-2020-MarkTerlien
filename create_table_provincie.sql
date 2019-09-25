-- Table: public.provincie

-- DROP TABLE public.provincie;

CREATE TABLE public.provincie
(
    id integer NOT NULL,
    geom geometry(Geometry,4326),
    provnaam character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT provincie_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.provincie
    OWNER to postgres;