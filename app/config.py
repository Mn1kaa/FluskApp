import os
from dotenv import load_dotenv


load_dotenv()
os.environ.update(os.environ)
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")
DB_SSL=os.environ.get("DB_SSL")
SECRET_K=os.environ.get("SECRET_K")


path=os.getcwd()




path2=f"{path}\\{DB_SSL}"

print(path2)





class Config:
    SECRET_KEY=f"{SECRET_K}"
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?ssl_ca={path2}"

    SQLALCHEMY_TRACK_MODIFICATIONS=True
    
