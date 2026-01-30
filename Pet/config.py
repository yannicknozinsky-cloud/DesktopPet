from enum import Enum

# Bewegungsschritte & Geschwindigkeit
STEPSIZE = 2
RUNSTEPSIZE = 4
FALLSPEED = 5
FALLSTEP = 1
RUNSPEED = 10



# Verhalten des Pets
class PetBehavior(Enum):
    REST="rest"
    WALK = "walk"
    GOHOME="home"
    STAY="stay"
    FALLING="falling"
    WAIT="wait"
    TIMER ="timer"
    WECKER="wecker"

class PetDirektion(Enum):
    LEFT = "left"
    RIGTH = "rigth"

# Farben
BLUE = "blue"
GREEN = "green"
PURPLE = "purple"
RED = "red"

import psycopg2

# =========================
# Supabase PostgreSQL Config
# =========================
PG_CONFIG = {
    "host": "db.qkmtybzdthrpjfkbgskw.supabase.co",
    "database": "postgres",
    "user": "postgres",
    "password": "AfFiMaCeL26!",
    "port": 5432,
}

def get_pg_connection():
    """
    Erstellt eine neue Verbindung zur Supabase PostgreSQL DB
    """
    return psycopg2.connect(
        host=PG_CONFIG["host"],
        dbname=PG_CONFIG["database"],
        user=PG_CONFIG["user"],
        password=PG_CONFIG["password"],
        port=PG_CONFIG["port"],
        sslmode="require",      # Supabase braucht SSL
        connect_timeout=10
    )
