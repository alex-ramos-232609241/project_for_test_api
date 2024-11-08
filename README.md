# README

## CONTENTS OF THIS FILE
   
* Introduction
* Requirements
* Recommended
* Configuration

## INTRODUCTION

Este proyecto nos permite realizar TEST AUTOMATIZADOS(revisar archivo OrganizationBooker/test/)
 basados en BDD,
se realizo la automatizacion para poder realizar los test de la API
restfull-booker.

* SE UTILIZO EL PATRON DE DISEÑO Factory para crear las peticiones
* SE Utilizo el patron singleton para generar una instancia, almacenar 
  y actualizar el token.

* Para este proyecto se utilizaron las tecnologias como:

  BEHAVE

  "Behave es un marco BDD de código abierto basado en Python para escribir pruebas en un estilo de  lenguaje natural."
  
    https://behave.readthedocs.io/en/latest/api/

  Django , python , allure (para poder observar los reportes ) , selenium 

## RECOMMENDED

* para correr el proyecto 
  - pip install -r requirements
  - cd ApiTestWeb
  - behave