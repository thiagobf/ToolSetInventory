import random
from pathlib import Path

base_record = "José de Salles;Av. São Paulo, 1250;Brazil;+55 19 980901202"

first_names = [
    "José", "Maria", "Carlos", "Ana", "Pedro", "Luiza", "Rafael", "Beatriz",
    "Thiago", "Camila", "Lucas", "Fernanda", "Gustavo", "Juliana", "Mateus",
    "Larissa", "Bruno", "Patrícia", "Daniel", "Sofia"
]

last_names = [
    "de Salles", "Silva", "Souza", "Oliveira", "Pereira", "Costa", "Lima",
    "Almeida", "Ferreira", "Santos", "Ribeiro", "Martins", "Gomes", "Rodrigues",
    "Nunes", "Barbosa", "Mendonça", "Teixeira", "Carvalho", "Azevedo"
]

streets = [
    "Av. São Paulo", "Rua das Flores", "Rua da Liberdade", "Av. Brasil", "Rua XV de Novembro",
    "Alameda Santos", "Rua Augusta", "Av. Paulista", "Rua do Comércio", "Praça da Sé"
]

countries = ["Brazil", "Argentina", "Chile", "Colombia", "Peru", "Uruguay", "Paraguay", "Mexico", "Portugal", "Spain"]
phone_prefixes = ["+55 11", "+55 12", "+55 13", "+55 14", "+55 15", "+55 16", "+55 17", "+55 18", "+55 19", "+55 21", "+55 31", "+55 41"]


def build_record(index: int) -> str:
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    address = f"{random.choice(streets)}, {random.randint(100, 5000)}"
    country = random.choice(countries)
    phone = f"{random.choice(phone_prefixes)} {random.randint(900000000, 999999999)}"
    return f"{name};{address};{country};{phone}"


if __name__ == "__main__":
    workspace_root = Path(__file__).resolve().parents[1]
    output_path = workspace_root / "database" / "rawdata" / "random_records_1000.csv"
    records = [build_record(i) for i in range(1000)]
    output_path.write_text("\n".join(records), encoding="utf-8")
    print(f"Generated {len(records)} records in {output_path}")
