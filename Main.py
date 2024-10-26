from llama3_2B import llama_model
from Image_preprocessing import preprocessing
from Text_Extraction import Text_Extractor


model = 'llama3.2'
image_path = "Dataset\TestImg.jpg"
text = "top 5 cities" + "just give the name of the city"


if __name__=='__main__':

    # image preprocessing
    preprocessed_image_path = preprocessing(image_path)

    # Extracting the text from the image
    text = Text_Extractor(preprocessed_image_path)

    text = text + "               < Please identify only the medicine name from this text. >"

    # Sending the text to the language model
    llama_model(text, model)


