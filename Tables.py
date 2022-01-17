import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', password='root', database='Hospital')
c1 = conn.cursor()
c1.execute("create table patient_details(p_name varchar(30),p_age int,p_problems varchar(20),p_phono int)")
c1.execute("create table doctor_details(d_name varchar(30),d_age int,d_department varchar(20),d_phono int)")
c1.execute("create table worker_details(w_name varchar(30),w_age int,w_workname varchar(20),w_phono int)")