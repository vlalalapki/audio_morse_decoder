export $(grep -v '^#' ../.env | xargs)
export TRACKING_SERVER_PORT=$TRACKING_SERVER_PORT

mlflow ui --port ${TRACKING_SERVER_PORT} --backend-store-uri sqlite:///mlruns.db
