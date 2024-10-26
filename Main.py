from llama3_2B import llama_model
from Image_preprocessing import preprocessing
from Text_Extraction import Text_Extractor
import gdown
import pandas as pd
from Database_Information_Retrival import retrive_names


model = 'llama3.2'
image_path = "Dataset\TestImg.jpg"
# file_id = "1xVMgkoCgi0jLEQR182-Qkfn1J9TzOKKy"
# url = f"https://drive.google.com/uc?id={file_id}"
# output = "medicinedata.csv"  
# gdown.download(url, output, quiet=False)
interactive_prompt = "      <Create an engaging and easy-to-understand description for a medicine,including its name, potential substitutes, key uses and benefits, possible side effects and precautions. Also, indicate whether the medicine is habit-forming or safe for general use, and include any relevant expiry information. Make sure to use simple language that avoids complex medical terminology so that customers who may not be familiar with medical concepts can easily grasp the essential details.>"


if __name__=='__main__':

    # image preprocessing
    preprocessed_image_path = preprocessing(image_path)

    # Extracting the text from the image
    text = Text_Extractor(preprocessed_image_path)

    text = text + "               < Please identify only the medicine name from this text. >"

    # Sending the text to the language model
    medicine_name = llama_model(text, model)

    medicine_information = retrive_names(medicine_name)
    medicine_info_str = medicine_information.to_string(index=False)


    medicine_info_str = medicine_info_str +    "      <Create an engaging and easy-to-understand description for a medicine,including its name, potential substitutes, key uses and benefits, possible side effects and precautions. Also, indicate whether the medicine is habit-forming or safe for general use, and include any relevant expiry information. Make sure to use simple language that avoids complex medical terminology so that customers who may not be familiar with medical concepts can easily grasp the essential details.>"

    print(medicine_info_str)

    final_medicine_data = llama_model(medicine_info_str, model)

    print()
    print()
    print()
    print()
    print(medicine_information)




