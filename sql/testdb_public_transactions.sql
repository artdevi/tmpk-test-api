create table transactions
(
    id          serial
        constraint transactions_pkey
            primary key,
    contract_id integer   not null
        constraint transactions_contract_id_fkey
            references contracts,
    sum         integer   not null,
    datetime    timestamp not null
);

alter table transactions
    owner to postgres;

INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (1, 1, 400, '2020-05-15 00:59:21.000000');
INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (2, 1, 500, '2020-07-21 00:59:52.000000');
INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (3, 1, 400, '2020-08-18 01:00:12.000000');
INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (4, 1, 100, '2020-09-20 01:00:29.000000');
INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (5, 1, 600, '2021-01-15 01:00:42.000000');
INSERT INTO public.transactions (id, contract_id, sum, datetime) VALUES (6, 1, 300, '2022-02-15 01:01:05.000000');