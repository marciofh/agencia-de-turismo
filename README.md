# Agência de turismo
Esse projeto tem como objetivo acelerar o processo de elaboração de pacotes turísticos
tirando todos os serviços manuais, recursos humanos e longos períodos de consultas a hotéis
e empresas aéreas.

Para solucionar essa demanda, foi desenvolvido um Crawler capaz de
pesquisar e extrair dados do site de uma das principais linhas aéreas brasileiras, a Gol Linhas Aéreas.
Foi implementado também uma API para puxar preços de hotéis com intuito de explorar
outras soluções para a problemática.

O sistema primeiro irá consultar se os
os inputs digitados pelo usuário batem com algum dado no Banco. Caso tenha, essa
consulta irá economizar requisições pois não será necessário chamar a API e o Crawler para
fazer a busca. Caso não tenha, logo após a resposta dos serviços, o sistema
fará o cadastro para que caso ocorra uma nova pesquisa para o mesmo lugar, na mesma data,
não seja necessário fazer mais requisições.

# CRAWER
O framework utilizado foi Selenium desenvolvido em Python e pode
rodar em qualquer navegador. É necessário escolher qual browser deseja usar e importar o webdriver do Selenium.

# API
A api é um serviço desenvolvido pela Dojo Net, ela busca
no TripAdivisor todos os hotéis da cidade e retorna vários dados como nome, preço,
endereço, fotos, avaliações. A api é gratuita, porém possui um limite de 500 requisições por
mês e 5 requisições a cada segundo.É necessário um token que pode ser adquirido no site
https://rapidapi.com/apidojo/api/travel-advisor.

# Observações
Deve-se levar em consideração as desvantagens de cada serviço, seja na
demora significativa do Crawler e as inúmeras vezes que ocorreu bugs, ou a restrição que a api
nos impõem. 
