# Projeto Job Insights

Esse projeto foi realizado para exercitar o que foi aprendido no Seção 1 do Módulo de Ciência da Computação do curso da [Trybe](https://www.betrybe.com/), no qual foi sobre `Introdução á Linguagem Python`, `Entrada e Saída de dados` e `Testes`.

Neste projeto foram desenvolvidos módulos para realizarem análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também foram desenvolvidos testes unitários para os módulos e assim verificar a funcionalidade dos mesmos.

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/datasets/atharvap329/glassdoor-data-science-job-data), uma plataforma que disponibliza conjuntos de dados para cientistas de dados.

## Tecnologias

  - Python
  - Pytest
  - Flask
  - Docker

## Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone git@github.com:Lucas-Almeida-SD/Trybe-Projeto_34-Job_Insights.git

$ cd Trybe-Projeto_34-Job_Insights
```

Para iniciá-lo, siga os passos abaixo:

<details>
  <summary><strong>Com Docker</strong></summary>

  ```bash
  # Criar container e iniciar aplicação
  $ docker-compose up -d
  ```

  Para executar os testes, utilize o terminal interativo do container e insira o comando abaixo: 

  ```bash
  $ python3 -m pytest
  ```

  A aplicação estará disponível em [http://localhost:5000/](http://localhost:5000/).
</details>

<details>
  <summary><strong>Sem Docker</strong></summary>

  ```bash
  # criar o ambiente virtual
  $ python3 -m venv .venv

  # ativar o ambiente virtual
  $ source .venv/bin/activate

  # instalar as dependências no ambiente virtual
  $ python3 -m pip install -r dev-requirements.txt

  # iniciar a aplicação
  $ flask run
  ```

  Para executar os testes, insira o comando abaixo: 

  ```bash
  $ python3 -m pytest
  ```

  A aplicação estará disponível em [http://localhost:5000/](http://localhost:5000/).
</details>