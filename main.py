import json
import requests

response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
 
dishes = json.loads(response.content)

menu = dishes[:20]

def dish_fetch(num):
  return menu[num - 1]


def main():
  print("=== MENÚ DE PLATOS TÍPICOS DE COLOMBIA ===\n")
  for i, plato in enumerate(menu, start=1):
    print(f"{i}. {plato['name']}")

  seleccion = int(input("\nElige el número de un plato para ver su descripción: "))
  plato = dish_fetch(seleccion)

  print(f"\nPlato típico: {plato['name']}")
  print(f"Descripción: {plato['description']}")

if __name__=="__main__":
  main()