# 📂 Pasta `src/`

Esta pasta contém os **scripts Python** utilizados no projeto **Clusterização de Estilos de Jogo**. Esses scripts foram criados para modularizar e automatizar partes do fluxo de trabalho, como pré-processamento, clusterização e visualização.

---

## 🗂️ Estrutura

- **`preprocessing.py`**:  
  Funções para o tratamento de dados, incluindo:  
  - Tratamento de valores ausentes.  
  - Normalização e padronização.  
  - Seleção de variáveis relevantes.

- **`clustering.py`**:  
  Funções para aplicar e avaliar algoritmos de clusterização, como:  
  - Definição do número de clusters usando Elbow e Silhouette Score.  
  - Implementação de K-means e retorno dos rótulos.  

- **`visualization.py`**:  
  Funções para visualização de dados e resultados, incluindo:  
  - Histogramas e boxplots para análise exploratória.  
  - Gráficos de dispersão (usando PCA ou t-SNE) para clusters.  
  - Visualizações personalizadas dos perfis dos clusters.

---

## 🛠️ Como Utilizar

1. **Importe os scripts no seu notebook ou aplicação**:  
   Exemplos:  
   ```python
   from src.preprocessing import handle_missing_values, normalize_data
   from src.clustering import determine_clusters, apply_kmeans
   from src.visualization import plot_cluster_scatter, plot_boxplots
   ```
2. Automatize as etapas do projeto:
- Substitua código repetitivo nos notebooks pelas funções disponíveis nos scripts.
3. Personalize:
- Adicione ou edite funções conforme necessário para atender a novos casos de uso.

---

## 📋 Exemplos de Funções

**`preprocessing.py`**
- **`handle_missing_values(df)`**: Trata valores ausentes usando estratégias como média ou mediana.
- **`normalize_data(df)`**: Normaliza as variáveis numéricas com StandardScaler.

**`clustering.py`**
- **`determine_clusters(data, range_clusters)`**: Usa Elbow e Silhouette para sugerir o número ideal de clusters.
- **`apply_kmeans(data, n_clusters)`**: Aplica K-means aos dados e retorna os rótulos.

**`visualization.py`**
- **`plot_cluster_scatter(data, labels)`**: Gera gráficos de dispersão 2D ou 3D para clusters.
- **`plot_boxplots(data, labels, columns)`**: Cria boxplots comparando variáveis entre clusters.
