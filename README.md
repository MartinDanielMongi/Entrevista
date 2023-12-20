# Entrevista tecnica

## Descripción

Este repositorio esta preparado para la resolucion de la entrevista tecnica propuesta por ___ para un puesto como Software Support Engineer.
Se puede encontrar las condiciones de la entrevista en "Consigna.docx" (nota 1)

## Instalación

Clone el repositorio: 

    git clone https://github.com/MartinDanielMongi/Entrevista.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    venv/Scripts/Activate

Instale las dependencias:

    pip install -r requirements.txt

## Uso

Para correr el programa corra:

    uvicorn main:app

o

    make run

y luego realice la siguiente request:

    curl --location 'http://127.0.0.1:8000/fight' \
    --header 'Content-Type: application/json' \
    --data '{"player1":{"movimientos":["D","DSD","S","DSD", "SD"],"golpes":["K","P","","K","P"]},"player2":  {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K",    "","K","P","P"]}} '


respuesta esperada:

    [
        Tonyn Stallone da una patada
        Arnaldor Shuatseneguer conecta un Remuyuken
        Tonyn Stallone usa un Taladoken
        Arnaldor Shuatseneguer se mueve
        Tonyn Stallone se mueve
        Arnaldor Shuatseneguer conecta un Remuyuken
        Arnaldor Shuatseneguer gana la batalla, y aun le queda 2 de vida

    ]




## Tests

Para correr los tests de esta aplicacion se recomienda usar el siguiente comando 

    pytest --cov=src --cov-config=.coveragerc --cov-report=html


puede abrir el archivo **htmlcov/index.html** para ver el coverage generado de los tests

## Cómo contribuir

Si bien este proyecto solo implica los conocimientos al momento de hacer esta entrevista creo que siempre puede ser bueno saber como se puede mejorar una entrega de este tipo, desde la funcionalidad del codigo, los tests hasta la documentacion o la presentacion del corriente archivo.

Si alguien se siente en capacidad de aportar sientase libre de crear una rama nueva y con un PR aportar sus ideas para mejorar esta presentacion

## Notas

- En la documentacion del ejercicio, el primer ejemplo aportado considere que tiene un error en el 3 comando de ataque del player 1, ya que menciona un ataque mientras que en los comandos no aporta ningun ataque

- Si bien hay algunas cosas que se podrian implementar no se hizo debido al alcance del ejercicio como Github Actions para realizar un Coverage Badge