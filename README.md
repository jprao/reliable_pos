# reliable_pos
reliable POS API Application



## Create Database (PostgreSQL)
```sql
create database reliable_pos;
create role reliable_pos with password 'reliable_pos';
grant all privileges on database reliable_pos to reliable_pos;
alter role reliable_pos with login;
```
