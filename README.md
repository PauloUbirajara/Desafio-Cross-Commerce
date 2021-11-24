# Desafio Cross-Commerce

- Linguagem: Python
- Framework: Flask
- Dependências utilizadas:
  - [Flask](https://palletsprojects.com/p/flask/)
  - [requests](https://docs.python-requests.org/en/master/index.html)
  - [Unittest](https://docs.python.org/3/library/unittest.html)

## Como usar:
### Para iniciar a aplicação:
- Ir até a pasta `/src/`
- Executar `flask run` no terminal
- Os números ordenados estarão disponibilizados na seguinte URL: 
  - `http://localhost:5000/api`

### Para executar os testes:
- Ir até a pasta `/tests/`
- Executar o seguinte comando:
  ```bash
  $ python -m unittest discover -s . -p "test_*.py" -v
  ```
