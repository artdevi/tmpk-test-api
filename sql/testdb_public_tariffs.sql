create table tariffs
(
    id          serial
        constraint tariffs_pkey
            primary key,
    name        varchar(64) not null,
    price       integer     not null,
    start_date  date        not null,
    end_date    date,
    contract_id integer     not null
);

alter table tariffs
    owner to postgres;

INSERT INTO public.tariffs (id, name, price, start_date, end_date, contract_id) VALUES (1, 'Стандарт', 400, '2022-01-02', '2022-02-02', 1);
INSERT INTO public.tariffs (id, name, price, start_date, end_date, contract_id) VALUES (2, 'Премиум', 1200, '2022-02-02', null, 1);