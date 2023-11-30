# 👁 Plurii - Sistema de Agendamento

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)

<img src="https://github.com/anabxalves/anabxalves/assets/108446826/18072226-9184-45db-afb8-f283bd7faaeb"/>

> Unindo experiências para criar soluções Plurais!
---

## 🤖 Cliente
<table>
   <tr>
      <td>
         <img src="https://github.com/anabxalves/abxaSHimp/assets/108446826/727024fd-ecdc-4ed6-b82d-7bd64a853ddb"/>
      </td>
      <td>
         <i> O “Garagem” é um espaço maker equipado com maquinário, ferramentas e componentes eletrônicos destinado ao estudo e criação de artefatos físicos e interativos. Sendo o Garagino um grupo de estudos dentro do garagem. </i>
      </td>
   </tr>
</table>

## 👊 Problemática
<div align="center">
   <h3>
      Como aprimorar a segurança, eficiência e colaboração no uso das salas e equipamentos do Laboratório Garagem?
   </h3>
   <i>
      Dificuldades e incertezas a respeito da centralização de informações e procedimento de solicitação a respeito dos espaços e ferramentas do Laboratório Garagem, o que gera um excesso comunicativo.
   </i>
</div>

## 😎 Solução
<div align="center">
   <br>
   <img src="https://github.com/anabxalves/anabxalves/assets/108446826/18072226-9184-45db-afb8-f283bd7faaeb"/>
</div>
<br>
<div align="center">
   <h3>
      <i>
         Sistema web responsivo de agendamento de horários e visualização de disponibilidade das salas do Laboratório Garagem, sob confirmação de responsável, com canal de comunicação via email.
      </i>
   </h3>
</div>

### Nossas funcionalidades

<table class="table">
   <tr>
      <td align="center">
         <b>
            Visualização da Disponibilidade
         </b>
      </td>
      <td align="center">
         <b>
            Agendamento
         </b>
      </td>
      <td align="center">
         <b>
            Confirmação via Email
         </b>
      </td>
   </tr>
   <tr>
      <td>
         Esta funcionalidade permite aos usuários visualizarem de forma intuitiva a disponibilidade das salas no laboratório garagem. Os usuários poderão facilmente verificar quais horários estão livres e quais estão ocupados, fornecendo uma visão geral das opções disponíveis para agendamento.
      </td>
      <td>
         Permite aos usuários solicitar o agendamento de uma sala, sujeito à aprovação de um responsável. Na solicitação, o usuário deve fornecer um motivo para a reserva da sala. Além disso, o sistema fornecerá informações sobre as características e recursos de cada sala, como equipamentos disponíveis, capacidade de assentos. Isso ajudará os usuários a escolherem a sala apropriada para suas necessidades, garantindo um processo de agendamento eficiente.
      </td>
      <td>
         Esta funcionalidade automatiza a comunicação com os usuários. Após a aprovação do agendamento, o sistema enviará um e-mail de confirmação ao usuário que efetuou a reserva. Além disso, o usuário receberá notificações por e-mail sobre quaisquer atualizações ou alterações em seu agendamento, garantindo que estejam sempre informados.
      </td>
   </tr>
</table>

## 🚀 Linguagem utilizada
- <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />

## ⚙️ Instruções

