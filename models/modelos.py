from config.db  import  *
from datetime import datetime

from sqlalchemy import String,DateTime,Float,Integer,Boolean,ForeignKey
from typing import Optional,Dict
from sqlalchemy.orm import Mapped, mapped_column




class tb_presupuesto(Base):
    __tablename__ = 'tb_presupuesto'
    presupuesto         : Mapped[str]       = mapped_column(String(7),  primary_key=True)
    proyecto            : Mapped[str]       = mapped_column(String(),nullable=False)
    propietario         : Mapped[str]       = mapped_column(String(40))
    fecha_apertura      : Mapped[datetime]  = mapped_column(DateTime(), default= datetime.now)
    hora_apertura       : Mapped[str]       = mapped_column(String)
    area_construccion   : Mapped[float]     = mapped_column(Float)
    fecha_cambio        : Mapped[datetime]  = mapped_column(DateTime(), default= datetime.now)
    cod_usuario         : Mapped[Optional[str]]       = mapped_column(String(15))
    tipo_licitacion     : Mapped[int]       = mapped_column(Integer)
    responsable         : Mapped[int]       = mapped_column(Integer)
    num_licitacion      : Mapped[str]       = mapped_column(String)
    activo              : Mapped[Optional[bool]]      = mapped_column(Boolean)

    def __str__(self):
        return self.presupuesto


class tb_elementos_sectores(Base):
    __tablename__  = 'tb_elementos_sectores'
    presupuesto         : Mapped[str]       = mapped_column(ForeignKey("tb_presup_manobra.presupuesto"), primary_key=True)
    elemento            : Mapped[int]       = mapped_column(Integer, nullable=True)
    sector              : Mapped[Optional[str]]       = mapped_column(String(1))
    descripcion         : Mapped[Optional[str]]       = mapped_column(String(50))
    comentario          : Mapped[Optional[str]]       = mapped_column(String)
    cantidad_elemento   : Mapped[int]       = mapped_column(Integer, nullable=True)
    cod_ele_sec         : Mapped[str]       = mapped_column(ForeignKey("tb_presup_manobra.cod_ele_sec"), primary_key=True)
    fecha_cambio        : Mapped[datetime]  = mapped_column(DateTime(), default= datetime.now)
    cod_usuario         : Mapped[Optional[str]]       = mapped_column(String(15))
    unidad_medida       : Mapped[int]       = mapped_column(ForeignKey("tb_unidad_medida.cod_unidad_medida"), primary_key=True)
    consecutivo         : Mapped[int]       = mapped_column(Integer, nullable=True)

    def __str__(self):
        return self.presupuesto+ '-'+ self.cod_ele_sec

class tb_unidad_medida(Base):
    __tablename__  = 'tb_unidad_medida'
    cod_unidad_medida   : Mapped[int]                 = mapped_column(Integer,  primary_key=True, autoincrement=True)
    descripcion         : Mapped[Optional[str]]       = mapped_column(String(30))
    fecha_cambio        : Mapped[datetime]            = mapped_column(DateTime(), default= datetime.now)
    cod_usuario         : Mapped[Optional[str]]       = mapped_column(String(15))
    descrip_larga       : Mapped[Optional[str]]       = mapped_column(String(30))

    def __str__(self):
        return self.cod_unidad_medida+ '-'+ self.descrip_larga


class tb_presup_manobra(Base):
    __tablename__  = 'tb_presup_manobra'

    presupuesto     : Mapped[str]       = mapped_column(String(7),  primary_key=True)
    codigo_manobra  : Mapped[int]       = mapped_column(ForeignKey("tb_manoobra.codigo_manobra"))
    cantidad        : Mapped[float]       = mapped_column(Float, nullable=True)
    rendimiento     : Mapped[float]       = mapped_column(Float, nullable=True)
    cant_hht        : Mapped[float]       = mapped_column(Float, nullable=True)
    costo_hh        : Mapped[float]       = mapped_column(Float, nullable=True)
    costo_hht       : Mapped[float]       = mapped_column(Float, nullable=True)
    fecha_cambio    : Mapped[datetime]            = mapped_column(DateTime(), default= datetime.now)
    cod_usuario     : Mapped[Optional[str]]       = mapped_column(String(15))
    unidad_medida   : Mapped[int]       = mapped_column(ForeignKey("tb_unidad_medida.cod_unidad_medida"))
    cod_ele_sec     : Mapped[str]       = mapped_column(String(8),  primary_key=True)

    def __str__(self):
        return self.presupuesto+ '-'+ self.codigo_manobra + '-' + self.cod_ele_sec


class tb_manoobra(Base):
    __tablename__= "tb_manoobra"
   
    codigo_manobra  : Mapped[int]       = mapped_column(Integer,  primary_key=True)
    actividad       : Mapped[Optional[str]]       = mapped_column(String(30))
    rendimiento     : Mapped[float]       = mapped_column(Float, nullable=True)
    puesto          : Mapped[str]       = mapped_column(String(3),  nullable=True)
    cod_usuario     : Mapped[str]       = mapped_column(String(15),  nullable=True)
    fecha_cambio    : Mapped[datetime]            = mapped_column(DateTime(), default= datetime.now)
    unidad_medida   : Mapped[int]       = mapped_column(ForeignKey("tb_unidad_medida.cod_unidad_medida"))
    
    def __str__(self):
        return self.codigo_manobra 
