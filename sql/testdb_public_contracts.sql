create table contracts
(
    id              serial
        constraint contracts_pkey
            primary key,
    name            varchar(150) not null,
    balance         integer      not null,
    is_legal_entity boolean      not null,
    is_active       boolean      not null
);

alter table contracts
    owner to postgres;

INSERT INTO public.contracts (id, name, balance, is_legal_entity, is_active) VALUES (1, 'Тохталиев Анис Ринатович', 0, true, true);