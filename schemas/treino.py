from pydantic import BaseModel, ConfigDict, AliasGenerator, field_serializer, field_validator
from pydantic.alias_generators import to_camel, to_snake
from datetime import time, date, datetime
from typing import Iterable, Optional, Any
from model import Treino


class TreinoSchema(BaseModel):
    """Define como um novo treino deve ser representado
    """ 
    nome_esportista: str = "João Pedro Xavier Freitas"
    data_treino: date = date(2024, 4, 14)
    esporte: str = "Corrida"
    duracao: Optional[time] = None
    calorias: Optional[int] = None
    bpm: Optional[int] = None

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_snake,
        )
    )
    

class TreinoViewSchema(BaseModel):
    """Define como um novo treino deve ser visualizado
    """ 
    nome_esportista: str = "João Pedro Xavier Freitas"
    data_treino: date = date(2024, 4, 14)
    esporte: str = "Corrida"
    duracao: Optional[time] = None
    calorias: Optional[int] = None
    bpm: Optional[int] = None

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        )
    )

    @field_serializer("data_treino")
    def _transformar_tipo_date_em_string(self, v: date):
        return v.strftime("%d/%m/%Y") if v else v

    @field_serializer("duracao")
    def _transformar_tipo_time_em_string(self, v: time):
        return v.strftime("%H:%M:%S") if v else v


def apresenta_treino(
    treino_orm: Treino
) -> dict[str, Any]:
    treino_view_schema = TreinoViewSchema.model_validate(obj=treino_orm)
    treino_json = treino_view_schema.model_dump(by_alias=True)
    return treino_json


class ListagemTreinosSchema(BaseModel):
    """Define como uma listagem de treinos será retornada
    para o cliente.
    """
    treinos: Iterable[TreinoSchema]


def apresenta_treinos(
    treinos_orm: Iterable[Treino]
) -> dict[str, Any]:
    lista_de_treinos_json = []
    for treino_orm in treinos_orm:
        treino_view_schema = TreinoViewSchema.model_validate(
            obj=treino_orm
        )
        lista_de_treinos_json.append(
            treino_view_schema.model_dump(by_alias=True)
        )
    return {"treinos": lista_de_treinos_json}


class TreinoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a 
    busca de um treino que será feita baseada na chave 
    primária, composta pelo nome, data e modalidade do treino.
    """
    nome: str = "João Pedro Xavier Freitas"
    data: str = "14/04/2024"
    esporte: str = "Natação"

    @field_validator("data")
    @classmethod
    def _ajuste_no_padrao_do_campo_data(cls, v: str):
        """O campo data de um treino é fornecido na rota de
        delete como uma string no padrão do calendário brasileiro.
        No entanto, é necessário com que essa string seja apresentada
        na query pelo formato ISO de data.
        """
        date_modelo_ISO = datetime.strptime(v, "%d/%m/%Y")
        return date_modelo_ISO.strftime("%Y-%m-%d")

            
class TreinoDeletadoSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado 
    após uma requisição de remoção de um treino.
    """
    message: str
    nome: str = "João Pedro Xavier Freitas"
