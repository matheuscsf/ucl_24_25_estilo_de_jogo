# Gráficos de dispersão usando PCA para projeção 2D
plt.figure(figsize=(10, 8))
plt.scatter(reduced_data['PC1'], reduced_data['PC2'], c=kmeans_labels, cmap='tab10', alpha=0.6)
plt.title('Dispersão dos Clusters (Projeção PCA 2D)')
plt.xlabel('Componente Principal 1 (PC1)')
plt.ylabel('Componente Principal 2 (PC2)')
plt.colorbar(label='Clusters')
plt.grid()
plt.show()

# Boxplots para comparar variáveis entre clusters
for column in cluster_data.columns:
    plt.figure(figsize=(12, 6))
    clustered_data.boxplot(column=column, by='Cluster', grid=False, patch_artist=True, showmeans=True)
    plt.title(f'Boxplot: {column} por Cluster')
    plt.suptitle('')  # Remove o título automático do Pandas
    plt.xlabel('Cluster')
    plt.ylabel(column)
    plt.show()