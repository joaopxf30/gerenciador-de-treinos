# Back-end do projeto de controlador de treinos 

Este pequeno projeto, intitulado controlador de treinos, compõe o MVP desenvolvido para a sprint de **Desenvolvimento Full Stack Básico** do curso de pós-graduação em Desenvolvimento Full Stack. O controlador de treinos é uma aplicação web responsável por cadastrar esportistas e registrar treinos vinculados a cada esportista. O presente documento ressalta aspectos do desenvolvimento voltados ao back-end.


---
## Ambiente de Desenvolvimento

### Ambientes virtuais

É fortemente recomendado a utilização de ambientes virtuais. Para tal, execute no terminal a partir de um <path> desejado o seguinte comando de acordo com o sistema operacional:

**WINDOWS**:
```
python -m venv env
```

**OS/LINUX**:
```
python3 -m venv env
```

Para ativação do ambiente virutal, execute o seguinte comando de acordo com a platafoma:

**WINDOWS**:
```
<path>\env\Scripts\Activate.ps1
```

**POSIX**:
```
source <path>/env/bin/activate
```

O ambiente virtual será cirado.

### Instalando dependências

Todas as dependências do projeto se encontram no arquivo `requirements.txt`. A obtenção é feita da execução do seguinte comando a partir da raiz `meu_app_api`.

```
pip install -r requirements.txt
```

As dependências são instaladas.