1. Baixar o [PostgreSQL](https://www.postgresql.org/download/)
2. Inicie o instalador e siga as etapas de instalação. Mantenha as opções padrão, mas na seção de password, defina a **senha como "plurii"**. No final da instalação, quando perguntado se deseja iniciar o Stack Builder, não selecione a caixa.
3. Agora, abra o programa *pgAdmin4*, que foi instalado como parte do PostgreSQL.
4. No pgAdmin4, clique em "Add New Server". Dê um nome ao seu servidor e, na aba "Connection", configure o "Hostname" como "localhost". Use a password como "plurii", como foi definido anteriormente.
5. Depois de adicionar o servidor, abra-o na lista à esquerda. Clique na opção "database" e escolha "Create". Nomeie o banco de dados como "Plurii" (com "P" maiúsculo) e clique em "Save".
6. Clone esse repositório e abra o projeto no vscode:
   
#### No terminal pelo Visual Studio Code:
<dl>
   1.Instale o poetry, esse é o nosso gerenciador de ambiente virtual
   <dt>
      
      pip install poetry  
   </dt>
  
   2. Installar as configurações do projeto:
   <dt>
      
      poetry install
   </dt>
   
   3. Iniciar o sheel do poetry
   <dt>
      
      poetry shell
   </dt>
   
   4.Caso queira que a aplicação comece a rodar:
   <dt>
      
      uvicorn app.main:app
   </dt>
   5. Aplicação sendo executada com sucesso!
</dl>

# 📄 Como foi desenvolvido?
Este projeto foi concebido com a visão de combinar funcionalidade robusta com uma experiência de usuário imersiva. 

**Ideação e Planejamento**
<br>
Inicialmente, realizamos sessões de brainstorming para identificar as funcionalidades chave necessárias em um sistema de reserva. Após definir os requisitos, esboçamos wireframes e criamos um roadmap de desenvolvimento, priorizando as funcionalidades e a experiência do usuário.

**Desenvolvimento Ágil**
<br>
Adotamos uma abordagem ágil para o desenvolvimento, permitindo uma adaptação rápida às mudanças e a entrega contínua de recursos. Iterações regulares e feedback da equipe garantiram que o projeto permanecesse alinhado com nossos objetivos.

**Componentes Reutilizáveis**
<br>
Com foco na modularidade, criamos componentes reutilizáveis que poderiam ser facilmente adaptados e reutilizados em diferentes partes do aplicativo, garantindo consistência e eficiência no desenvolvimento.

🌟 Cada linha de código reflete nosso compromisso com qualidade e atenção aos detalhes, culminando em um sistema de reservas que é tanto robusto quanto intuitivo. 

## 🔗 Google Sites

O Google Site é utilizado como repositório geral das atividades da equipe.

<a href="https://sites.google.com/cesar.school/plurii-projetos3/home">
  <img src="https://img.shields.io/badge/Acessar%20Site%20-Google Sites-%2304D361">
</a>

## 🎨 Layout

O layout completo da aplicação está disponível no Figma:

<a href="https://www.figma.com/proto/TjWS7gPzge1Yv398tRMIGQ/Projetos-3_PlurII?type=design&node-id=728-2196&t=k6GWB3zTk8Ul7R7a-0&scaling=min-zoom&starting-point-node-id=942%3A4551&show-proto-sidebar=1">
  <img src="https://img.shields.io/badge/Acessar%20Layout%20-Figma-%2304D361">
</a>

# 🤝 Integrantes da equipe
<table>
  <tr>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/108764670?v=4" width="100px;"/><br/><sub><b>Adriana Rodrigues</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/108446826?v=4" width="100px;"/><br/><sub><b>Ana Beatriz Alves</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="./assets/ANA BEATRIZ ROCHA.png" width="100px;" alt=""/><br/><sub><b>Ana Beatriz Rocha</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="./assets/ANA LUIZA LIMA.jpeg" width="100px;" alt=""/><br/><sub><b>Ana Luiza Lima</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104402971?v=4" width="100px;"/><br/><sub><b>Cristina Matsunaga</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/39159963?v=4" width="100px;"/><br/><sub><b>Francisco Luz</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="./assets/JORGE.jpeg" width="100px;" alt=""/><br /><sub><b>Jorge Herbster</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="./assets/LUCI.jpeg" width="100px;" alt=""/><br /><sub><b>Lucibelle Lemos</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/marianefontes" width="100px;" alt=""/><br /><sub><b>Mariane Fontes</b></sub></a><br/></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/112591325?v=4" width="100px;"/><br/><sub><b>Thiago Araújo</b></sub></a><br /></a></td>
  </tr>
</table>
