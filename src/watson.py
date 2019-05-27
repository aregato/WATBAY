#Watson Module: Anropar Visual recognition från IBM Watson
from watson_developer_cloud import VisualRecognitionV3
#Watson API;key+ version
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='5daede11f0f6d3120c164a88c059acf2914fe051')

def classify():
    '''
    Öppnar lagrad bild
    Anropar Watson med bild
    Retunerar resultat i format dictionary
    '''
    picture = open('src/picture.jpg','rb')
    watson_result = visual_recognition.classify(images_file=picture)
    return watson_result

def get_name(watson_result, item_nr):
    '''
    Hämtar namn från Watsons resultat
    Retunerar en string
    '''
    name = watson_result['images'][0]['classifiers'][0]['classes'][item_nr]['class']
    return name

def get_score(watson_result, item_nr):
    '''
    Hämtar träffsäkerheten från Watsons resultat
    Omvandlar det till procent
    Returnerar en av rundad int 
    '''
    score = watson_result['images'][0]['classifiers'][0]['classes'][item_nr]['score']
    score = score * 100
    return round(score)
    
