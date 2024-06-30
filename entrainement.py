from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

import pandas as pd
import joblib

# Charger les données (remplacez par votre propre dataset)
df = pd.read_excel('Insurance-data.xlsx')

# Définir les caractéristiques et la cible
X = df.drop(columns=['charges'])  # Remplacez 'charges' par le nom de votre colonne cible
y = df['charges']  # Remplacez 'charges' par le nom de votre colonne cible

# Définir les caractéristiques numériques et catégorielles
numeric_features = ['age', 'bmi', 'children']
categorical_features = ['sex', 'smoker', 'region']

# Créer un transformateur pour les caractéristiques numériques
numeric_transformer = StandardScaler()

# Créer un transformateur pour les caractéristiques catégorielles
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Créer un préprocesseur avec les transformations appropriées
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Créer un pipeline complet avec le modèle et le préprocesseur
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', GradientBoostingRegressor())
])

# Séparer les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le pipeline complet
pipeline.fit(X_train, y_train)

# Sauvegarder le pipeline complet
joblib.dump(pipeline, 'pipeline_model.pkl')
