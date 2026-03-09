from typing import List, Dict, Union

def main() -> None:
    
    people: List[Dict[str, Union[str, int]]] = [
        {"name": "Ali", "age": 25},
        {"name": "Veli", "age": 19},
        {"name": "Ayşe", "age": 18},
        {"name": "Mehmet", "age": 30},
        {"name": "Ahmet", "age": 15},
        {"name": "Zeynep", "age": 17},
        {"name": "Cem", "age": 22}
    ]

    filteredlist = [
        person for person in people 
        if person["age"] > 20 or person["name"].startswith("A")
    ]

    print("Kriterlere Uyan Kişiler")
    for selected in filteredlist:
        print(f"İsim: {selected['name']:<8} Yaş: {selected['age']}")

if __name__ == "__main__":
    main()