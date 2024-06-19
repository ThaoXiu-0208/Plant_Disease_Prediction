import h5py
try:
    with h5py.File('trained_plant_disease_model.keras', 'r') as f:
        print("File opened successfully")
except OSError as e:
    print(f"Error opening file: {e}")
