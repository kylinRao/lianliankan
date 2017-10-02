drop table if exists wzryStore;
drop table if exists Store;
create table Store (
  aid integer primary key autoincrement,
  pic string not null,
  name string not null,
  price int not null,
  basicPro string not null,
  skill string

);
drop table if exists wzryStoreType;
create table wzryStoreType (
  id integer primary key autoincrement,
  type int not null,
  des string not null
);

drop table if exists wzryStoreLayer;
create table wzryStoreLayer (
  id integer primary key autoincrement,
  type int not null,
  des string not null
);


drop table if exists wzryStoreAttackType;
create table wzryStoreAttackType (
  id integer primary key autoincrement,
  type int not null,
  des string not null
);

drop table if exists wzryStoreDefendType;
create table wzryStoreDefendType (
  id integer primary key autoincrement,
  type int not null,
  des string not null
);

-- 初始化类型数据，道具类型表
insert into wzryStoreType (type,des) values (0,"全部");
insert into wzryStoreType (type,des) values (1,"攻击");
insert into wzryStoreType (type,des) values (2,"法术");
insert into wzryStoreType (type,des) values (3,"防御");
insert into wzryStoreType (type,des) values (4,"移动");
insert into wzryStoreType (type,des) values (5,"打野");
-- 初始化层级数据，道具层级表
insert into wzryStoreLayer (type,des) values (0,"全部");
insert into wzryStoreLayer (type,des) values (1,"小件");
insert into wzryStoreLayer (type,des) values (2,"中件");
insert into wzryStoreLayer (type,des) values (3,"大件");
-- 初始化攻击属性数据，道具攻击属性表
insert into wzryStoreAttackType (type,des) values (0,"全部");
insert into wzryStoreAttackType (type,des) values (1,"物理攻击");
insert into wzryStoreAttackType (type,des) values (2,"暴击");
insert into wzryStoreAttackType (type,des) values (3,"攻击速度");
insert into wzryStoreAttackType (type,des) values (4,"物理吸血");
insert into wzryStoreAttackType (type,des) values (4,"法术攻击");
-- 初始化防御属性数据，道具防御属性表
insert into wzryStoreDefendType (type,des) values (0,"全部");
insert into wzryStoreDefendType (type,des) values (1,"最大生命");
insert into wzryStoreDefendType (type,des) values (2,"物理防御");
insert into wzryStoreDefendType (type,des) values (3,"法术防御");
insert into wzryStoreDefendType (type,des) values (0,"冷却缩减");
insert into wzryStoreDefendType (type,des) values (0,"移速");

