import pickle

def save_to_file(filename, variable):
    with open(filename, "wb") as failas:
        pickle.dump(variable, failas)

def load_from_file(filename):
    with open(filename, "rb") as failas:
        return pickle.load(failas)