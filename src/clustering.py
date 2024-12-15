# Selecionar as variáveis representativas para clusterização
selected_columns = [
    'goals', 'assists', 'total_attempts',  # Ofensivas
    'tackles', 'blocked', 'clearance_attempted',  # Defensivas
    'passing_accuracy(%)', 'dribbles',  # Habilidade Técnica
    'distance_covered(km/h)', 'height(cm)'  # Outros
]

# Criar um novo DataFrame com as colunas selecionadas
cluster_data = scaled_data[selected_columns]

# Exibir as primeiras linhas das variáveis selecionadas
cluster_data.head()
# Testar diferentes números de clusters para o método Elbow e Silhouette Score
elbow_inertia = []
silhouette_scores = []
cluster_range = range(2, 11)
for k in cluster_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(reduced_data)
    elbow_inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(reduced_data, kmeans.labels_))
    # Plotar o método Elbow
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, elbow_inertia, marker='o', linestyle='--')
plt.title('Método Elbow para Determinar o Número de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Inércia (Elbow)')
plt.grid()
plt.show()
# Plotar o Silhouette Score
plt.figure(figsize=(10, 6))
plt.plot(cluster_range, silhouette_scores, marker='o', linestyle='--', color='orange')
plt.title('Silhouette Score para Diferentes Números de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Silhouette Score')
plt.grid()
plt.show()
# Determinar o número ideal de clusters com base nos gráficos
optimal_clusters_elbow = cluster_range[elbow_inertia.index(min(elbow_inertia)) - 1]
optimal_clusters_silhouette = cluster_range[silhouette_scores.index(max(silhouette_scores))]
# Aplicar o algoritmo de K-means com 9 clusters
kmeans_model = KMeans(n_clusters=9, random_state=42)
kmeans_labels = kmeans_model.fit_predict(reduced_data)
# Adicionar os rótulos dos clusters à base de dados original
clustered_data = cluster_data.copy()
clustered_data['Cluster'] = kmeans_labels
# Exibir as primeiras linhas com os clusters
clustered_data.head()
# Calcular as médias das métricas por cluster
cluster_means = clustered_data.groupby('Cluster').mean()
cluster_means