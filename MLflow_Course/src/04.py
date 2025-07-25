# g) Challenge avec la méthode mlflow.autolog()

import mlflow
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
import pandas as pd
from scipy.stats import randint

def load_and_prep_data(data_path: str):
    """Load and prepare data for training."""
    # Implémentez cette fonction
    df = pd.read_csv(data_path)
    X = data.drop(columns=["date", "demand"])
    X = X.astype('float')
    y = data["demand"]
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_val, y_train, y_val

def main():
    # Configuration de base
    EXPERIMENT_NAME = "4"
    N_TRIALS = 5

    # Configurez MLflow
    mlflow.set_tracking_uri("http://127.0.0.1:8080")
    apple_experiment = mlflow.set_experiment(EXPERIMENT_NAME)

    # Activez l'autologging
    mlflow.autolog()

    # Chargez les données
    X_train, X_val, y_train, y_val = load_and_prep_data("path_to_your_data.csv")

    # Définissez l'espace de recherche des hyperparamètres
    params={n_estimators:randint.rvs(2, 200, size=3)}
    # Implémentez cette partie

    # Créez et exécutez RandomizedSearchCV
    # Implémentez cette partie
    r=RandomForestRegressor()
    clf = RandomizedSearchCV(r, params)
    search = clf.fit(X_train, y_train)

    # Récupérez les informations sur le meilleur modèle
    # Implémentez cette partie
    b=search.best_params_

    # Créez un résumé des résultats
    r=f'{search.best_score_} {b}'
    # Implémentez cette partie

    # Enregistrez le résumé en tant qu'artifact
    #TODO
    # Implémentez cette partie

if __name__ == "__main__":
    main()
