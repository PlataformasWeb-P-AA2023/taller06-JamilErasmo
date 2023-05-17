from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://invitado:UTPLUTPL@localhost:5432/countries", echo=True)

