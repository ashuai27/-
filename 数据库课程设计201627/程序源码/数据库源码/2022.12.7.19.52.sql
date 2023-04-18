-- create database campuscard_manage_system;
-- use campuscard_manage_system;
-- create database test;
-- drop database heu123;
use test;
drop table if exists charger;
drop table if exists consumer;
drop table if exists bankcard;
drop table if exists campuscard;
-- 创建校园卡信息表campuscard
create table campuscard
(
	campuscardid char(8) not null unique,
    studentid char(10) not null unique,
    sname char(24) not null ,
    sclass char(8) not null,
    balance double not null,
    card_status char(10) not null,
    create_time date not null,
    primary key(campuscardid)
);

-- show create table bankcard;
-- SET `fk_bankcard_campuscard` =0;
-- select * from bankcard where campuscardid= 20200001;
-- set foreign_key_checks = 0; delete from campuscard where campuscardid= '20200001'; set foreign_key_checks = 1;

-- 向campuscard表插入数据
INSERT INTO campuscard VALUES ('20200001', '2020201627', '钟帅', '20202016', 1000, '激活', '2022-11-12');
INSERT INTO campuscard VALUES ('20200002', '2020201628', '周孚佳', '20202016', 2000, '激活', '2022-11-11');
INSERT INTO campuscard VALUES ('20200003', '2020201629', '周浩宇', '20202016', 1500, '激活', '2022-11-11');
INSERT INTO campuscard VALUES ('20200006', '2020201632', '朱瑞东', '20202016', 1350, '激活', '2022-11-12');
INSERT INTO campuscard VALUES ('20200007', '2020201501', '宋立辉', '20202015', 2000, '激活', '2022-11-13');
INSERT INTO campuscard VALUES ('20200008', '2020201401', '陈子安', '20202014', 6000, '挂失', '2022-11-21');
INSERT INTO campuscard VALUES ('20200009', '2020201402', '杨馥菁', '20202014', 1500, '激活', '2022-11-13');
INSERT INTO campuscard VALUES ('20200010', '2020201301', '袁野', '20202013', 2300, '激活', '2022-11-23');

drop table if exists bankcard;
-- 创建银行卡信息表bankcard
create table bankcard
(
	bankcardid char(4) not null unique,
    sname char(24) not null ,
    balance double not null,
    campuscardid char(8) not null ,
    primary key(bankcardid),
    CONSTRAINT fk_bankcard_campuscard FOREIGN KEY(campuscardid) REFERENCES campuscard(campuscardid) ON DELETE CASCADE ON UPDATE CASCADE
    
);


-- 向bankcard表中插入数据
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0001', 4000, '钟帅', '20200001');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0003', 3299, '周孚佳', '20200002');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0004', 500, '周浩宇', '20200003');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0006', 300, '朱瑞东', '20200006');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0007', 2300, '宋立辉', '20200007');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0008', 4500, '陈子安', '20200008');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0009', 4000, '杨馥菁', '20200009');
INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0010', 3000, '袁野', '20200010');
-- INSERT INTO bankcard(bankcardid, balance, sname, campuscardid) VALUES ('0010', 3000, '袁野', '20200013');

drop table if exists manager;
-- 创建管理员信息表manager
create table manager
(
	account_ char(10) not null unique,
    password_ char(20) not null ,
    primary key(account_)
);

-- 初始化管理员信息表
INSERT INTO manager VALUES ('zs', 'password');

drop table if exists consumer;
-- 创建消费记录表 consumer
create table consumer
(
	campuscardid char(8) not null ,
    consum_money double not null,
    consum_address char(25) not null,
    consum_date date not null,
    CONSTRAINT fk_consumer_campuscard FOREIGN KEY(campuscardid) REFERENCES campuscard(campuscardid)
);

-- 向消费记录表插入数据
INSERT INTO consumer VALUES ('20200003', 13, '大美', '2022-12-01');
INSERT INTO consumer VALUES ('20200003', 15, '大美', '2022-12-01');
INSERT INTO consumer VALUES ('20200007', 45, '小美', '2022-12-02');
INSERT INTO consumer VALUES ('20200001', 30, '至美', '2022-12-03');
INSERT INTO consumer VALUES ('20200006', 30, '至美', '2022-12-03');
INSERT INTO consumer VALUES ('20200010', 78, '超市', '2022-12-05');
INSERT INTO consumer VALUES ('20200002', 13, '天美', '2022-12-07');
INSERT INTO consumer VALUES ('20200002', 13, '天美', '2022-12-07');
INSERT INTO consumer VALUES ('20200001', 3, '至美', '2022-12-04');

drop table if exists charger;
-- 创建充值表charger
create table charger
(
	campuscardid char(8) not null ,
    bankcardid char(4) not null,
    charge_money double not null,
    charge_date date not null,
    CONSTRAINT fk_charger_campuscard FOREIGN KEY(campuscardid) REFERENCES campuscard(campuscardid),
    CONSTRAINT fk_charger_bankcard FOREIGN KEY(bankcardid) REFERENCES bankcard(bankcardid)
);

-- 向充值记录表插入数据
INSERT INTO charger VALUES ('20200001', '0001', 100, '2022-12-03');
INSERT INTO charger VALUES ('20200006', '0006', 200, '2022-12-04');
INSERT INTO charger VALUES ('20200001', '0001', 200, '2022-12-03');
INSERT INTO charger VALUES ('20200006', '0006', 200, '2022-12-04');
INSERT INTO charger VALUES ('20200001', '0001', 100, '2022-12-03');

drop view if exists consum_sum;
-- 创建消费总额视图consum_sum
create view consum_sum(campuscardid, studentid, sname, sclass, consum_sum)
as 
select consumer.campuscardid, studentid, sname, sclass, sum(consum_money)
from campuscard, consumer
where consumer.campuscardid = campuscard.campuscardid
group by studentid;

drop view if exists charge_sum;
-- 创建充值总额视图charge_sum
create view charge_sum(campuscardid, studentid, sname, sclass, charge_sum)
as 
select charger.campuscardid, studentid, sname, sclass, sum(charge_money)
from campuscard, charger
where charger.campuscardid = campuscard.campuscardid
group by studentid;

drop trigger if exists consumer_campuscard;
-- 创建触发器consumer_campuscard用于消费后更新校园卡余额 
create trigger consumer_campuscard
after insert on consumer
for each row
update campuscard
set balance = balance - new.consum_money
where new.campuscardid = campuscard.campuscardid;

-- select *from campuscard;
-- select *from bankcard;
-- select *from bankcard;

drop trigger if exists charger_campuscard;
-- 创建触发器charger_campuscard用于消费后更新校园卡余额 
create trigger charger_campuscard
after insert on charger
for each row
update campuscard
set balance = balance + new.charge_money
where new.campuscardid = campuscard.campuscardid;


drop trigger if exists charger_bankcard;
-- 创建触发器charger_campuscard用于消费后更新校园卡余额 
create trigger charger_bankcard
after insert on charger
for each row
update bankcard
set balance = balance - new.charge_money
where new.bankcardid = bankcard.bankcardid;

