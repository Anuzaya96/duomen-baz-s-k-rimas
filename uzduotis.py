
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

    def __repr__(self):
        return f"({self.id},{self.vardas},{self.pavarde},{self.tel_nr},{self.adresas})"

class Uzsakymas(Base):
    __tablename__ = "uzsakymas"
    id = Column(Integer, primary_key=True)
    uzsakymo_data = Column("Data", DateTime, default=datetime.datetime.utcnow)
    suma = Column("suma", Float)
    pristatymo_adresas = Column("adresas", String)

    sastusas_id = Column("statusas_id", Integer, ForeignKey("uzsakymo statusas.id"))
    statusas = relationship("Uzsakymo_statusas", back_populates="uzsakymo statusas")

    klientas_id = Column("klientas_id", Integer, ForeignKey("klientas.id"))
    klientas = relationship("Klientas", Integer, back_populates="klientas")


    def __repr__(self):
        return f"({self.id}, {self.uzsakymo_data}, {self.suma}, {self.pristatymo_adresas})"

class Uzsakymo_statusas(Base):
    __tablename__ = "uzsakymo statusas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)

    def __repr__(self):
        return f"({self.id},{self.pavadinimas})"

class Uzsakymo_eilute(Base):
    __tablename__ = "uzsakymo eilute"
    id = Column(Integer, primary_key=True)
    kiekis = Column("kiekis", Integer)
    suma = Column("suma", Float)
    uzsakymas_id = Column("uzsakymas_id", Integer, ForeignKey("uzsakymas.id"))
    uzsakymas = relationship("Uzsakymas", Integer, back_populates="uzsakymas")

    gaminys_id = Column("gaminys_id", Integer, ForeignKey("uzsakymas.id"))
    gaminys = relationship("Gaminys", Integer, back_populates = ("gaminys"))

    def __repr__(self):
        return f"({self.id}, {self.kiekis}, {self.suma})"

class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    _1_vnt_kaina = Column("1 vnt kaina", Float)
    _1_vnt_svoris = Column("1 vnt svoris", Float)
    
    def __repr__(self):
        return f"({self.id}, )"

if __name__ == "__main__":
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)