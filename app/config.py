import os
from dotenv import load_dotenv


load_dotenv()

DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")
DB_HOST=os.environ.get("DB_HOST")
DB_NAME=os.environ.get("DB_NAME")
DB_SSL=os.environ.get("NIX_SSL_CERT_FILE")
SECRET_K=os.environ.get("SECRET_K")
DB_PORT=os.environ.get("DB_PORT")





class Config:
    #?ssl_ca={DB_SSL}
    SECRET_KEY=f"{SECRET_K}"
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    

    SQLALCHEMY_TRACK_MODIFICATIONS=True
    
