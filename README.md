# han-character-ml
Repository to create han character ML

# Content
- Used model
- Instalation
- Input and Output

# Used Model
## CNN (Convolutional Neural Network)

# Instalation
## Download Kanji image dataset (non-commercial propose):
Link: http://etlcdb.db.aist.go.jp/
- Register on the ETL page to gain access to the dataset
- Clone etl extractor: https://github.com/choo/etlcdb-image-extractor
- With the extractor, extract ETL8G

## Script execution order:
- Filter hiragana character and compressed the image dataset to a compressed numpy file (npz)
```
python read_kanji.py
```
- Generate npz training/testing data
```
python generate_training_data.py
```
- (Optional) Visualize training or testing data set
```
python visualize_kanji.py
```
- Train model
```
python kanji_CNN.py
```
- (Optional) Check model summary and accuracy
```
python kanji_CNN_summary.py
```

# Input and Output
## Input data
The ML model requires an image wiht a format of 48x48 and color black kanji as an entry parameter
```
input_shape: (48, 48, 1)
48 - Width
48 - Height
1 - Color channel
```
![Sample 1](sample_images/sample1.png) ![Sample 2](sample_images/sample2.png)

## Output data
The ML model after proccessing the data it's return and array of porcentages for every character (879)
```
input_shape: (879,)
```
