import pickle

# Vérifier le bundle Lille
print("=== BUNDLE LILLE ===")
with open('models/model_lille_best.pkl', 'rb') as f:
    lille_bundle = pickle.load(f)
print("Keys:", list(lille_bundle.keys()))

# Vérifier le bundle Bordeaux
print("\n=== BUNDLE BORDEAUX ===")
with open('models/model_bordeaux_best_2.pkl', 'rb') as f:
    bordeaux_bundle = pickle.load(f)
print("Keys:", list(bordeaux_bundle.keys())) 