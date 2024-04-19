from pydantic import BaseModel, ConfigDict, AliasGenerator, Field
from pydantic.alias_generators import to_camel, to_snake
from typing import Iterable, Any, Optional
from model import Esportista


class EsportistaSchema(BaseModel):
    """Define como um novo esportista deve ser representado
    """
    nome_completo: str = "João Pedro Xavier Freitas"
    idade: int = 26
    altura: Optional[float] = Field(default=None, description="Valor tipo float opcional")
    peso: Optional[float] = Field(default=None, description="Valor tipo float opcional")
    
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_snake,
        )
    )


class EsportistaViewSchema(BaseModel):
    """Define como um novo esportista deve ser visualizado
    """
    nome_completo: str
    idade: int
    altura: Optional[float] = Field(default=None)
    peso: Optional[float] = Field(default=None)

    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
        json_schema_extra={
            "example": {
                "nomeCompleto": "João Pedro Xavier Freitas",
                "idade": 26,
                "altura": 1.80,
                "peso": 75.0
            }
        }
    )


def apresenta_esportista(
    esportista_orm: Esportista
) -> dict[str, Any]:
    esportista_view_schema = EsportistaViewSchema.model_validate(obj=esportista_orm)
    esportista_json = esportista_view_schema.model_dump(by_alias=True)
    return esportista_json


class ListagemEsportistasSchema(BaseModel):
    """Define como uma listagem de esportistas será retornada
    para o cliente.
    """
    esportistas: Iterable[EsportistaSchema]


def apresenta_esportistas(
    esportistas_orm: Iterable[Esportista]
) -> Iterable[str]:
    lista_de_esportistas_json = []
    for esportista_orm in esportistas_orm:
        esportista_view_schema = EsportistaViewSchema.model_validate(
            obj=esportista_orm
        )
        lista_de_esportistas_json.append(
            esportista_view_schema.model_dump(by_alias=True)
        )
    return {"esportistas": lista_de_esportistas_json}


class EsportistaBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca
    que será feita apenas com base no nome do esportista.
    """
    nome: str = "João Pedro Xavier Freitas"


class EsportistaDeletadoSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado 
    após uma requisição de remoção de um esportista.
    """
    message: str
    nome: str = "João Pedro Xavier Freitas"


        


