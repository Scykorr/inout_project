toc.dat                                                                                             0000600 0004000 0002000 00000042200 14657712732 0014453 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       	                |            innout    16.4    16.4 3    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    16493    innout    DATABASE     z   CREATE DATABASE innout WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE innout;
                postgres    false                     2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false         �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4         �            1259    16509    add_ons    TABLE     �   CREATE TABLE public.add_ons (
    id_addons bigint NOT NULL,
    name_addons character varying(30),
    addons_price money NOT NULL,
    fk_solution_type bigint NOT NULL
);
    DROP TABLE public.add_ons;
       public         heap    postgres    false    4         �            1259    16640    center_help    TABLE     �   CREATE TABLE public.center_help (
    id_ticket bigint NOT NULL,
    fk_client_user bigint,
    subject character varying(10),
    what_happend text,
    what_would_u_like text,
    url text,
    files bytea
);
    DROP TABLE public.center_help;
       public         heap    postgres    false    4         �            1259    16576    client_account    TABLE     r  CREATE TABLE public.client_account (
    id_client_user bigint NOT NULL,
    serial_id_client character varying NOT NULL,
    password character varying NOT NULL,
    fk_payment bigint NOT NULL,
    fk_solution bigint NOT NULL,
    fk_addons bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    id_client_billing bigint NOT NULL
);
 "   DROP TABLE public.client_account;
       public         heap    postgres    false    4         �            1259    16504    client_billing    TABLE     �  CREATE TABLE public.client_billing (
    " id_client_billing" bigint NOT NULL,
    domain character varying(50) NOT NULL,
    email character varying(40) NOT NULL,
    company character varying(50) NOT NULL,
    phone character varying(20) NOT NULL,
    street character varying(40) NOT NULL,
    city character varying(20) NOT NULL,
    zip character varying(20) NOT NULL,
    state character varying(20) NOT NULL,
    inn character varying(30) NOT NULL
);
 "   DROP TABLE public.client_billing;
       public         heap    postgres    false    4         �            1259    16514    customer_solution    TABLE     '  CREATE TABLE public.customer_solution (
    id_solution bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    number_of_users integer NOT NULL,
    "month/year" character varying(10) NOT NULL,
    total_price money NOT NULL,
    fk_addons bigint NOT NULL
);
 %   DROP TABLE public.customer_solution;
       public         heap    postgres    false    4         �            1259    16546    payment    TABLE     �  CREATE TABLE public.payment (
    id_payment bigint NOT NULL,
    fk_solution bigint NOT NULL,
    fk_addons bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    fk_client_billing bigint NOT NULL,
    card_number character varying(50) NOT NULL,
    card_date character varying(10) NOT NULL,
    card_code character varying(5) NOT NULL,
    sucess boolean NOT NULL,
    payment_date date NOT NULL,
    formed_payment_date date NOT NULL
);
    DROP TABLE public.payment;
       public         heap    postgres    false    4         �            1259    16499    service    TABLE     �   CREATE TABLE public.service (
    id_service bigint NOT NULL,
    name_service character varying(50),
    price_service money NOT NULL
);
    DROP TABLE public.service;
       public         heap    postgres    false    4         �            1259    16494    solution_type    TABLE     �   CREATE TABLE public.solution_type (
    id_solution_type bigint NOT NULL,
    name_solution_type character varying(50),
    solution_type_price money NOT NULL
);
 !   DROP TABLE public.solution_type;
       public         heap    postgres    false    4         �            1259    16652    users    TABLE     �   CREATE TABLE public.users (
    id_user bigint NOT NULL,
    name character varying(50),
    level_acess character varying(10)[],
    email character varying(20),
    password character varying(30),
    fk_client_user bigint NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false    4         �          0    16509    add_ons 
   TABLE DATA           Y   COPY public.add_ons (id_addons, name_addons, addons_price, fk_solution_type) FROM stdin;
    public          postgres    false    218       4848.dat �          0    16640    center_help 
   TABLE DATA           v   COPY public.center_help (id_ticket, fk_client_user, subject, what_happend, what_would_u_like, url, files) FROM stdin;
    public          postgres    false    222       4852.dat �          0    16576    client_account 
   TABLE DATA           �   COPY public.client_account (id_client_user, serial_id_client, password, fk_payment, fk_solution, fk_addons, fk_solution_type, fk_service, id_client_billing) FROM stdin;
    public          postgres    false    221       4851.dat �          0    16504    client_billing 
   TABLE DATA           |   COPY public.client_billing (" id_client_billing", domain, email, company, phone, street, city, zip, state, inn) FROM stdin;
    public          postgres    false    217       4847.dat �          0    16514    customer_solution 
   TABLE DATA           �   COPY public.customer_solution (id_solution, fk_solution_type, fk_service, number_of_users, "month/year", total_price, fk_addons) FROM stdin;
    public          postgres    false    219       4849.dat �          0    16546    payment 
   TABLE DATA           �   COPY public.payment (id_payment, fk_solution, fk_addons, fk_solution_type, fk_service, fk_client_billing, card_number, card_date, card_code, sucess, payment_date, formed_payment_date) FROM stdin;
    public          postgres    false    220       4850.dat �          0    16499    service 
   TABLE DATA           J   COPY public.service (id_service, name_service, price_service) FROM stdin;
    public          postgres    false    216       4846.dat �          0    16494    solution_type 
   TABLE DATA           b   COPY public.solution_type (id_solution_type, name_solution_type, solution_type_price) FROM stdin;
    public          postgres    false    215       4845.dat �          0    16652    users 
   TABLE DATA           \   COPY public.users (id_user, name, level_acess, email, password, fk_client_user) FROM stdin;
    public          postgres    false    223       4853.dat @           2606    16513    add_ons add_ons_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT add_ons_pkey PRIMARY KEY (id_addons);
 >   ALTER TABLE ONLY public.add_ons DROP CONSTRAINT add_ons_pkey;
       public            postgres    false    218         J           2606    16646    center_help center_help_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT center_help_pkey PRIMARY KEY (id_ticket);
 F   ALTER TABLE ONLY public.center_help DROP CONSTRAINT center_help_pkey;
       public            postgres    false    222         H           2606    16582 "   client_account client_account_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_pkey PRIMARY KEY (id_client_user);
 L   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_pkey;
       public            postgres    false    221         >           2606    16508 "   client_billing client_billing_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.client_billing
    ADD CONSTRAINT client_billing_pkey PRIMARY KEY (" id_client_billing");
 L   ALTER TABLE ONLY public.client_billing DROP CONSTRAINT client_billing_pkey;
       public            postgres    false    217         B           2606    16518 (   customer_solution customer_solution_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT customer_solution_pkey PRIMARY KEY (id_solution);
 R   ALTER TABLE ONLY public.customer_solution DROP CONSTRAINT customer_solution_pkey;
       public            postgres    false    219         D           2606    16609 ,   payment payment_fk_solution_fk_solution1_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_fk_solution_fk_solution1_key UNIQUE (fk_solution) INCLUDE (fk_solution);
 V   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_fk_solution_fk_solution1_key;
       public            postgres    false    220         F           2606    16550    payment payment_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (id_payment);
 >   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_pkey;
       public            postgres    false    220         <           2606    16503    service service_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (id_service);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    216         :           2606    16498     solution_type solution_type_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.solution_type
    ADD CONSTRAINT solution_type_pkey PRIMARY KEY (id_solution_type);
 J   ALTER TABLE ONLY public.solution_type DROP CONSTRAINT solution_type_pkey;
       public            postgres    false    215         L           2606    16658    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    223         V           2606    16615    client_account  payment    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT " payment" FOREIGN KEY (fk_payment) REFERENCES public.payment(id_payment) NOT VALID;
 C   ALTER TABLE ONLY public.client_account DROP CONSTRAINT " payment";
       public          postgres    false    221    220    4678         N           2606    16531    customer_solution addons    FK CONSTRAINT     �   ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;
 B   ALTER TABLE ONLY public.customer_solution DROP CONSTRAINT addons;
       public          postgres    false    4672    218    219         Q           2606    16603    payment addons    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;
 8   ALTER TABLE ONLY public.payment DROP CONSTRAINT addons;
       public          postgres    false    218    220    4672         W           2606    16620    client_account addons    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;
 ?   ALTER TABLE ONLY public.client_account DROP CONSTRAINT addons;
       public          postgres    false    221    4672    218         R           2606    16598    payment client_billing    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT client_billing FOREIGN KEY (fk_client_billing) REFERENCES public.client_billing(" id_client_billing") NOT VALID;
 @   ALTER TABLE ONLY public.payment DROP CONSTRAINT client_billing;
       public          postgres    false    220    217    4670         X           2606    16635    client_account client_billing    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_billing FOREIGN KEY (id_client_billing) REFERENCES public.client_billing(" id_client_billing") NOT VALID;
 G   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_billing;
       public          postgres    false    217    4670    221         \           2606    16647    center_help client_user    FK CONSTRAINT     �   ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT client_user FOREIGN KEY (fk_client_user) REFERENCES public.client_account(id_client_user) NOT VALID;
 A   ALTER TABLE ONLY public.center_help DROP CONSTRAINT client_user;
       public          postgres    false    222    221    4680         ]           2606    16659    users client_user    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT client_user FOREIGN KEY (fk_client_user) REFERENCES public.client_account(id_client_user) NOT VALID;
 ;   ALTER TABLE ONLY public.users DROP CONSTRAINT client_user;
       public          postgres    false    4680    223    221         O           2606    16541    customer_solution service    FK CONSTRAINT     �   ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;
 C   ALTER TABLE ONLY public.customer_solution DROP CONSTRAINT service;
       public          postgres    false    4668    216    219         S           2606    16593    payment service    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;
 9   ALTER TABLE ONLY public.payment DROP CONSTRAINT service;
       public          postgres    false    220    216    4668         Y           2606    16630    client_account service    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;
 @   ALTER TABLE ONLY public.client_account DROP CONSTRAINT service;
       public          postgres    false    4668    216    221         T           2606    16583    payment solution    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT solution FOREIGN KEY (fk_solution) REFERENCES public.customer_solution(id_solution) NOT VALID;
 :   ALTER TABLE ONLY public.payment DROP CONSTRAINT solution;
       public          postgres    false    219    220    4674         Z           2606    16610    client_account solution    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT solution FOREIGN KEY (fk_solution) REFERENCES public.customer_solution(id_solution) NOT VALID;
 A   ALTER TABLE ONLY public.client_account DROP CONSTRAINT solution;
       public          postgres    false    221    4674    219         M           2606    16519    add_ons solution_type    FK CONSTRAINT     �   ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;
 ?   ALTER TABLE ONLY public.add_ons DROP CONSTRAINT solution_type;
       public          postgres    false    215    218    4666         P           2606    16536    customer_solution solution_type    FK CONSTRAINT     �   ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;
 I   ALTER TABLE ONLY public.customer_solution DROP CONSTRAINT solution_type;
       public          postgres    false    219    215    4666         U           2606    16588    payment solution_type    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;
 ?   ALTER TABLE ONLY public.payment DROP CONSTRAINT solution_type;
       public          postgres    false    215    4666    220         [           2606    16625    client_account solution_type    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;
 F   ALTER TABLE ONLY public.client_account DROP CONSTRAINT solution_type;
       public          postgres    false    215    221    4666                                                                                                                                                                                                                                                                                                                                                                                                        4848.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4852.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014265 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4851.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014264 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4847.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014271 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4849.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014273 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4850.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4846.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014270 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4845.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4853.dat                                                                                            0000600 0004000 0002000 00000000005 14657712732 0014266 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           restore.sql                                                                                         0000600 0004000 0002000 00000034407 14657712732 0015412 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

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

DROP DATABASE innout;
--
-- Name: innout; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE innout WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';


ALTER DATABASE innout OWNER TO postgres;

\connect innout

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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: add_ons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.add_ons (
    id_addons bigint NOT NULL,
    name_addons character varying(30),
    addons_price money NOT NULL,
    fk_solution_type bigint NOT NULL
);


ALTER TABLE public.add_ons OWNER TO postgres;

--
-- Name: center_help; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.center_help (
    id_ticket bigint NOT NULL,
    fk_client_user bigint,
    subject character varying(10),
    what_happend text,
    what_would_u_like text,
    url text,
    files bytea
);


ALTER TABLE public.center_help OWNER TO postgres;

--
-- Name: client_account; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client_account (
    id_client_user bigint NOT NULL,
    serial_id_client character varying NOT NULL,
    password character varying NOT NULL,
    fk_payment bigint NOT NULL,
    fk_solution bigint NOT NULL,
    fk_addons bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    id_client_billing bigint NOT NULL
);


ALTER TABLE public.client_account OWNER TO postgres;

--
-- Name: client_billing; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client_billing (
    " id_client_billing" bigint NOT NULL,
    domain character varying(50) NOT NULL,
    email character varying(40) NOT NULL,
    company character varying(50) NOT NULL,
    phone character varying(20) NOT NULL,
    street character varying(40) NOT NULL,
    city character varying(20) NOT NULL,
    zip character varying(20) NOT NULL,
    state character varying(20) NOT NULL,
    inn character varying(30) NOT NULL
);


ALTER TABLE public.client_billing OWNER TO postgres;

--
-- Name: customer_solution; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer_solution (
    id_solution bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    number_of_users integer NOT NULL,
    "month/year" character varying(10) NOT NULL,
    total_price money NOT NULL,
    fk_addons bigint NOT NULL
);


ALTER TABLE public.customer_solution OWNER TO postgres;

--
-- Name: payment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment (
    id_payment bigint NOT NULL,
    fk_solution bigint NOT NULL,
    fk_addons bigint NOT NULL,
    fk_solution_type bigint NOT NULL,
    fk_service bigint NOT NULL,
    fk_client_billing bigint NOT NULL,
    card_number character varying(50) NOT NULL,
    card_date character varying(10) NOT NULL,
    card_code character varying(5) NOT NULL,
    sucess boolean NOT NULL,
    payment_date date NOT NULL,
    formed_payment_date date NOT NULL
);


ALTER TABLE public.payment OWNER TO postgres;

--
-- Name: service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service (
    id_service bigint NOT NULL,
    name_service character varying(50),
    price_service money NOT NULL
);


ALTER TABLE public.service OWNER TO postgres;

--
-- Name: solution_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.solution_type (
    id_solution_type bigint NOT NULL,
    name_solution_type character varying(50),
    solution_type_price money NOT NULL
);


ALTER TABLE public.solution_type OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id_user bigint NOT NULL,
    name character varying(50),
    level_acess character varying(10)[],
    email character varying(20),
    password character varying(30),
    fk_client_user bigint NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: add_ons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.add_ons (id_addons, name_addons, addons_price, fk_solution_type) FROM stdin;
\.
COPY public.add_ons (id_addons, name_addons, addons_price, fk_solution_type) FROM '$$PATH$$/4848.dat';

--
-- Data for Name: center_help; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.center_help (id_ticket, fk_client_user, subject, what_happend, what_would_u_like, url, files) FROM stdin;
\.
COPY public.center_help (id_ticket, fk_client_user, subject, what_happend, what_would_u_like, url, files) FROM '$$PATH$$/4852.dat';

--
-- Data for Name: client_account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client_account (id_client_user, serial_id_client, password, fk_payment, fk_solution, fk_addons, fk_solution_type, fk_service, id_client_billing) FROM stdin;
\.
COPY public.client_account (id_client_user, serial_id_client, password, fk_payment, fk_solution, fk_addons, fk_solution_type, fk_service, id_client_billing) FROM '$$PATH$$/4851.dat';

--
-- Data for Name: client_billing; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.client_billing (" id_client_billing", domain, email, company, phone, street, city, zip, state, inn) FROM stdin;
\.
COPY public.client_billing (" id_client_billing", domain, email, company, phone, street, city, zip, state, inn) FROM '$$PATH$$/4847.dat';

--
-- Data for Name: customer_solution; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer_solution (id_solution, fk_solution_type, fk_service, number_of_users, "month/year", total_price, fk_addons) FROM stdin;
\.
COPY public.customer_solution (id_solution, fk_solution_type, fk_service, number_of_users, "month/year", total_price, fk_addons) FROM '$$PATH$$/4849.dat';

--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payment (id_payment, fk_solution, fk_addons, fk_solution_type, fk_service, fk_client_billing, card_number, card_date, card_code, sucess, payment_date, formed_payment_date) FROM stdin;
\.
COPY public.payment (id_payment, fk_solution, fk_addons, fk_solution_type, fk_service, fk_client_billing, card_number, card_date, card_code, sucess, payment_date, formed_payment_date) FROM '$$PATH$$/4850.dat';

--
-- Data for Name: service; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service (id_service, name_service, price_service) FROM stdin;
\.
COPY public.service (id_service, name_service, price_service) FROM '$$PATH$$/4846.dat';

--
-- Data for Name: solution_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.solution_type (id_solution_type, name_solution_type, solution_type_price) FROM stdin;
\.
COPY public.solution_type (id_solution_type, name_solution_type, solution_type_price) FROM '$$PATH$$/4845.dat';

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id_user, name, level_acess, email, password, fk_client_user) FROM stdin;
\.
COPY public.users (id_user, name, level_acess, email, password, fk_client_user) FROM '$$PATH$$/4853.dat';

--
-- Name: add_ons add_ons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT add_ons_pkey PRIMARY KEY (id_addons);


--
-- Name: center_help center_help_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT center_help_pkey PRIMARY KEY (id_ticket);


--
-- Name: client_account client_account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_pkey PRIMARY KEY (id_client_user);


--
-- Name: client_billing client_billing_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_billing
    ADD CONSTRAINT client_billing_pkey PRIMARY KEY (" id_client_billing");


--
-- Name: customer_solution customer_solution_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT customer_solution_pkey PRIMARY KEY (id_solution);


--
-- Name: payment payment_fk_solution_fk_solution1_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_fk_solution_fk_solution1_key UNIQUE (fk_solution) INCLUDE (fk_solution);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (id_payment);


--
-- Name: service service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (id_service);


--
-- Name: solution_type solution_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.solution_type
    ADD CONSTRAINT solution_type_pkey PRIMARY KEY (id_solution_type);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);


