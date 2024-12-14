# 🎯 **Clusterização de Estilos de Jogo**

Bem-vindo ao repositório do projeto **Clusterização de Estilos de Jogo**, onde exploramos dados de jogadores de futebol para identificar padrões de desempenho e estilo de jogo. Utilizamos técnicas de Machine Learning, como K-means, para agrupar jogadores em categorias interpretáveis.

---

## 📊 **Objetivo**

Este projeto busca responder às seguintes questões:
1. Quais são os grupos de jogadores com características semelhantes de desempenho, independentemente de sua posição declarada?
2. Como esses grupos podem ser interpretados em termos de estilos de jogo?
3. Quais insights podem ser extraídos para auxiliar clubes, analistas e treinadores?

---

## 🛠️ **Estrutura do Repositório**

- **`data/`**: Contém os dados utilizados no projeto.
  - **`raw/`**: Dados brutos.
  - **`processed/`**: Dados tratados e prontos para análise.
- **`notebooks/`**: Jupyter Notebooks organizados por etapas do projeto.
- **`src/`**: Scripts Python para tratamento, clusterização e visualização.
- **`results/`**: Gráficos gerados, perfis dos clusters e outros resultados.
- **`requirements.txt`**: Lista de bibliotecas necessárias.
- **`README.md`**: Este arquivo com a documentação do projeto.

---

## 🚀 **Como Executar**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheuscsf/ucl_24_25_estilo_de_jogo.git
   cd project-ucl_24_25_estilo_de_jogo
   ```
2. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```
3. Execute os notebooks: Navegue para a pasta **`notebooks/`** e execute as etapas na ordem para reproduzir os resultados.

---

## 📂 Dados

Os dados originais estão disponíveis na pasta **`data/raw/`**. A principal base utilizada foi **`final_players_data.csv`**. Após o pré-processamento, os dados tratados podem ser encontrados em **`data/processed/`**.

---

## 🔑 Principais Resultados

- Clusters Identificados:
  - Criadores de Jogadas
  - Defensores Incansáveis
  - Finalizadores de Elite
  - E outros...

- Insights Extraídos:
  - Análise de talentos por estilo de jogo.
  - Identificação de áreas de desenvolvimento para jogadores.
  - Gráficos e Visualizações: Imagens geradas estão disponíveis na pasta **`results/cluster_visualizations/`**.
