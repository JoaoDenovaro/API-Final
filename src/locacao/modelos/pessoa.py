import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from locacao.modelos.modelo_base import ModeloBase

class Pessoa(ModeloBase):
    __tablename__ = 'pessoa'

    uuid: orm.Mapped[str] = orm.mapped_column(
        sa.String(36), primary_key=True)
    cnh: orm.Mapped[str] = orm.mapped_column(
        sa.String(11), unique=True)
    tipo: orm.Mapped[str] = orm.mapped_column(
        sa.String(30))
    nome: orm.Mapped[str] = orm.mapped_column(
        sa.String(100))
    
    def __repr__(self) -> str:
        return (f'Pessoa(uuid={self.uuid}, cnh={self.cnh}, ' + 
                f'tipo={self.tipo}, nome={self.nome})')