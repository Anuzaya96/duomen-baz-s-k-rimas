
import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/uzsakymas.db')
Base = declarative_base()

class Klientas(Base):
    __tablename__ = "klientas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    tel_nr = Column("telefono numeris", String)
    adresas = Column("adresas", String)

class Uzsakymas(Base):
    __tablename__ = "uzsakymas"
    id = Column(Integer, primary_key=True)
    uzsakymo_data = Column("Data", DateTime, default=datetime.datetime.utcnow)
    suma = Column("suma", Float)
    pristatymo_adresas = Column("adresas", String)
    sastusas_id = Column("satusas_id", Integer, ForeignKey("statusas.id"))
    statusas = relationship("Uzsakymo_statusas", back_populates='Uzsakymas')

    klientas_id = 
    kilientas

class Uzsakymo_statusas(Base):
    __tablename__ = "uzsakymo statusas"
    id = Column(Integer, primary_key=True)
    pavadinimas = ("pavadinimas", String)


class Uzsakymo_eilute(Base):
    __tablename__ = "uzsakymo eilute"
    id = Column(Integer, primary_key=True)
    kiekis = Column("kiekis", Integer)
    suma = Column("suma", Float)
    uzsakymas_id = 
    gaminys_id = Column()

class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    pavadinimas = ("pavadinimas", String)
    _1_vnt_kaina = ("1 vnt kaina", Float)
    _1_vnt_svoris = ("1 vnt svoris", Float)


if __name__ == "__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)`