--
-- Name: client_account  payment; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT " payment" FOREIGN KEY (fk_payment) REFERENCES public.payment(id_payment) NOT VALID;


--
-- Name: customer_solution addons; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;


--
-- Name: payment addons; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;


--
-- Name: client_account addons; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT addons FOREIGN KEY (fk_addons) REFERENCES public.add_ons(id_addons) NOT VALID;


--
-- Name: payment client_billing; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT client_billing FOREIGN KEY (fk_client_billing) REFERENCES public.client_billing(" id_client_billing") NOT VALID;


--
-- Name: client_account client_billing; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_billing FOREIGN KEY (id_client_billing) REFERENCES public.client_billing(" id_client_billing") NOT VALID;


--
-- Name: center_help client_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT client_user FOREIGN KEY (fk_client_user) REFERENCES public.client_account(id_client_user) NOT VALID;


--
-- Name: users client_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT client_user FOREIGN KEY (fk_client_user) REFERENCES public.client_account(id_client_user) NOT VALID;


--
-- Name: customer_solution service; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;


--
-- Name: payment service; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;


--
-- Name: client_account service; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT service FOREIGN KEY (fk_service) REFERENCES public.service(id_service) NOT VALID;


--
-- Name: payment solution; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT solution FOREIGN KEY (fk_solution) REFERENCES public.customer_solution(id_solution) NOT VALID;


--
-- Name: client_account solution; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT solution FOREIGN KEY (fk_solution) REFERENCES public.customer_solution(id_solution) NOT VALID;


--
-- Name: add_ons solution_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;


--
-- Name: customer_solution solution_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer_solution
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;


--
-- Name: payment solution_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;


--
-- Name: client_account solution_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT solution_type FOREIGN KEY (fk_solution_type) REFERENCES public.solution_type(id_solution_type) NOT VALID;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         