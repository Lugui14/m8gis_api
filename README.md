# M8 GIS

## API

Para rodar a api é necessario executar os seguintes comandos:

```bash
  # cria ambiente virtual
  python -m venv venv
  .\venv\Scripts\activate

  # instala dependencias
  pip install -r requirements.txt

  # roda migrations
  python -m flask db upgrade

```

Para criar novas migrations é necessário adicionar uma entidade e rodas o comando:

```bash
  #cria migrations
  python -m flask db migrate "migration_name"
```

### Avisos

- Escrever codigo basico em ingles e usar português para nomear tabelas
- Não esqueça de colocar as variaveis de ambiente
