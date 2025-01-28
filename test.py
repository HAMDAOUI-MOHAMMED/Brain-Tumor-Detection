import h5py

try:
    with h5py.File('model/brain.h5', 'r') as file:
        print("Fichier ouvert avec succès")
except OSError as e:
    print(f"Erreur lors de l'ouverture du fichier : {e}")
