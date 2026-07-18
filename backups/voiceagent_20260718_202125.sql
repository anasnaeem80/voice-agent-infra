--
-- PostgreSQL database dump
--

\restrict bd3Q2yDp6GrnutbcfXD9iiHSZ1ROANOSbvWAo17utEXBVkmwfKebRC2UAA8gSLd

-- Dumped from database version 16.14 (Debian 16.14-1.pgdg13+1)
-- Dumped by pg_dump version 16.14 (Debian 16.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: call_records; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.call_records (
    id integer NOT NULL,
    patient_name character varying(255) NOT NULL,
    date_of_birth character varying(50),
    phone_number character varying(50),
    reason character varying(500),
    status character varying(100),
    created_at timestamp without time zone
);


ALTER TABLE public.call_records OWNER TO postgres;

--
-- Name: call_records_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.call_records_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.call_records_id_seq OWNER TO postgres;

--
-- Name: call_records_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.call_records_id_seq OWNED BY public.call_records.id;


--
-- Name: call_records id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.call_records ALTER COLUMN id SET DEFAULT nextval('public.call_records_id_seq'::regclass);


--
-- Data for Name: call_records; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.call_records (id, patient_name, date_of_birth, phone_number, reason, status, created_at) FROM stdin;
1	Anas Naeem	2002-03-02	+921234567890	Need an appointment	received	2026-07-18 15:06:52.015692
\.


--
-- Name: call_records_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.call_records_id_seq', 1, true);


--
-- Name: call_records call_records_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.call_records
    ADD CONSTRAINT call_records_pkey PRIMARY KEY (id);


--
-- Name: ix_call_records_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_call_records_id ON public.call_records USING btree (id);


--
-- PostgreSQL database dump complete
--

\unrestrict bd3Q2yDp6GrnutbcfXD9iiHSZ1ROANOSbvWAo17utEXBVkmwfKebRC2UAA8gSLd

