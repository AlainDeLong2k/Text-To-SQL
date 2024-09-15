import sqlite3

# Connect to sqlite
connection = sqlite3.connect("database/student.db")

# Create a cursor object to create table, insert record and retrieve
cursor = connection.cursor()

# Create the table
table_info = """ create table if not exists STUDENT (
    ID_STU          integer primary key not null,
    NAME_STU        nvarchar(30),
    BIRTHDAY_STU    date,
    BIRTHPLACE_STU  nvarchar(100))"""
cursor.execute(table_info)

table_info = """ create table if not exists LECTURER (
    ID_LEC          integer primary key not null,
    NAME_LEC        nvarchar(30),
    BIRTHDAY_LEC    date,
    BIRTHPLACE_LEC  nvarchar(100))"""
cursor.execute(table_info)

table_info = """create table if not exists COURSE (
    ID_COU      integer primary key not null,
    NAME_COU    nvarchar(100),
    ID_LEC      integer,
    foreign key (ID_LEC) references LECTURER(ID_LEC))"""
cursor.execute(table_info)

table_info = """create table if not exists REGISTRATION_FORM (
    ID_REG integer primary key not null,
    ID_COU integer,
    ID_STU integer,
    foreign key (ID_COU) references COURSE(ID_COU),
    foreign key (ID_STU) references STUDENT(ID_STU))"""
cursor.execute(table_info)


# Insert some records
connection.execute("PRAGMA foreign_keys = ON")

cursor.execute(
    """insert into STUDENT values (1, 'Đặng Tuấn Anh','1999-08-08', 'Hải Phòng');"""
)
cursor.execute(
    """insert into STUDENT values (2, 'Hoàng Đức Anh','1999-08-09', 'Hà Nội');"""
)
cursor.execute(
    """insert into STUDENT values (3, 'Lưu Trang Anh','1999-08-10', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into STUDENT values (4, 'Phạm Hoàng Anh','2000-08-11', 'Nam Định');"""
)
cursor.execute(
    """insert into STUDENT values (5, 'Phạm Thị Hiền Anh','2000-07-12', 'Hưng Yên');"""
)
cursor.execute(
    """insert into STUDENT values (6, 'Phạm Khắc Việt Anh','2000-07-13', 'Hải Phòng');"""
)
cursor.execute(
    """insert into STUDENT values (7, 'Đỗ Hoàng Gia Bảo','2000-07-14', 'Hà Nội');"""
)
cursor.execute(
    """insert into STUDENT values (8, 'Trần Thị Minh Châu','1998-07-15', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into STUDENT values (9, 'Tăng Phương Chi','1998-09-16', 'Nam Định');"""
)
cursor.execute(
    """insert into STUDENT values (10, 'Gan Feng Du','1998-09-17', 'Hưng Yên');"""
)
cursor.execute(
    """insert into STUDENT values (11, 'Phạm Tiến Dũng','1998-09-19', 'Hải Phòng');"""
)
cursor.execute(
    """insert into STUDENT values (12, 'Nguyễn Thái Dương','1997-09-19', 'Hà Nội');"""
)
cursor.execute(
    """insert into STUDENT values (13, 'Trần An Dương','1997-05-20', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into STUDENT values (14, 'Mạc Trung Đức','1997-05-21', 'Nam Định');"""
)
cursor.execute(
    """insert into STUDENT values (15, 'Vũ Hương Giang','1997-05-22', 'Hưng Yên');"""
)
cursor.execute(
    """insert into STUDENT values (16, 'Nguyễn Thị Ngân Hà','1997-01-23', 'Hải Phòng');"""
)
cursor.execute(
    """insert into STUDENT values (17, 'Nguyễn Lê Hiếu','1996-01-24', 'Hà Nội');"""
)
cursor.execute(
    """insert into STUDENT values (18, 'Phạm Xuân Hòa','1996-01-25', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into STUDENT values (19, 'Khoa Minh Hoàng','1996-01-26', 'Nam Định');"""
)
cursor.execute(
    """insert into STUDENT values (20, 'Nguyễn Hữu Hiệp Hoàng','1996-01-27', 'Hưng Yên');"""
)
cursor.execute(
    """insert into STUDENT values (21, 'Nguyễn Văn A', '2000-09-25', 'Hải Phòng')"""
)
cursor.execute("""insert into STUDENT (ID_STU, BIRTHPLACE_STU) values (22, 'Hà Nội')""")

