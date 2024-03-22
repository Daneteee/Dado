class File_:

    # Escriu una llista de línies en un fitxer de text. Si el fitxer no existeix, el crea. Si el fitxer ja existeix,
    # sobreescriu el seu contingut. Pots especificar un missatge opcional per mostrar quan la operació s'ha completat
    # amb èxit.
    @staticmethod
    def write_lines_(file, lines, message=""):
        file = f"{file}"
        try:
            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print(f"{message}")
        except IOError:
            print("ERROR: No s'ha pogut escriure a l'arxiu")
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")

    # Escriu una cadena en un fitxer de text. Igual que write_lines, pots especificar un missatge opcional per
    # mostrar quan l'operació s'ha completat amb èxit.
    @staticmethod
    def write_(file, content, message=""):
        try:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"{message}")
        except IOError:
            print("ERROR: No s'ha pogut escriure a l'arxiu")
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")

    # Afegeix contingut al final d'un fitxer de text existent. Si el fitxer no existeix, el crea. També pots especificar
    # un missatge opcional per mostrar quan l'operació s'ha completat amb èxit.
    @staticmethod
    def append_(file, content, message=""):
        try:
            with open(file, 'a', encoding='utf-8') as f:
                f.write(content)
            print(f"{message}")
        except IOError:
            print("ERROR: No s'ha pogut escriure a l'arxiu")
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")

    # Llegeix totes les línies d'un fitxer de text i les retorna com una llista. Pots especificar un missatge opcional
    # per mostrar quan la operació s'ha completat amb èxit.
    @staticmethod
    def read_lines_(file, message=""):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            print(f"{message}")
            return lines
        except IOError:
            print("ERROR: No s'ha pogut escriure a l'arxiu")
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")

    # Llegeix tot el contingut d'un fitxer de text i el retorna com una cadena. Al igual que read_lines, pots
    # especificar un missatge opcional per mostrar quan la operació s'ha completat amb èxit.
    @staticmethod
    def read_(file, message=""):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.read()
            print(f"{message}")
            return lines
        except IOError:
            print("ERROR: No s'ha pogut escriure a l'arxiu")
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")

    # Verifica si un fitxer existeix i és accessible per a lectura/escriptura.
    @staticmethod
    def check_file(file):
        try:
            with open(file, "r+", encoding="utf-8"):
                pass
            print(f"El fitxer '{file}' existeix i és accessible per a lectura/escriptura.")
            return True
        except FileNotFoundError:
            print(f"ERROR: El fitxer '{file}' no existeix.")
            return False
        except PermissionError:
            print(f"ERROR: No tens permisos per a llegir/escriure el fitxer '{file}'.")
            return False
        except:
            print("ERROR: Alguna cosa no ha funcionat bé")
            return False
