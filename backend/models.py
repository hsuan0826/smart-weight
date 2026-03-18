from sqlalchemy import Column, Integer, String, Float, Date, DateTime,ForeignKey
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,
                     primary_key = True,
                     index = True
                     )
    
    email = Column(String,
                   unique = True,
                   nullable = False)
    gender = Column(String)
    password_hash = Column(String(60), 
                           nullable = False)
    
    first_name = Column(String)

    last_name = Column(String)

    dob = Column(Date, 
                 nullable = False)
    
    initial_wt = Column(Float,
                  nullable = False)

    target_wt = Column(Float)
    height = Column(Float)
    created_at = Column(DateTime,
                        nullable = False, 
                        server_default = func.now()
                        )
    
class WeightLog(Base):
    __tablename__ = "weight_log"
    log_id = Column(Integer,
                    primary_key = True,
                    unique = True
                    )
    weight = Column(Float,
                    nullable = False)
    time_of_day = Column(String, nullable = False
                         )
    user_id = Column(Integer,ForeignKey("users.user_id"),nullable = False)

    date =  Column(Date, 
                 nullable = False)
    logged_at = Column(DateTime,
                        nullable = False, 
                        server_default = func.now()
                        )