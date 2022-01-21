import json

dictionary = {
    "dataset_url": input("Enter Dataset URL: "),
    "data_dir": input("Enter Data Directory Name: "),
    "batch_size": int(input("Enter Batch Size: ")),
    "img_height": int(input("Enter Image Height: ")),
    "img_width": int(input("Enter Image Width: ")),
    "epochs": int(input("Enter Number of Epochs: ")),
    "test_url": input("Enter Test Image URL: "),
    "test_name": input("Enter Test Image Name: ")
}

# Serializing json
json_object = json.dumps(dictionary, indnt=4)

# Writing to sample.json
with open("gen.json", "w") as outfile:
    outfile.write(json_object)