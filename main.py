from flask import Flask
from src.routes.chat_route import chat_route
from src.routes.predict_route import predict_route
# import src.utils.test
# import src.utils.combined_faiss_index

app = Flask(__name__)

# Registering routes
app.register_blueprint(predict_route)
app.register_blueprint(chat_route)

if __name__ == '__main__':
    app.run(debug=True)
