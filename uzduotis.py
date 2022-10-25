
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
    uzsakymai = relationship("Uzsakymas", back_populates = "klientas")

    def __repr__(self):
        return f"({self.id},{self.vardas},{self.pavarde},{self.tel_nr},{self.adresas})"

class Uzsakymas(Base):
    __tablename__ = "uzsakymas"
    id = Column(Integer, primary_key=True)
    uzsakymo_data = Column("Data", DateTime, default=datetime.datetime.utcnow)
    suma = Column("suma", Float)
    pristatymo_adresas = Column("adresas", String)

    statusas_id = Column("statusas_id", Integer, ForeignKey("statusas.id"))
    statusas = relationship("UzsakymoStatusas", back_populates="uzsakymai")

    klientas_id = Column("klientas_id", Integer, ForeignKey("klientas.id"))
    klientas = relationship("Klientas", back_populates="uzsakymai")

    uzsakymo_eilutes = relationship("UzsakymoEilute", back_populates = "uzsakymas")

    def __repr__(self):
        return f"({self.id}, {self.uzsakymo_data}, {self.suma}, {self.pristatymo_adresas})"

class UzsakymoStatusas(Base):
    __tablename__ = "statusas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    uzsakymai = relationship("Uzsakymas", back_populates = "statusas")


    def __repr__(self):
        return f"({self.id},{self.pavadinimas})"

class UzsakymoEilute(Base):
    __tablename__ = "uzsakymo_eilute"
    id = Column(Integer, primary_key=True)
    kiekis = Column("kiekis", Integer)
    suma = Column("suma", Float)
    uzsakymas_id = Column("uzsakymas_id", Integer, ForeignKey("uzsakymas.id"))
    uzsakymas = relationship("Uzsakymas", back_populates="uzsakymo_eilutes")

    gaminys_id = Column("gaminys_id", Integer, ForeignKey("uzsakymas.id"))
    gaminys = relationship("Gaminys", back_populates = "uzsakymo_eilutes")

    def __repr__(self):
        return f"({self.id}, {self.kiekis}, {self.suma})"

class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    _1_vnt_kaina = Column("1 vnt kaina", Float)
    _1_vnt_svoris = Column("1 vnt svoris", Float)
    uzsakymo_eilutes = relationship("UzsakymoEilute", back_populates = "gaminys")
    
    def __repr__(self):
        return f"({self.id}, )"

if __name__ == "__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)