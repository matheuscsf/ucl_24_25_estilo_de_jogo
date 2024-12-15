# Carregar o arquivo enviado pelo usuário
file_path = 'final_players_data.csv'
data = pd.read_csv(file_path)

# Exibir as primeiras linhas da base de dados para revisão
data.head()
# Excluir a coluna 'player_image'
data.drop(columns=['player_image'], inplace=True)

# Confirmar se a coluna foi removida
data.head()
# Verificar a estrutura dos dados
data_info = data.info()
data_info
# Análise descritiva inicial
data_description = data.describe()
data_description
# Excluir colunas irrelevantes ou redundantes
columns_to_drop = ['id_player', 'id_team', 'player_name', 'nationality', 'field_position', 'position']
data.drop(columns=columns_to_drop, inplace=True)

# Confirmar a exclusão das colunas
data.head()
# Verificar o número e a proporção de valores nulos por coluna
missing_data = data.isnull().sum()
missing_data_percentage = (missing_data / len(data)) * 100

# Consolidar as informações de valores ausentes em uma tabela
missing_summary = pd.DataFrame({
    'Coluna': missing_data.index,
    'Valores Nulos': missing_data.values,
    'Percentual de Nulos (%)': missing_data_percentage.values
}).sort_values(by='Percentual de Nulos (%)', ascending=False)

missing_summary
# 1. Imputar valores para variáveis com alta proporção de nulos usando a mediana
high_null_columns = ['weight(kg)', 'height(cm)']
for col in high_null_columns:
    if col in data.columns:
        data[col].fillna(data[col].median(), inplace=True)
        # 2. Imputar valores para variáveis com proporção moderada de nulos usando a média
moderate_null_columns = [
    'offsides', 'tackles', 'crosses_attempted', 'dribbles',
    'clearance_attempted', 'total_attempts'
]
for col in moderate_null_columns:
    if col in data.columns:
        data[col].fillna(data[col].mean(), inplace=True)
        # 4. Remover linhas com muitos valores nulos
threshold = len(data.columns) * 0.5  # Mais de 50% de nulos
data = data.dropna(thresh=threshold)
# Verificar se restam valores nulos
remaining_nulls = data.isnull().sum().sum()
remaining_nulls
# Criar um objeto StandardScaler
scaler = StandardScaler()
# Aplicar a padronização
scaled_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
# Confirmar a transformação ao exibir as primeiras linhas
scaled_data.head()