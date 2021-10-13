# Correcting-Image-Orientation

# About the Dataset

<p align ="justify">Here, we will use the Computer Vision and Pattern Recognition challenge dataset given by MIT. The reason we chose this dataset is that in the indoor domain, most scene recognition models that work well for outdoor scenes perform poorly. 

<p align ="justify">67 indoor categories and a total of 15620 images are included in the database. The number of pictures varies across categories, but per category, there are at least 100 pictures. Every picture is in jpg format.The training and testing data are divided into 80 percent and 20 percent. 
  
  ![](http://web.mit.edu/torralba/www/allIndoors.jpg)
  
  # Problem Statement
<p align ="justify">It is easy for us to determine whether or not a natural picture is being rotated. But it may be hard for computers to replicate human output. So, that's our objective of replicating human performance by using Convolutional Neural Network. In this project we are going to pridict rotation angle of a  image [0, 90, 180, 270].


<p align ="justify">The images in the dataset are well organized(rotated). But for our research purpose, we are going to rotate the images at different angles (like 90 degrees). And so that, we can reproduce human performance via the computer.
  
  
  http://pyimg.co/x772x
  
And form there click the “Download” link. The entire .tar archive is 2.4 GB so plan your
download accordingly. Once the file has downloaded, unarchive it. Once unarchived, you’ll find
a directory named Images which contains a number of subdirectories, each one containing a
particular class label in the dataset
  
  To keep the Indoor CVPR dataset organized I created a new directory named indoor_cvpr,
moved the Images directory inside of (changing the uppercase “I” to lowercase “i”), and creating
two new subdirectories – hdf5 and rotated_images. My directory structure for this project is as
follows:
  
--- indoor_cvpr
  
  |     |--- hdf5
  
  |     |--- images
  
  |     |--- rotated_images
  
  The hdf5 directory will store the features extracted from our input images using a pre-trained
Convolutional Neural Network. In order to generate our training data, we will create a custom
Python script that generates randomly rotates images. These rotated images will be stored in
rotated_images. The features extracted from these images will be stored in HDF5 datasets.
  
  # Building Dataset
<p align="justify"> As we have said earlier that, our dataset is well organized. But for our research purpose, our dataset needs to build. For building our dataset we have to rotate our dataset into some different angles purposely. So, that computer can detect and correct the orientation of images properly. And, in here we are going to use Keras.
  
  Before we get started let’s take a look at our project structure:
  
--- image_orientation
  
| |--- creat_dataset.py
  
| |--- extract_features.py
  
| |--- HDF5file/
  
| |--- indoor_cvpr/
  
| |--- models/
  
| |--- orient_images.py
  
| |--- train_model.py
  
  
 ![Screenshot_8](https://user-images.githubusercontent.com/64821137/137177171-aee27fe5-5381-4f9e-adc5-e4dca2964ff6.png)

  
  We’ll be using the create_dataset.py script to build the training and testing sets for our input
dataset. From there extract_features.py will be used to create an HDF5 file for the dataset
splits. Given the extracted features we can use train_model.py to train a Logistic Regression
classifier to recognize image orientations and save the resulting model in the models directory.
Finally, orient_images.py can be applied to orient testing input images.
Just as I have done with the ImageNet dataset, I created a sym-link to indoor_cvpr to make it
easier to type out commands; however, you can ignore this step if you wish and instead specify the
full path to the input/output directories when executing the Python scripts.
Let’s go ahead and learn how we can construct our own custom image orientation dataset
from an existing dataset. Make sure you have downloaded the .tar file from the Indoor Scene
Recognition dataset, and from there, open up a new file, name it create_dataset.py, and we’ll
get it work
  
