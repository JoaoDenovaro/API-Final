import uvicorn
from fastapi import FastAPI, APIRouter
from locacao.controladores.controlador_base import ControladorBase
from locacao.controladores.controlador_locadora import ControladorLocadora
# from locacao.controladores.controlador_pessoas import ControladorPessoas
# from locacao.controladores.controlador_veiculo import ControladorVeiculo
from locacao.controladores.controlador_autenticacao import ControladorAutenticacao

VERSAO_API = '/v1'

def vincular_controlador(app: FastAPI, controlador: ControladorBase):
    roteador = APIRouter(prefix=VERSAO_API)
    for endpoint in controlador.endpoints:
        roteador.add_api_route(endpoint=endpoint, **endpoint.rota)
    app.include_router(roteador) 

app = FastAPI()

control_locadora = ControladorLocadora()
control_autenticacao = ControladorAutenticacao()

vincular_controlador(app, control_locadora)
vincular_controlador(app, control_autenticacao)

if __name__ == '__main__':
    uvicorn.run('api:app', port=8000, host='0.0.0.0', reload=True)