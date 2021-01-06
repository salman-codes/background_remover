# How to use.

1. You'll need a `model` folder.
2. `model` folder contanins the Machine Learning models for object detection, masking and segmentation.
3. Download the `model.zip` file from `https://drive.google.com/file/d/1ytUOp9Pqi7riI8m_coKfc9m7ZPwIwlvW/view?usp=sharing`, and extract the contents in root directory of the application (same level as manage.py)
4. Simply run `python3 manage.py runserver`
5. Visit `http:://localhost:8000`, upload the image, a cliackable link will be generated.
6. The link will contain the new processes image.
7. The processed and downloaded images both will be available in `uploads` directory.