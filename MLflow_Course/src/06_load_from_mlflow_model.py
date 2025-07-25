import mlflow
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. Chargement des données
print("Chargement des données...")
data = pd.read_csv('data/fake_data.csv')
X = data.drop(columns=["date", "demand"])
X = X.astype('float')

# 2. Définir le chemin vers le modèle MLflow
model_path = '/home/ubuntu/MLflow_Course/mlruns/534228407498600468/64abd802e94b44f7bdfe2a267462430b/artifacts/rf_apples'  # Par exemple : '/home/ubuntu/MLflow/mlruns/EXPERIMENT_ID/RUN_ID/artifacts/rf_apples'

# 3. Charger le modèle
print("Chargement du modèle...")
model = mlflow.sklearn.load_model(model_path)

# 4. Faire des prédictions sur l'ensemble du jeu de données
print("Calcul des prédictions...")
predictions = model.predict(X)

# 5. Calculer et afficher la moyenne des prédictions
mean_prediction = predictions.mean()  # Utiliser la fonction appropriée de numpy ou pandas

print(f"\nRésultats :")
print(f"Nombre de prédictions : {len(predictions)}")
print(f"Moyenne des prédictions : {mean_prediction:.2f}")

# mlflow models serve \
#         --model-uri '/home/ubuntu/MLflow_Course/mlruns/534228407498600468/64abd802e94b44f7bdfe2a267462430b/artifacts/rf_apples' \
#         --port 5002 \
#         --host 0.0.0.0 \
#         --env-manager local
