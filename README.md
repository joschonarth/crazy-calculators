# 🧮 Calculadoras Malucas

Este projeto implementa uma série de calculadoras desenvolvidas com boas práticas de **design de código** e **clean code**. Criado utilizando **Python** e **Flask**, ele também faz uso das poderosas bibliotecas **NumPy** para cálculos avançados e **Pytest** para garantir a qualidade através de testes automatizados. O objetivo é proporcionar uma solução robusta e eficiente, seguindo princípios de desenvolvimento limpo e organizado.

---

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python**: Linguagem de programação principal.
- 🌐 **Flask**: Framework web utilizado para expor as rotas das calculadoras.
- 🔢 **Numpy**: Biblioteca para cálculos matemáticos complexos.
- 🧪 **Pytest**: Ferramenta para testes automatizados.

---

## 📋 Regras de Negócio

### 1️⃣ Primeira Calculadora

- Um número é dividido em **3 partes iguais**.
  1. A **primeira parte** é dividida por 4, somada a 7, elevada ao quadrado e multiplicada por 0.257.
  2. A **segunda parte** é elevada à potência de 2.121, dividida por 5 e somada a 1.
  3. A **terceira parte** permanece inalterada.
- O resultado final é a soma desses três valores.

### 2️⃣ Segunda Calculadora

- **N números** são enviados como entrada.
- Cada número é multiplicado por 11 e elevado à potência de 0.95.
- O desvio padrão dos resultados é calculado e retornado como o **inverso** (1 / resultado).

### 3️⃣ Terceira Calculadora

- **N números** são fornecidos como entrada.
- Se a **variância** dos números for **menor** que a multiplicação entre eles:
  - Uma mensagem de sucesso é retornada.
- Caso contrário:
  - Uma mensagem de falha é exibida.

### 4️⃣ Quarta Calculadora

- **N números** são fornecidos como entrada.
- A **média** dos números é calculada e retornada.

---

## 🏗️ Design Patterns

O projeto utiliza dois padrões de design principais, aplicados para melhorar a organização e a escalabilidade do código.

### 🏠 Padrão Facade

A aplicação do **Padrão Facade** simplifica o uso das bibliotecas externas, como o `NumPy`, oferecendo uma interface simplificada para a lógica principal das calculadoras. Isso ajuda a reduzir a complexidade no código que interage diretamente com essas bibliotecas.

### 🏭 Padrão Factory

O **Padrão Factory** é utilizado para separar a responsabilidade de criação das instâncias das calculadoras. Dentro da pasta `factories`, há um arquivo específico para cada calculadora, que é responsável por criar a instância correspondente. Isso mantém o arquivo de rotas mais limpo e focado na interação com o usuário.

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:

    ```bash
    git clone 
    cd 
    ```

2. Crie um ambiente virtual (opcional):

   ```bash
   python -m venv .venv
   ```

   2.1. Ative o ambiente virtual:

    ```bash
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate   # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor Flask:

    ```bash
    python run.py
    ```

5. Acesse o projeto em `http://localhost:5000`.

---

## 🌐 Rotas

### 1️⃣ POST - `/calculator/1`

**Request:**

```json
{
    "number": 3
}
```

**Response:**

```json
{
    "data": {
        "calculator": 1,
        "result": 15.71
    }
}
```

### 2️⃣ POST - `/calculator/2`

**Request:**

```json
{
    "numbers": [2.12, 4.62, 1.32]
}
```

**Response:**

```json
{
    "data": {
        "calculator": 2,
        "result": 0.08
    }
}
```

### 3️⃣ POST - `/calculator/3`

**Request:**

```json
{
    "numbers": [1, 2, 3, 4, 5]
}
```

**Response:**

```json
{
    "data": {
        "calculator": 3,
        "success": true,
        "value": 2.0
    }
}
```

**Request:**

```json
{
    "numbers": [1, 1, 1, 1, 1000]
}
```

**Response:**

```json
{
    "errors": [
        {
            "detail": "Process failure: variance greater than multiplication",
            "title": "BadRequest"
        }
    ]
}
```

### 4️⃣ POST - `/calculator/4`

**Request:**

```json
{
    "numbers": [1, 2, 3, 4, 5]
}
```

**Response:**

```json
{
    "data": {
        "calculator": 4,
        "success": true,
        "value": 3.0
    }
}
```

---

## 🧪 Testes

Os testes podem ser executados com o `Pytest`. Para rodar todos os testes, use o seguinte comando:

```bash
pytest
```

## 📚 Documentações e Links Úteis

- 🐍 **Python Documentation**: [Documentação oficial do Python](https://docs.python.org/3/).
- 📖 **Flask Documentation**: [Documentação oficial do Flask](https://flask.palletsprojects.com/).
- 📘 **NumPy Documentation**: [Documentação oficial do NumPy](https://numpy.org/doc/stable/index.html).
- 🧪 **Pytest Documentation**: [Documentação oficial do Pytest](https://docs.pytest.org/en/stable/).
- 🏠 **Facade Pattern**: [Padrão de Design Facade](https://refactoring.guru/design-patterns/facade).
- 🏭 **Factory Pattern**: [Padrão de Design Factory](https://refactoring.guru/design-patterns/factory-method).

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

---

## 📞 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joschonarth/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joschonarth@gmail.com)
