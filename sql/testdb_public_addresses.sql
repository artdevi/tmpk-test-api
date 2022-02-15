create table addresses
(
    id          serial
        constraint addresses_pkey
            primary key,
    contract_id integer      not null
        constraint addresses_contract_id_fkey
            references contracts,
    city        varchar(100) not null,
    street      varchar(100) not null,
    house       varchar(16)  not null,
    apartment   integer      not null
);

alter table addresses
    owner to postgres;

INSERT INTO public.addresses (id, contract_id, city, street, house, apartment) VALUES (1, 1, 'Дубна', 'Боголюбова', '1А', 11);