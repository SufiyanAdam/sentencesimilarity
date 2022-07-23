
from fastapi import FastAPI, Path
from pydantic import BaseModel
import spacy


nlp = spacy.load("en_core_web_lg")
app = FastAPI()

class ResultSimilarity(BaseModel):
    sentence1: str
    sentence2: str

#------------------------------------
#tried to implement using just a function without the BaseModel Class
#@app.post("/predict")
# def comparison(string1: str = Path(None, description="Enter the first sentence"), string2: str = Path(None, description="Enter the second sentence")):
    

#     doc1 = nlp(string1)
#     doc2 = nlp(string2)

 
#     value = doc1.similarity(doc2)
#     resObj = {
#         "similarity" : value
#     }
#     return resObj
#-------------------------------------

@app.post("/predict")
def comparison(object: ResultSimilarity):
    doc1 = nlp(object.sentence1)
    doc2 = nlp(object.sentence2)

    value = doc1.similarity(doc2)

    resObj = {
        "similarity": value
    }
    return resObj