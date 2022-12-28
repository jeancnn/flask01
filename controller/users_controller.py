from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from models.calendar_model import User, Event

from database import engine

def listAllUsers():
    with Session(engine) as session:
        ### The option .options(selectinload(User.events)) has to me used so that the query returns the data instead o "lazy loading" it
        ### if removed the option, you will have to use de data only inside of a session otherwise an error will be trown as lazy load problem.
        statement = select(User).options(selectinload(User.events))
        user = session.exec(statement)
        ### The .all() is used to return the result as an Object, otherwise the return will be shown as a object in the memory. The .first() also can be used to return a single object.
        return user.all()
    
