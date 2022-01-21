# IoT_Air_Conditioning_Backend
## About Me
This is my IoT Air Conditioning System's backend. Python + Flask backend for BLE indoor positioning. This was created for CZ4171, also because I keep forgetting to turn off my air conditioning when I leave the house :)

### Brief Description
Files in test folder are used for debugging, you may ignore them.

The server is run from main.py. Classifier is implemented in knn_classifier.py. 2 databases are used. statusdatabase.db holds the current status of the aircon and rssidatabase.db holds the latest rssi values from training. rssivalues.csv is a temporary file that holds the values from rssidatabase.db during retraining of the knn_classifier.

Please note that RSSI values may vary from device to device. Using a different android device would most likely require you to retrain the classifier with RSSI values specific to the device that you are using.
