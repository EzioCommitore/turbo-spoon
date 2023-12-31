from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine(
    "postgresql+psycopg2://user:password@localhost/clases", query_cache_size = 1200, echo = True
)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.user, models.user_contact_info, models.user_physical_address
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
