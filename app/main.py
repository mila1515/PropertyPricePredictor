from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routes import predict_lille, predict_bordeaux, predict

app = FastAPI(
    title="API Estimation Prix m²",
    description="API pour estimer le prix au m² des biens immobiliers à Lille et Bordeaux",
    version="1.0.0"
)

app.include_router(predict_lille.router)
app.include_router(predict_bordeaux.router)
app.include_router(predict.router)


# @app.get("/")
# def read_root():
#     return {
#         "message": "Bienvenue sur l'API d'estimation de prix m²",
#         "endpoints": {
#             "lille": "/predict/lille",
#             "bordeaux": "/predict/bordeaux"
#         }
#     }


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>API Estimation Prix m²</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4; }
                h1 { color: #2c3e50; }
                a { text-decoration: none; color: #3498db; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>🏠 API Estimation de prix immobilier</h1>
            <p>Bienvenue sur l’API permettant d’estimer le prix au m² de biens immobiliers à <strong>Lille</strong> et <strong>Bordeaux</strong>.</p>
            <p>Accès rapide :</p>
            <ul>
                <li><a href="/docs">📘 Interface Swagger</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
