PGDMP      	                |            innout    16.4    16.4 `    $           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            %           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            &           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            '           1262    16959    innout    DATABASE     z   CREATE DATABASE innout WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE innout;
                postgres    false            �            1259    17115    access_levels    TABLE     |   CREATE TABLE public.access_levels (
    id_access_level integer NOT NULL,
    level_name character varying(255) NOT NULL
);
 !   DROP TABLE public.access_levels;
       public         heap    postgres    false            �            1259    17114 !   access_levels_id_access_level_seq    SEQUENCE     �   CREATE SEQUENCE public.access_levels_id_access_level_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.access_levels_id_access_level_seq;
       public          postgres    false    234            (           0    0 !   access_levels_id_access_level_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.access_levels_id_access_level_seq OWNED BY public.access_levels.id_access_level;
          public          postgres    false    233            �            1259    16968    add_ons    TABLE     �   CREATE TABLE public.add_ons (
    id_addons integer NOT NULL,
    id_solution_type integer,
    name_addons character varying(255) NOT NULL,
    addons_price numeric(10,2) NOT NULL
);
    DROP TABLE public.add_ons;
       public         heap    postgres    false            �            1259    16967    add_ons_id_addons_seq    SEQUENCE     �   CREATE SEQUENCE public.add_ons_id_addons_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.add_ons_id_addons_seq;
       public          postgres    false    218            )           0    0    add_ons_id_addons_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.add_ons_id_addons_seq OWNED BY public.add_ons.id_addons;
          public          postgres    false    217            �            1259    17087    center_help    TABLE     �   CREATE TABLE public.center_help (
    id_ticket integer NOT NULL,
    id_client_user integer,
    subject character varying(255) NOT NULL,
    what_happend text NOT NULL,
    what_would_u_want text,
    files bytea
);
    DROP TABLE public.center_help;
       public         heap    postgres    false            �            1259    17086    center_help_id_ticket_seq    SEQUENCE     �   CREATE SEQUENCE public.center_help_id_ticket_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.center_help_id_ticket_seq;
       public          postgres    false    230            *           0    0    center_help_id_ticket_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.center_help_id_ticket_seq OWNED BY public.center_help.id_ticket;
          public          postgres    false    229            �            1259    17050    client_account    TABLE     L  CREATE TABLE public.client_account (
    id_client_user integer NOT NULL,
    serial_id_client character varying(50) NOT NULL,
    password character varying(255) NOT NULL,
    id_payment integer,
    id_solution integer,
    id_solution_type integer,
    id_addons integer,
    id_service integer,
    id_client_billing integer
);
 "   DROP TABLE public.client_account;
       public         heap    postgres    false            �            1259    17049 !   client_account_id_client_user_seq    SEQUENCE     �   CREATE SEQUENCE public.client_account_id_client_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.client_account_id_client_user_seq;
       public          postgres    false    228            +           0    0 !   client_account_id_client_user_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.client_account_id_client_user_seq OWNED BY public.client_account.id_client_user;
          public          postgres    false    227            �            1259    17009    client_billing    TABLE     �  CREATE TABLE public.client_billing (
    id_client_billing integer NOT NULL,
    domain character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    company character varying(255) NOT NULL,
    phone character varying(20) NOT NULL,
    street character varying(255),
    city character varying(255),
    state character varying(255),
    zip character varying(10),
    country character varying(255)
);
 "   DROP TABLE public.client_billing;
       public         heap    postgres    false            �            1259    17008 $   client_billing_id_client_billing_seq    SEQUENCE     �   CREATE SEQUENCE public.client_billing_id_client_billing_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.client_billing_id_client_billing_seq;
       public          postgres    false    224            ,           0    0 $   client_billing_id_client_billing_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.client_billing_id_client_billing_seq OWNED BY public.client_billing.id_client_billing;
          public          postgres    false    223            �            1259    16987    custom_solution    TABLE       CREATE TABLE public.custom_solution (
    id_solution integer NOT NULL,
    id_addons integer,
    id_solution_type integer,
    id_service integer,
    number_of_users integer NOT NULL,
    month_year character varying(20) NOT NULL,
    total_price numeric(10,2) NOT NULL
);
 #   DROP TABLE public.custom_solution;
       public         heap    postgres    false            �            1259    16986    custom_solution_id_solution_seq    SEQUENCE     �   CREATE SEQUENCE public.custom_solution_id_solution_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.custom_solution_id_solution_seq;
       public          postgres    false    222            -           0    0    custom_solution_id_solution_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.custom_solution_id_solution_seq OWNED BY public.custom_solution.id_solution;
          public          postgres    false    221            �            1259    17018    payment    TABLE     �  CREATE TABLE public.payment (
    id_payment integer NOT NULL,
    id_solution integer,
    id_addons integer,
    id_solution_type integer,
    id_service integer,
    id_client_billing integer,
    card_number character varying(20) NOT NULL,
    card_code character varying(5) NOT NULL,
    card_date date NOT NULL,
    success boolean NOT NULL,
    payment_date timestamp without time zone NOT NULL,
    formed_payment_date timestamp without time zone NOT NULL
);
    DROP TABLE public.payment;
       public         heap    postgres    false            �            1259    17017    payment_id_payment_seq    SEQUENCE     �   CREATE SEQUENCE public.payment_id_payment_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.payment_id_payment_seq;
       public          postgres    false    226            .           0    0    payment_id_payment_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.payment_id_payment_seq OWNED BY public.payment.id_payment;
          public          postgres    false    225            �            1259    16980    service    TABLE     �   CREATE TABLE public.service (
    id_service integer NOT NULL,
    name_service character varying(255) NOT NULL,
    service_price numeric(10,2) NOT NULL
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    16979    service_id_service_seq    SEQUENCE     �   CREATE SEQUENCE public.service_id_service_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.service_id_service_seq;
       public          postgres    false    220            /           0    0    service_id_service_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.service_id_service_seq OWNED BY public.service.id_service;
          public          postgres    false    219            �            1259    16961    solution_type    TABLE     �   CREATE TABLE public.solution_type (
    id_solution_type integer NOT NULL,
    name_solution_type character varying(255) NOT NULL,
    solution_type_price numeric(10,2) NOT NULL
);
 !   DROP TABLE public.solution_type;
       public         heap    postgres    false            �            1259    16960 "   solution_type_id_solution_type_seq    SEQUENCE     �   CREATE SEQUENCE public.solution_type_id_solution_type_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.solution_type_id_solution_type_seq;
       public          postgres    false    216            0           0    0 "   solution_type_id_solution_type_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.solution_type_id_solution_type_seq OWNED BY public.solution_type.id_solution_type;
          public          postgres    false    215            �            1259    17121    user_access_levels    TABLE     o   CREATE TABLE public.user_access_levels (
    id_user integer NOT NULL,
    id_access_level integer NOT NULL
);
 &   DROP TABLE public.user_access_levels;
       public         heap    postgres    false            �            1259    17101    users    TABLE     �   CREATE TABLE public.users (
    id_user integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    id_client_user integer
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    17100    users_id_user_seq    SEQUENCE     �   CREATE SEQUENCE public.users_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_id_user_seq;
       public          postgres    false    232            1           0    0    users_id_user_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_id_user_seq OWNED BY public.users.id_user;
          public          postgres    false    231            T           2604    17118    access_levels id_access_level    DEFAULT     �   ALTER TABLE ONLY public.access_levels ALTER COLUMN id_access_level SET DEFAULT nextval('public.access_levels_id_access_level_seq'::regclass);
 L   ALTER TABLE public.access_levels ALTER COLUMN id_access_level DROP DEFAULT;
       public          postgres    false    234    233    234            L           2604    16971    add_ons id_addons    DEFAULT     v   ALTER TABLE ONLY public.add_ons ALTER COLUMN id_addons SET DEFAULT nextval('public.add_ons_id_addons_seq'::regclass);
 @   ALTER TABLE public.add_ons ALTER COLUMN id_addons DROP DEFAULT;
       public          postgres    false    217    218    218            R           2604    17090    center_help id_ticket    DEFAULT     ~   ALTER TABLE ONLY public.center_help ALTER COLUMN id_ticket SET DEFAULT nextval('public.center_help_id_ticket_seq'::regclass);
 D   ALTER TABLE public.center_help ALTER COLUMN id_ticket DROP DEFAULT;
       public          postgres    false    230    229    230            Q           2604    17053    client_account id_client_user    DEFAULT     �   ALTER TABLE ONLY public.client_account ALTER COLUMN id_client_user SET DEFAULT nextval('public.client_account_id_client_user_seq'::regclass);
 L   ALTER TABLE public.client_account ALTER COLUMN id_client_user DROP DEFAULT;
       public          postgres    false    227    228    228            O           2604    17012     client_billing id_client_billing    DEFAULT     �   ALTER TABLE ONLY public.client_billing ALTER COLUMN id_client_billing SET DEFAULT nextval('public.client_billing_id_client_billing_seq'::regclass);
 O   ALTER TABLE public.client_billing ALTER COLUMN id_client_billing DROP DEFAULT;
       public          postgres    false    224    223    224            N           2604    16990    custom_solution id_solution    DEFAULT     �   ALTER TABLE ONLY public.custom_solution ALTER COLUMN id_solution SET DEFAULT nextval('public.custom_solution_id_solution_seq'::regclass);
 J   ALTER TABLE public.custom_solution ALTER COLUMN id_solution DROP DEFAULT;
       public          postgres    false    221    222    222            P           2604    17021    payment id_payment    DEFAULT     x   ALTER TABLE ONLY public.payment ALTER COLUMN id_payment SET DEFAULT nextval('public.payment_id_payment_seq'::regclass);
 A   ALTER TABLE public.payment ALTER COLUMN id_payment DROP DEFAULT;
       public          postgres    false    225    226    226            M           2604    16983    service id_service    DEFAULT     x   ALTER TABLE ONLY public.service ALTER COLUMN id_service SET DEFAULT nextval('public.service_id_service_seq'::regclass);
 A   ALTER TABLE public.service ALTER COLUMN id_service DROP DEFAULT;
       public          postgres    false    219    220    220            K           2604    16964    solution_type id_solution_type    DEFAULT     �   ALTER TABLE ONLY public.solution_type ALTER COLUMN id_solution_type SET DEFAULT nextval('public.solution_type_id_solution_type_seq'::regclass);
 M   ALTER TABLE public.solution_type ALTER COLUMN id_solution_type DROP DEFAULT;
       public          postgres    false    215    216    216            S           2604    17104    users id_user    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN id_user SET DEFAULT nextval('public.users_id_user_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN id_user DROP DEFAULT;
       public          postgres    false    231    232    232                       0    17115    access_levels 
   TABLE DATA           D   COPY public.access_levels (id_access_level, level_name) FROM stdin;
    public          postgres    false    234   �~                 0    16968    add_ons 
   TABLE DATA           Y   COPY public.add_ons (id_addons, id_solution_type, name_addons, addons_price) FROM stdin;
    public          postgres    false    218   �~                 0    17087    center_help 
   TABLE DATA           q   COPY public.center_help (id_ticket, id_client_user, subject, what_happend, what_would_u_want, files) FROM stdin;
    public          postgres    false    230                    0    17050    client_account 
   TABLE DATA           �   COPY public.client_account (id_client_user, serial_id_client, password, id_payment, id_solution, id_solution_type, id_addons, id_service, id_client_billing) FROM stdin;
    public          postgres    false    228   /                 0    17009    client_billing 
   TABLE DATA           }   COPY public.client_billing (id_client_billing, domain, email, company, phone, street, city, state, zip, country) FROM stdin;
    public          postgres    false    224   L                 0    16987    custom_solution 
   TABLE DATA           �   COPY public.custom_solution (id_solution, id_addons, id_solution_type, id_service, number_of_users, month_year, total_price) FROM stdin;
    public          postgres    false    222   i                 0    17018    payment 
   TABLE DATA           �   COPY public.payment (id_payment, id_solution, id_addons, id_solution_type, id_service, id_client_billing, card_number, card_code, card_date, success, payment_date, formed_payment_date) FROM stdin;
    public          postgres    false    226   �                 0    16980    service 
   TABLE DATA           J   COPY public.service (id_service, name_service, service_price) FROM stdin;
    public          postgres    false    220   �                 0    16961    solution_type 
   TABLE DATA           b   COPY public.solution_type (id_solution_type, name_solution_type, solution_type_price) FROM stdin;
    public          postgres    false    216   �       !          0    17121    user_access_levels 
   TABLE DATA           F   COPY public.user_access_levels (id_user, id_access_level) FROM stdin;
    public          postgres    false    235   �                 0    17101    users 
   TABLE DATA           O   COPY public.users (id_user, name, email, password, id_client_user) FROM stdin;
    public          postgres    false    232   �       2           0    0 !   access_levels_id_access_level_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.access_levels_id_access_level_seq', 1, false);
          public          postgres    false    233            3           0    0    add_ons_id_addons_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.add_ons_id_addons_seq', 1, false);
          public          postgres    false    217            4           0    0    center_help_id_ticket_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.center_help_id_ticket_seq', 1, false);
          public          postgres    false    229            5           0    0 !   client_account_id_client_user_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.client_account_id_client_user_seq', 1, false);
          public          postgres    false    227            6           0    0 $   client_billing_id_client_billing_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.client_billing_id_client_billing_seq', 1, false);
          public          postgres    false    223            7           0    0    custom_solution_id_solution_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.custom_solution_id_solution_seq', 1, false);
          public          postgres    false    221            8           0    0    payment_id_payment_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.payment_id_payment_seq', 1, false);
          public          postgres    false    225            9           0    0    service_id_service_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.service_id_service_seq', 1, false);
          public          postgres    false    219            :           0    0 "   solution_type_id_solution_type_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.solution_type_id_solution_type_seq', 1, false);
          public          postgres    false    215            ;           0    0    users_id_user_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.users_id_user_seq', 1, false);
          public          postgres    false    231            h           2606    17120     access_levels access_levels_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.access_levels
    ADD CONSTRAINT access_levels_pkey PRIMARY KEY (id_access_level);
 J   ALTER TABLE ONLY public.access_levels DROP CONSTRAINT access_levels_pkey;
       public            postgres    false    234            X           2606    16973    add_ons add_ons_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT add_ons_pkey PRIMARY KEY (id_addons);
 >   ALTER TABLE ONLY public.add_ons DROP CONSTRAINT add_ons_pkey;
       public            postgres    false    218            d           2606    17094    center_help center_help_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT center_help_pkey PRIMARY KEY (id_ticket);
 F   ALTER TABLE ONLY public.center_help DROP CONSTRAINT center_help_pkey;
       public            postgres    false    230            b           2606    17055 "   client_account client_account_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_pkey PRIMARY KEY (id_client_user);
 L   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_pkey;
       public            postgres    false    228            ^           2606    17016 "   client_billing client_billing_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.client_billing
    ADD CONSTRAINT client_billing_pkey PRIMARY KEY (id_client_billing);
 L   ALTER TABLE ONLY public.client_billing DROP CONSTRAINT client_billing_pkey;
       public            postgres    false    224            \           2606    16992 $   custom_solution custom_solution_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.custom_solution
    ADD CONSTRAINT custom_solution_pkey PRIMARY KEY (id_solution);
 N   ALTER TABLE ONLY public.custom_solution DROP CONSTRAINT custom_solution_pkey;
       public            postgres    false    222            `           2606    17023    payment payment_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (id_payment);
 >   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_pkey;
       public            postgres    false    226            Z           2606    16985    service service_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (id_service);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    220            V           2606    16966     solution_type solution_type_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.solution_type
    ADD CONSTRAINT solution_type_pkey PRIMARY KEY (id_solution_type);
 J   ALTER TABLE ONLY public.solution_type DROP CONSTRAINT solution_type_pkey;
       public            postgres    false    216            j           2606    17125 *   user_access_levels user_access_levels_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.user_access_levels
    ADD CONSTRAINT user_access_levels_pkey PRIMARY KEY (id_user, id_access_level);
 T   ALTER TABLE ONLY public.user_access_levels DROP CONSTRAINT user_access_levels_pkey;
       public            postgres    false    235    235            f           2606    17108    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id_user);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    232            k           2606    16974 %   add_ons add_ons_id_solution_type_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.add_ons
    ADD CONSTRAINT add_ons_id_solution_type_fkey FOREIGN KEY (id_solution_type) REFERENCES public.solution_type(id_solution_type);
 O   ALTER TABLE ONLY public.add_ons DROP CONSTRAINT add_ons_id_solution_type_fkey;
       public          postgres    false    216    218    4694            z           2606    17095 +   center_help center_help_id_client_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.center_help
    ADD CONSTRAINT center_help_id_client_user_fkey FOREIGN KEY (id_client_user) REFERENCES public.client_account(id_client_user);
 U   ALTER TABLE ONLY public.center_help DROP CONSTRAINT center_help_id_client_user_fkey;
       public          postgres    false    230    4706    228            t           2606    17071 ,   client_account client_account_id_addons_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_addons_fkey FOREIGN KEY (id_addons) REFERENCES public.add_ons(id_addons);
 V   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_addons_fkey;
       public          postgres    false    218    4696    228            u           2606    17081 4   client_account client_account_id_client_billing_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_client_billing_fkey FOREIGN KEY (id_client_billing) REFERENCES public.client_billing(id_client_billing);
 ^   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_client_billing_fkey;
       public          postgres    false    224    4702    228            v           2606    17056 -   client_account client_account_id_payment_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_payment_fkey FOREIGN KEY (id_payment) REFERENCES public.payment(id_payment);
 W   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_payment_fkey;
       public          postgres    false    228    4704    226            w           2606    17076 -   client_account client_account_id_service_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_service_fkey FOREIGN KEY (id_service) REFERENCES public.service(id_service);
 W   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_service_fkey;
       public          postgres    false    4698    220    228            x           2606    17061 .   client_account client_account_id_solution_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_solution_fkey FOREIGN KEY (id_solution) REFERENCES public.custom_solution(id_solution);
 X   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_solution_fkey;
       public          postgres    false    222    228    4700            y           2606    17066 3   client_account client_account_id_solution_type_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.client_account
    ADD CONSTRAINT client_account_id_solution_type_fkey FOREIGN KEY (id_solution_type) REFERENCES public.solution_type(id_solution_type);
 ]   ALTER TABLE ONLY public.client_account DROP CONSTRAINT client_account_id_solution_type_fkey;
       public          postgres    false    216    4694    228            l           2606    16993 .   custom_solution custom_solution_id_addons_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.custom_solution
    ADD CONSTRAINT custom_solution_id_addons_fkey FOREIGN KEY (id_addons) REFERENCES public.add_ons(id_addons);
 X   ALTER TABLE ONLY public.custom_solution DROP CONSTRAINT custom_solution_id_addons_fkey;
       public          postgres    false    4696    218    222            m           2606    17003 /   custom_solution custom_solution_id_service_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.custom_solution
    ADD CONSTRAINT custom_solution_id_service_fkey FOREIGN KEY (id_service) REFERENCES public.service(id_service);
 Y   ALTER TABLE ONLY public.custom_solution DROP CONSTRAINT custom_solution_id_service_fkey;
       public          postgres    false    220    4698    222            n           2606    16998 5   custom_solution custom_solution_id_solution_type_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.custom_solution
    ADD CONSTRAINT custom_solution_id_solution_type_fkey FOREIGN KEY (id_solution_type) REFERENCES public.solution_type(id_solution_type);
 _   ALTER TABLE ONLY public.custom_solution DROP CONSTRAINT custom_solution_id_solution_type_fkey;
       public          postgres    false    4694    222    216            o           2606    17029    payment payment_id_addons_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_id_addons_fkey FOREIGN KEY (id_addons) REFERENCES public.add_ons(id_addons);
 H   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_id_addons_fkey;
       public          postgres    false    218    4696    226            p           2606    17044 &   payment payment_id_client_billing_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_id_client_billing_fkey FOREIGN KEY (id_client_billing) REFERENCES public.client_billing(id_client_billing);
 P   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_id_client_billing_fkey;
       public          postgres    false    224    4702    226            q           2606    17039    payment payment_id_service_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_id_service_fkey FOREIGN KEY (id_service) REFERENCES public.service(id_service);
 I   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_id_service_fkey;
       public          postgres    false    4698    226    220            r           2606    17024     payment payment_id_solution_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_id_solution_fkey FOREIGN KEY (id_solution) REFERENCES public.custom_solution(id_solution);
 J   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_id_solution_fkey;
       public          postgres    false    226    4700    222            s           2606    17034 %   payment payment_id_solution_type_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_id_solution_type_fkey FOREIGN KEY (id_solution_type) REFERENCES public.solution_type(id_solution_type);
 O   ALTER TABLE ONLY public.payment DROP CONSTRAINT payment_id_solution_type_fkey;
       public          postgres    false    226    4694    216            |           2606    17131 :   user_access_levels user_access_levels_id_access_level_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_access_levels
    ADD CONSTRAINT user_access_levels_id_access_level_fkey FOREIGN KEY (id_access_level) REFERENCES public.access_levels(id_access_level) ON DELETE CASCADE;
 d   ALTER TABLE ONLY public.user_access_levels DROP CONSTRAINT user_access_levels_id_access_level_fkey;
       public          postgres    false    234    235    4712            }           2606    17126 2   user_access_levels user_access_levels_id_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.user_access_levels
    ADD CONSTRAINT user_access_levels_id_user_fkey FOREIGN KEY (id_user) REFERENCES public.users(id_user) ON DELETE CASCADE;
 \   ALTER TABLE ONLY public.user_access_levels DROP CONSTRAINT user_access_levels_id_user_fkey;
       public          postgres    false    235    232    4710            {           2606    17109    users users_id_client_user_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_id_client_user_fkey FOREIGN KEY (id_client_user) REFERENCES public.client_account(id_client_user);
 I   ALTER TABLE ONLY public.users DROP CONSTRAINT users_id_client_user_fkey;
       public          postgres    false    228    4706    232                   x������ � �            x������ � �            x������ � �            x������ � �            x������ � �            x������ � �            x������ � �            x������ � �            x������ � �      !      x������ � �            x������ � �     