# Chace System with Redis
API com manipulação de dados via Redis e Mysql desenvolvido com FastAPI
<br><br><br>

![proj_redis](https://github.com/LariLealDias/Cache-system-for-a-blog/assets/108475403/f5e7cf76-43c4-4d60-b06f-b460fb0050a0)


## 🛠️ FERRAMENTAS E TECNOLOGIAS
<img src="https://skillicons.dev/icons?i=py,fastapi,redis,mysql,docker,postman,vscode" />
• Python
• FastAPI
• Redis
• Mysql • ORM sqlalchemy
• Docker
• Postman
• Vscode

<br><br><br>



## 📝 DESCRIÇÃO
**O foco deste projeto é a manipulação de dados com redis.**

Manipulções CRUD do objeto Post(postagens) para um sistema de blog com armazenamento em banco MYSQL e em Redis. Desenvolvido com o framework FastAPI do Python. 
As manipulações do banco MySQL foram realizadas com o ORM sqlalchemy. O Docker foi utilizado para baixar a imagem oficial do Redis.


<br><br>
 ### ℹ️ INFORMAÇÕES
Este projeto visa a lógica de desenvolvimento com Redis, ou seja: 
- Método POST: cria um objeto no banco, se sucesso nesta operação, é criando o mesmo objeto no banco Redis.
- Método GET: a consulta é priorizada no banco Redis, caso não tenha, a busca é diretamento no banco MySQL, caso esta operação tenha sucesso, é setado o objeto encontrado no banco Redis.
- Método PATCH: esta ação modifica primeiro o objeto no banco MySQL, se sucesso, é setado novamento este objeto no banco Redis
- Método DELETE: deleta o objeto primeiro no banco MySQL e se sucesso, deleta no banco MySQL

O TTL configurado é de 6h, equivalente a 21600 segundos.

 

<br><br><br>
## 👩‍💻 Autora
Larissa Leal 
<br><br>
[![Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/larissa-leal-dias-408455157/)

