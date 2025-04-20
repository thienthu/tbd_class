import pathlib

# path
working_dir = pathlib.Path("C:/Thu/My library/University course/Bioinformatics/1st ay/Machine Learning for Life Sciences/Projec 2/cellular-protein-localization-prediction-challenge/")
# working_dir = pathlib.Path("/content/drive/MyDrive/cellular-protein-localization-prediction-challenge/")
image_dir = pathlib.Path(working_dir/"data/raw_data/train")
train_folder = pathlib.Path(working_dir/"data/train_set")
valid_folder = pathlib.Path(working_dir/"data/valid_set")
test_folder = pathlib.Path(working_dir/"data/raw_data/test")
model_dir = pathlib.Path(working_dir/"model")

#name
model_name = 'res34_fr'

labels = {0: "Mitochondria",
          1: "Nuclear bodies",
          2: "Nucleoli",
          3: "Golgi apparatus",
          4: "Nucleoplasm",
          5: "Nucleoli fibrillar center",
          6: "Cytosol",
          7: "Plasma membrane",
          8: "Centrosome",
          9: "Nuclear speckles"}

#config
N_LABELS = 10
BATCHSIZE = 32 # should change to 32
N_EPOCHS = 100

EARLY_STOP_THRES = 10

pred_threshold = 0.5



