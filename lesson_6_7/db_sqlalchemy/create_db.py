from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_path = 'lesson6.sqlite'
engine = create_engine(f'sqlite:///{db_path}')
Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'
    name = Column(String, primary_key=True)
    description = Column(String, nullable=False)


class Unit(Base):
    __tablename__ = 'units'
    unit = Column(String, primary_key=True)


class Position(Base):
    __tablename__ = 'positions'
    position = Column(String, primary_key=True)


class Good(Base):
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(String, ForeignKey('units.unit'))
    cat = Column(String, ForeignKey('categories.name'))


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    fio = Column(String)
    position = Column(String, ForeignKey('positions.position'))


class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ownerchipform = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)


# Подготовка схемы - удаление всех записей из всех таблиц
def prepare_db(tables_list):
    for table in tables_list:
        engine.execute(table.delete())


# Проверка таблиц
def test_db(tables_list, session_):
    prepare_db(tables_list)
    cat = Category(name='cat_test', description='cat_test')
    unit = Unit(unit='unit_test')
    pos = Position(position='position_test')
    good = Good(name='good_test', unit=unit.unit, cat=cat.name)
    emp = Employee(position=pos.position)
    vendor = Vendor(name='vendor_test')
    objects = [cat, unit, pos, good, emp, vendor]
    session_.bulk_save_objects(objects)
    session_.commit()
    test_fetch(tables_list, session_)


# Проверка, что записи появились
def test_fetch(tables_list, session_):
    for table in tables_list:
        q = session_.query(table).all()
        assert len(q) == 1, f'{table.name} number of record is wrong!'
    print('DB tested successfully!')


Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()

tables = [table[1] for table in Base.metadata.tables.items()]

test_db(tables, session)
