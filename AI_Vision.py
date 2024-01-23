import os
import io
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient


#pip install azure-cognitiveservices-vision-computervision

def get_text_from_image(image_path):
    subscription_key = "567bc7ca129047b1852691ba716c34fb"
    endpoint = "https://computervisionai900.cognitiveservices.azure.com/"

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    local_image = open(image_path, "rb")

    list_text_in_image = []

    recognize_printed_results = computervision_client.recognize_printed_text_in_stream(image = local_image, detect_orientation = True, language="en")
    
    for region in recognize_printed_results.regions:
        for line in region.lines:
            # Each line consists of words
            for word in line.words:
                list_text_in_image.append(word.text)
               
    return list_text_in_image

print(get_text_from_image("C:\\Users\\Hossa\\Downloads\\Compressed\\receipt.jpg"))
