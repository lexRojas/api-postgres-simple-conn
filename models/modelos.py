from config.db  import  *
from datetime import datetime

from sqlalchemy import String,DateTime,Float,Integer,Boolean
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