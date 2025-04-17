
# Kwargs - Sukurkite funkciją, kuri formatuoja vartotojo profilio duomenis (vardas, amžius, vieta), 
# kur bet kuris laukas gali būti nenurodomas.

def rasti_bendrus(*args):
    if not args:
        return []
    
    pirmas_sarasas = args[0]
    rezultatas = []
    
    for elementas in pirmas_sarasas:
        yra_visuose = True
        
        for sarasas in args[1:]:
            if elementas not in sarasas:
                yra_visuose = False
                break
        
        if yra_visuose:
            rezultatas.append(elementas)
    
    return rezultatas

same_items = rasti_bendrus([1,2,3], [3,2,5],[2,3,8])
print(same_items)

def create_profile(**kwargs):

    user_profile = {}

    for elem in kwargs:
        if elem == "name":
            user_profile["name"] = kwargs[elem]
        elif elem == "age":
            user_profile["age"] = kwargs[elem]
        elif elem == "location":
            user_profile["location"] = kwargs[elem]
        else:
            print(f"Warning {elem} - argument is not used in this function")


    return user_profile


user = create_profile(name = "Rokas", age = 30, location = "Kaunas", academy = "CodeAcademy")
print(user)
