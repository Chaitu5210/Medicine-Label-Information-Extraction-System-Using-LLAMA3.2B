from llama3_2B import llama_model
from Image_preprocessing import preprocessing


model = 'llama3.2'
image_path = "Dataset\TestImg.jpg"
text = "top 5 cities" + "just give the name of the city"


if __name__=='__main__':

    # image preprocessing
    image_preprocessing = preprocessing(image_path)

    # Sending the text to the language model
    llama_model(text, model)


