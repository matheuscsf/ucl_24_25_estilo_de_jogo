# 📂 Pasta `data/`

Esta pasta contém todos os dados utilizados no projeto **Clusterização de Estilos de Jogo**. Ela está organizada em subpastas para facilitar o entendimento e o uso dos dados em diferentes etapas do projeto.

---

## 🗂️ Estrutura

- **`raw/`**: Contém os dados brutos que foram carregados inicialmente. Estes dados estão no formato original, sem pré-processamento ou limpeza.
- **`processed/`**: Contém os dados tratados e prontos para análise. Estas versões foram limpas, normalizadas e preparadas para as etapas de modelagem.
- **`final_players_data.csv`**: Arquivo principal de entrada, contendo as informações detalhadas dos jogadores.

---

## 📋 Descrição dos Dados

### Arquivo Principal: `final_players_data.csv`

| **Coluna**               | **Descrição**                                                              |
|--------------------------|---------------------------------------------------------------------------|
| `id_player`              | Identificador único do jogador.                                           |
| `player_name`            | Nome do jogador.                                                          |
| `nationality`            | Nacionalidade do jogador.                                                 |
| `field_position`         | Posição principal em campo (ex.: Forward, Midfielder).                     |
| `position`               | Posição específica (ex.: Striker, Central Midfielder).                    |
| `weight(kg)`             | Peso do jogador em quilogramas.                                           |
| `height(cm)`             | Altura do jogador em centímetros.                                         |
| `age`                    | Idade do jogador.                                                        |
| `goals`                  | Número de gols marcados.                                                 |
| `assists`                | Total de assistências realizadas.                                         |
| `dribbles`               | Total de dribles realizados.                                              |
| ...                      | **Outras variáveis relevantes detalhadas no notebook de EDA**.           |

> Para mais informações sobre os dados e como eles foram processados, consulte o notebook de **análise exploratória (EDA)** em `notebooks/1_exploratory_analysis.ipynb`.

---

## 🛠️ Como Utilizar

1. **Para Análise**:
   - Use os dados de `raw/` para reproduzir a etapa de pré-processamento.
   - Use os dados de `processed/` para ir diretamente à modelagem.

2. **Atualização de Dados**:
   - Substitua ou adicione novos arquivos em `raw/`, garantindo o versionamento apropriado.

---

## ⚠️ Avisos

- **Privacidade**: Certifique-se de que os dados não contenham informações sensíveis antes de compartilhar.
- **Qualidade dos Dados**: Revise os dados em `raw/` antes de usá-los diretamente, pois eles podem conter inconsistências ou valores ausentes.

---