cursor.execute(
    """insert into LECTURER values (1, 'Đặng Quốc Việt','1987-7-01', 'Hải Phòng');"""
)
cursor.execute(
    """insert into LECTURER values (2, 'Hoàng Văn Bảo','1987-7-02', 'Hà Nội');"""
)
cursor.execute(
    """insert into LECTURER values (3, 'Lưu Thanh Tuấn','1987-7-03', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into LECTURER values (4, 'Hoàng Thị Thanh Mai','1987-7-04', 'Nam Định');"""
)
cursor.execute(
    """insert into LECTURER values (5, 'Nguyễn Quỳnh Hoa','1987-7-05', 'Hưng Yên');"""
)
cursor.execute(
    """insert into LECTURER values (6, 'Cao Thị Xuân Dung','1992-6-06', 'Hải Phòng');"""
)
cursor.execute(
    """insert into LECTURER values (7, 'Đỗ Hồng Việt','1992-6-07', 'Hà Nội');"""
)
cursor.execute(
    """insert into LECTURER values (8, 'Phạm Thị Thu Hương','1992-6-08', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into LECTURER values (9, 'Bùi Thị Vân Thiện','1992-6-6', 'Nam Định');"""
)
cursor.execute(
    """insert into LECTURER values (10, 'Nguyễn Thị Thu Hiền','1990-5-10', 'Hưng Yên');"""
)
cursor.execute(
    """insert into LECTURER values (11, 'Nguyễn Thị Trà My','1990-5-11', 'Hải Phòng');"""
)
cursor.execute(
    """insert into LECTURER values (12, 'Trần Thị Thúy','1990-5-12', 'Hà Nội');"""
)
cursor.execute(
    """insert into LECTURER values (13, 'Trần Trọng Dũng','1990-5-13', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into LECTURER values (14, 'Mạc Văn Việt','1990-1-14', 'Nam Định');"""
)
cursor.execute(
    """insert into LECTURER values (15, 'Bùi Thị Thu Hương','1993-1-15', 'Hưng Yên');"""
)
cursor.execute(
    """insert into LECTURER values (16, 'Nguyễn Văn Đạm','1993-1-16', 'Hải Phòng');"""
)
cursor.execute(
    """insert into LECTURER values (17, 'Lê Thị Hợi','1993-1-17', 'Hà Nội');"""
)
cursor.execute(
    """insert into LECTURER values (18, 'Phạm Văn Cường','1993-2-18', 'Bắc Ninh');"""
)
cursor.execute(
    """insert into LECTURER values (19, 'Khoa Năng Tùng','1991-2-19', 'Nam Định');"""
)

cursor.execute("""insert into COURSE values (1,'Tester basic',1);""")
cursor.execute("""insert into COURSE values (2,'Tester advance',2);""")
cursor.execute("""insert into COURSE values (3,'Automation test',1);""")
cursor.execute("""insert into COURSE values (4,'API testing',4);""")
cursor.execute("""insert into COURSE values (5,'DB testing',5);""")
cursor.execute("""insert into COURSE values (6,'Performance testing',3);""")
cursor.execute("""insert into COURSE values (7,'GUI testing',7);""")
cursor.execute("""insert into COURSE values (8,'Mobile testing',8);""")
cursor.execute("""insert into COURSE values (9,'Game testing',9);""")

cursor.execute("""insert into REGISTRATION_FORM values (1,1,1);""")
cursor.execute("""insert into REGISTRATION_FORM values (2,2,2);""")
cursor.execute("""insert into REGISTRATION_FORM values (3,3,3);""")
cursor.execute("""insert into REGISTRATION_FORM values (4,4,4);""")
cursor.execute("""insert into REGISTRATION_FORM values (5,5,5);""")
cursor.execute("""insert into REGISTRATION_FORM values (6,6,6);""")
cursor.execute("""insert into REGISTRATION_FORM values (7,7,7);""")
cursor.execute("""insert into REGISTRATION_FORM values (8,8,8);""")
cursor.execute("""insert into REGISTRATION_FORM values (9,9,9);""")
cursor.execute("""insert into REGISTRATION_FORM values (10,1,10);""")
cursor.execute("""insert into REGISTRATION_FORM values (11,2,11);""")
cursor.execute("""insert into REGISTRATION_FORM values (12,3,12);""")
cursor.execute("""insert into REGISTRATION_FORM values (13,4,13);""")
cursor.execute("""insert into REGISTRATION_FORM values (14,5,14);""")
cursor.execute("""insert into REGISTRATION_FORM values (15,6,15);""")
cursor.execute("""insert into REGISTRATION_FORM values (16,7,16);""")
cursor.execute("""insert into REGISTRATION_FORM values (17,8,17);""")
cursor.execute("""insert into REGISTRATION_FORM values (18,9,18);""")
cursor.execute("""insert into REGISTRATION_FORM values (19,1,19);""")
cursor.execute("""insert into REGISTRATION_FORM values (20,2,20);""")
cursor.execute("""insert into REGISTRATION_FORM values (21,3,1);""")
cursor.execute("""insert into REGISTRATION_FORM values (22,4,2);""")
cursor.execute("""insert into REGISTRATION_FORM values (23,5,3);""")
cursor.execute("""insert into REGISTRATION_FORM values (24,6,4);""")
cursor.execute("""insert into REGISTRATION_FORM values (25,7,5);""")
cursor.execute("""insert into REGISTRATION_FORM values (26,8,6);""")
cursor.execute("""insert into REGISTRATION_FORM values (27,9,7);""")
cursor.execute("""insert into REGISTRATION_FORM values (28,1,8);""")
cursor.execute("""insert into REGISTRATION_FORM values (29,2,9);""")
cursor.execute("""insert into REGISTRATION_FORM values (30,3,10);""")


# Close the connection
connection.commit()
connection.close()
