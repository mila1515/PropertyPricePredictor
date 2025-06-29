import requests
import json

# Test de l'API Lille
def test_lille_api():
    url = "http://localhost:8000/predict/lille"
    data = {
        "surface_bati": 80,
        "nombre_pieces": 4,
        "type_local": "Appartement",
        "surface_terrain": 0,
        "nombre_lots": 1
    }
    
    response = requests.post(url, json=data)
    print("✅ Test Lille - Status:", response.status_code)
    result = response.json()
    print("✅ Réponse:", result)
    prix = result.get('prix_m2_estime', 0)
    print(f"✅ Prix: {prix} €/m²")

    assert response.status_code == 200
    assert prix > 0  # On veut un prix positif


# Test de l'API Bordeaux
def test_bordeaux_api():
    url = "http://localhost:8000/predict/bordeaux"
    data = {
        "surface_bati": 80,
        "nombre_pieces": 4,
        "type_local": "Maison",
        "surface_terrain": 100,
        "nombre_lots": 1
    }
    
    response = requests.post(url, json=data)
    print("✅ Test Bordeaux - Status:", response.status_code)
    result = response.json()
    print("✅ Réponse:", result)
    prix = result.get('prix_m2_estime', 0)
    print(f"✅ Prix: {prix} €/m²")

    assert response.status_code == 200
    assert prix > 0  # On veut un prix positif
