# import the necessary packages
# python C:\Users\BA\Downloads\image_orientation/train_model.py --db C:\Users\BA\Downloads\image_orientation/indoor_cvpr/hdf5/orientation_features.hdf5 --model C:\Users\BA\Downloads\image_orientation/models/orientation.cpickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import argparse
import pickle
import h5py

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--db", required=True,
	help="path HDF5 database")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
ap.add_argument("-j", "--jobs", type=int, default=-1,
	help="# of jobs to run when tuning hyperparameters")
args = vars(ap.parse_args())

# open the HDF5 database for reading then determine the index of
# the training and testing split, provided that this data was
# already shuffled *prior* to writing it to disk

db = h5py.File(args["db"], "r")
i = int(db["labels"].shape[0] * 0.75) # 75% training and 25% testing

# define the set of parameters that we want to tune then start a
# grid search where we evaluate our model for each value of C

print("[INFO] tuning hyperparameters...")
params = {"C": [0.01, 0.1, 1.0]}
model = GridSearchCV(LogisticRegression(), params, cv=3,
	n_jobs=args["jobs"])
model.fit(db["features"][:i], db["labels"][:i])
print("[INFO] best hyperparameters: {}".format(model.best_params_))



# serialize the model to disk
print("[INFO] saving model...")
f = open(args["model"], "wb")
f.write(pickle.dumps(model.best_estimator_))
f.close()

# close the database
db.close()