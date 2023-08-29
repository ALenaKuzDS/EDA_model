
# Разведочный анализ данных и основы разработки

1. Создание репозитория на GitHub:
* Регистрируемся на GitHub.
* Создаем новый репозиторий.
* Заходим в меню Settings -> переходим на вкладку Collaborators и нажимаем Add people -> в появившемся окне указываем aiedu-courses -> Выбираем пользователя и нажимаем Add aiedu-courses to this repository.

2. Проведение анализа данных
* Оценка значений признаков и основных статистик, в том числе выбросы, нулевые значения и дубли
* Построения рапределений признаков
* Изучение корреляций(Пирсона, Кэндала и Спирмена) 

3. Обучение модели
* Обучение только на числянных и числянных + категориальном признаках
* Построение pipeline с TargetEncoder для кодирования категориального признака и StandardScaler для масштабирования числянных признаков
* Подбор лучшей модели без подбора гиперпараметров из следующего перечня: KNeighborsRegressor(), LinearSVR, DecisionTreeRegressor, RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, CatBoostRegressor, LGBMRegressor, XGBRegressor
* По лучшей модели проведен подбор гипер-параметров
* Важность признаков, метрики и проч. рассмотрены с поомщью библиотеки Shap и в построенном Explainer Dashboard 

4. Деплой ExplainerDashboard, который построен на этапе разработки модели.
* Экспорт дашборда в yaml формат
* Вынесение запуска ExplainerDashboard в отдельный файл app.py
* Создание Dockerfile(https://hub.docker.com/repository/docker/alenakuzds/explainerdashboard/general)
