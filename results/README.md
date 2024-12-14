# 📂 Pasta `results/`

Esta pasta contém os **resultados e saídas do projeto** **Clusterização de Estilos de Jogo**. Aqui estão armazenados os perfis dos clusters, visualizações geradas e outros arquivos derivados das análises.

---

## 🗂️ Estrutura

- **`cluster_visualizations/`**:  
  Gráficos e visualizações gerados durante o projeto, incluindo:  
  - Gráficos de dispersão (usando PCA para projeção 2D ou 3D).  
  - Boxplots comparativos das métricas entre clusters.  

- **`cluster_profiles.csv`**:  
  Arquivo contendo as médias das métricas para cada cluster, permitindo identificar os padrões específicos de cada grupo.  

---

## 📋 Exemplos de Conteúdo

### **`cluster_visualizations/`**
- **`scatter_clusters_pca.png`**: Gráfico de dispersão dos clusters baseado na projeção PCA.  
- **`boxplot_goals_by_cluster.png`**: Boxplot mostrando a distribuição de `goals` por cluster.  
- **`silhouette_score_plot.png`**: Gráfico do Silhouette Score usado na avaliação do modelo.

### **`cluster_profiles.csv`**
| **Cluster** | **Goals** | **Assists** | **Total Attempts** | **Tackles** | ... |  
|-------------|-----------|-------------|---------------------|-------------|-----|  
| 0           | 0.43      | 0.74        | 2.15               | 0.08        | ... |  
| 1           | -0.31     | -0.36       | -0.57              | -0.52       | ... |  
| ...         | ...       | ...         | ...                | ...         | ... |

---


## 🛠️ Como Utilizar

1. **Explorar Gráficos**:
   - Os gráficos na pasta `cluster_visualizations/` fornecem insights visuais sobre os clusters e as métricas.

2. **Analisar Perfis dos Clusters**:
   - Use o arquivo `cluster_profiles.csv` para explorar as características médias de cada grupo.

3. **Criar Relatórios**:
   - Use os arquivos desta pasta como base para relatórios e apresentações.

---

## 📊 Exemplos de Insights

- **Clusters Identificados**:
  - Cluster 0: Alta média de dribles e distância percorrida. Possível interpretação: "Jogadores de Mobilidade" ou "Criadores de Jogadas".
  - Cluster 1: Baixas métricas em quase todas as variáveis. Possível interpretação: "Jogadores Menos Participativos".
  - Cluster 2: Alta média em tackles e distância percorrida. Possível interpretação: "Defensores Incansáveis".
  - Cluster 5: Altas métricas ofensivas, como gols e tentativas. Possível interpretação: "Finalizadores".
  - Cluster 6: Alta média de assistências e dribles. Possível interpretação: "Assistentes Técnicos".
  - Cluster 7: Alta média de clearance e tackles. Possível interpretação: "Defensores Clássicos".
  - Cluster 8: Baixas métricas gerais, mas sem características distintivas fortes.

- **Visualizações**:
  - Gráficos comparativos ajudam a identificar rapidamente as forças e fraquezas de cada cluster.
