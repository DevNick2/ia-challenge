from agno.db.postgres import PostgresDb
from utils.environment import environment

db_host = environment.get('DATABASE_HOST')
db_user = environment.get('DATABASE_USER')
db_port = environment.get('DATABASE_PORT')
db_name = environment.get('DATABASE_DB')
db_password = environment.get('DATABASE_PASSWORD')

connection = PostgresDb(
  db_url=f'postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}',
  memory_table='agent_image_generator_memory'
)