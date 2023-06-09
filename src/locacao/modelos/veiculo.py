import sqlalchemy as sa
import sqlalchemy.orm as orm
from locacao.modelos.modelo_base import ModeloBase

class Veiculo(ModeloBase):
    __tablename__ = "veiculo"

    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(36), primary_key=True)
    uuid_condutor: orm.Mapped[str] = orm.mapped_column(sa.ForeignKey("pessoa.uuid"))
    placa: orm.Mapped[str] = orm.mapped_column(sa.String(7), unique=True)
    modelo: orm.Mapped[str] = orm.mapped_column(sa.String(30))
    tipo: orm.Mapped[str] = orm.mapped_column(sa.String(30))
    combustivel: orm.Mapped[str] = orm.mapped_column(sa.String(30))
    capacidade: orm.Mapped[int] = orm.mapped_column(sa.Integer)
    cor: orm.Mapped[str] = orm.mapped_column(sa.String(30))

    # pessoa: orm.Mapped["Pessoa"] = orm.relationship(back_populates="veiculos")

    def __init__(self, uuid: str, uuid_condutor: str, placa: str, 
            modelo: str, tipo: str, combustivel: str, capacidade: int, 
            cor: str):
        super().__init__()
        self.uuid = uuid
        self.uuid_condutor = uuid_condutor
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo
        self.combustivel = combustivel
        self.capacidade = capacidade
        self.cor = cor

    def __repr__(self) -> str:
        return (f"Veiculo(uuid={self.uuid}, uuid_condutor={self.uuid_condutor}, " + 
                f"placa={self.placa}, modelo={self.modelo}, tipo={self.tipo}, " + 
                f"combustivel={self.combustivel}, capacidade={self.capacidade}, " + 
                f"cor={self.cor})")