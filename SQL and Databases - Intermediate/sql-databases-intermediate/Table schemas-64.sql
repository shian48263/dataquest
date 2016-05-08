## 2. Adding columns ##

alter table facts add leader text;

## 6. Creating a table with relations ##

create table factbook.states(
    id integer primary key,
    name text,
    area integer,
    country integer,
    foreign key(country) references facts(id)
);

## 7. Querying across foreign keys ##

select * from landmarks inner join facts on landmarks.country == facts.id;

## 8. Types of joins ##

select * from landmarks left outer join facts on landmarks.country == facts.id;