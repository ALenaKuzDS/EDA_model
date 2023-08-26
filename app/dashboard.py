from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from category_encoders.target_encoder import TargetEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split

from explainerdashboard import *

if __name__ == '__main__':
    df = pd.read_csv('df.csv')

    X = df.drop(['age', 'rings'], axis=1)
    y = df['age']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=911)
    cat_features = ['sex']
    model =  Pipeline([('encoder_',TargetEncoder(cols=cat_features)), ('scaler_', StandardScaler()),
      ('model', GradientBoostingRegressor(learning_rate=0.01, max_depth=7, n_estimators=500,subsample=0.5))
       ]).fit(X_train, y_train)

    explainer = RegressionExplainer(model, X_test, y_test)

    db = ExplainerDashboard(explainer)
    db.to_yaml("dashboard.yaml", explainerfile="explainer.joblib", dump_explainer=True)