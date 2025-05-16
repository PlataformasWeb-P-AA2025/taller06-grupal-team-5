from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from genera_base2 import Country

engine = create_engine('sqlite:///tableCountries.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Presentar todos los países del continente americano (asumiendo América = NA + SA)
print("Consulta 1: Presentar todos los países del continente americano (asumiendo América = NA + SA)")
paises_americanos = session.query(Country).filter(Country.continent.in_(['NA', 'SA'])).all()
for c in paises_americanos:
    print(c.name, " | ", c.continent)

print("\n----------------------------\n")

# 2. Presentar países de Asia ordenados por Dial
print("Consulta 2: Presentar países de Asia ordenados por Dial)")
paises_asia = session.query(Country).filter(Country.continent == 'AS').order_by(Country.dial).all()
for c in paises_asia:
    print(c.name, " | ", c.dial)

print("\n----------------------------\n")

# 3. Presentar los lenguajes de cada país
print("Consulta 3: Presentar los lenguajes de cada país")
todos_paises = session.query(Country).all()
for c in todos_paises:
    print(c.name, " | ", c.languages)

print("\n----------------------------\n")

# 4. Países de Europa ordenados por capital
print("Consulta 4: Países de Europa ordenados por capital")
paises_europa = session.query(Country).filter(Country.continent == 'EU').order_by(Country.capital).all()
for c in paises_europa:
    print(c.capital, " | ", c.name)

print("\n----------------------------\n")

# 5. Países cuyo nombre contenga "uador" o capital contenga "ito"
print("Consulta 5: Países cuyo nombre contenga uador o capital contenga ito")
paises_filtrados = session.query(Country).filter(
    or_(Country.name.like('%uador%'), Country.capital.like('%ito%'))
).all()
for c in paises_filtrados:
    print(c.name, " | ", c.capital)
