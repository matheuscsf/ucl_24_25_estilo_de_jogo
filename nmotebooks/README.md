# 📂 Pasta `notebooks/`

Esta pasta contém os **Jupyter Notebooks** organizados por etapas do projeto **Clusterização de Estilos de Jogo**. Cada notebook cobre uma parte específica do fluxo de trabalho, desde a análise exploratória até a obtenção dos insights finais.

---

## 🗂️ Estrutura

- **`1_exploratory_analysis.ipynb`**:  
  Realiza a análise exploratória dos dados, incluindo:  
  - Verificação da estrutura dos dados.
  - Estatísticas descritivas.
  - Visualização de distribuições e correlações.

- **`2_preprocessing.ipynb`**:  
  Aplica o pré-processamento aos dados, como:  
  - Tratamento de valores ausentes.
  - Normalização/padronização.
  - Seleção de variáveis relevantes para a clusterização.

- **`3_clustering.ipynb`**:  
  Executa o processo de clusterização, incluindo:  
  - Definição do número de clusters usando o método Elbow e Silhouette Score.
  - Aplicação do algoritmo K-means.
  - Interpretação inicial dos clusters.

- **`4_results_and_insights.ipynb`**:  
  Analisa os resultados e gera os insights:  
  - Perfis detalhados dos clusters.
  - Visualizações (gráficos de dispersão, boxplots, etc.).
  - Conclusões e recomendações baseadas nos resultados.

---

## 🛠️ Como Utilizar

1. **Configuração do Ambiente**:
   - Certifique-se de que todas as dependências do projeto estão instaladas. Veja `requirements.txt`.

2. **Ordem de Execução**:
   - Execute os notebooks na ordem numérica (1, 2, 3, 4) para garantir a reprodução correta dos resultados.

3. **Personalização**:
   - Modifique os notebooks para explorar diferentes configurações ou para incluir novos dados.

---

## 📊 Exemplos de Saídas

- **`1_exploratory_analysis.ipynb`**: Histogramas das distribuições das variáveis.  
- **`2_preprocessing.ipynb`**: Dados tratados e normalizados.  
- **`3_clustering.ipynb`**: Cluster labels atribuídos aos jogadores.  
- **`4_results_and_insights.ipynb`**: Gráficos interpretativos e perfis dos clusters.

---

## ⚠️ Avisos

- Os notebooks utilizam bibliotecas como `pandas`, `numpy`, `matplotlib`, `seaborn` e `sklearn`. Garanta que elas estão instaladas.  
- Antes de executar, verifique se os dados estão na estrutura correta na pasta `data/`.

---

**📓 Notebooks organizados para insights incríveis!** 🚀
