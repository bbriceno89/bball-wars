#from sqlalchemy import create_engine, ForeignKey ,Column, String, Integer, CHAR
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

#Base = declarative_base()

#class Person(Base):
   # __tablename__ = "people"

    #account = Column("account", Integer, primary_key=True)
    #firstname = Column("firstname", String)
    #lastname = Column("lastname", String)
    #gender = Column("gender", CHAR)
    #age = Column("age", Integer) 

    #def __init__(self ,account, first, last, gender, age):
       # self.account = account
      #  self.firstname = first
     #   self.lastname = last 
    #    self.gender = gender
   #     self.age = age

  #  def __repr__(self):
 #       return f"({self.account}) {self.firstname} {self.lastname} {self.gender} {self.age})"
    


#class Rental(Base):
    #__tablename__ = "rentals"

    #rid = Column("rid", Integer, primary_key=True)
    #movie = Column("movie", String )
    #renter = Column(String, ForeignKey("people.firstname"))

   # def __init__(self, rid, title, renter):
       # self.rid = rid
      #  self.title = title
     #   self.renter = renter

 #   def __repr__(self):
  #      return f"({self.rid}) {self.title} rented by {self.renter}"
    



#engine = create_engine("sqlite:///mydb.db", echo=True)
#Base.metadata.create_all(bind=engine)

#Session = sessionmaker(bind=engine)
#session = Session()

#person = Person(1122, "Beau", "Briceno", "m", 33)

#session.add(person)
#session.commit()

#p1 = Person(1234, "Laine", "Briceno", "f", 32)
#p2 = Person(1543, "Luna", "Briceno", "f", 9)
#p3 = Person(1134, "Deano", "Briceno", "m", 7)

#session.add(p1)
#session.add(p2)
#session.add(p3)
#session.commit()

#rental = Rental(1, "Star Wars", "")

#session.add(rental)
#session.commit()

