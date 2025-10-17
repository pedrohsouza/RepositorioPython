# Repositório Python

## Comandos Git

Comandos úteis para usar com o GitHub Codespaces/GitPod.

Para utilizar localmente (com um editor de código no próprio computador), podem ser necessários outros comandos.

Caso precisar, segue uma lista com mais exemplos [aqui](https://github.com/RafaelWillians/GitHubExample/tree/main/git-crash-course).

#### Consultar status do repositório
Mostram os arquivos que foram ou não adicionados para Staging (uma fila de arquivos que estão prontos para serem gravados no histórico do repositório).
```sh
git status
```

#### Criar uma branch e alternar para ela
```sh
git checkout -b <nome da branch>
```

#### Adicionar arquivo para Staging
```sh
git add <nome do arquivo>
```

#### Adicionar todos os arquivos para Staging
```sh
git add .
```

#### Dar commit
Gravar os arquivos e alterações para o histórico do repositório.
Detalhe que com esse comando essas alterações ainda não estão salvas no GitHub.
```sh
git commit -m "Texto da mensagem"
```

#### Subir as alterações para o repositório
Salvar no GitHub todos os commits que fez no ambiente.
```sh
git push
```