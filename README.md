# Disease Detection by Chest X-ray 

This project was created using Django as the backend and normal HTML/CSS for the front end.

## To classify disease

For the actual diagnosis, We custom train the model by using the VGG16 (Convolutional Neural Network that has 16 deep layers) model with some additional layers to get better accuracy. Basically, our model can only classify either X-ray affected by Opacity disease or Normal X-ray.

## Usage

The user/Doctor has to enter a chest X-ray image and our model will predict whether it is opacity or normal. If the user enters an image other than a chest X-ray, the model will refuse and prompt the user to enter a valid X-ray image.

For this kind of validation, we use a Qdrant vector database. The Qdrant vector database contains pre-processed chest X-ray images that are used to validate the user's input. If the user enters an image that is not a chest X-ray, the model compares the input image with the images in the quadrant vector database to determine if it is a valid chest X-ray image.

## Installation

To install and run this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Dr_X_ray.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Dr_X_ray
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Open your web browser and visit `http://localhost:8000` to access the project.

## Usage

Once the project is running, you can use it by following these steps:

1. Open your web browser and visit `http://localhost:8000`.

2. Upload a chest x-ray image using the provided form.

3. Click on the "Predict" button to submit the image.

4. The model will process the image and display the prediction result, indicating whether the image is classified as opacity or normal.

Note: Make sure to only upload chest X-ray images for accurate predictions.


## To use the Qdrant vector database

To classify whether an image is X-ray or not, we're using Qdrant Vector DB. To know more about Qdrant Vector Database, refer to https://qdrant.tech/documentation/. For our project, do the following steps:

1. Install Docker and inside Docker pull the Qdrant docker image from Docker Hub by using the `docker pull qdrant/qdrant` command.

2. Run the Qdrant docker image on port 6333 by using the `docker run -dp 6333:6333 qdrant/qdrant` command.

3. Collect 100 to 200 X-ray images and run our test.py file to create a collection and insert records into the collection.

4. Now, your Vector Database is ready to use. Enjoy! 

Note 1: Whenever you try to add data in Qdrant or use data from Qdrant DB, If you face any error, please check the proper collection name or port on which your Qdrant docker image is running.

Note 2: If you're storing your collection on Local Qdrant then whenever you restart your system or restart your project, you have to repeat step number 1 to add data in Qdrant DB.
