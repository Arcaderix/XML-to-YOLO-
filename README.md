
# XML to YOLO Format Conversion and Image Resizing

This script converts XML annotations in PASCAL VOC format to YOLO format and resizes the associated images to a standard size (default 640x640). It is useful for object detection projects using machine learning models.

## Requirements

- Python 3.x
- Required libraries:
  - `xml.etree.ElementTree`
  - `Pillow` (PIL)
  - `tqdm` (for progress bar)

You can install the necessary libraries using `pip`:

```bash
pip install Pillow tqdm
```

## Project Structure

This script is designed to process XML files and their corresponding images. The image format should be JPG, but you can adjust the code if you're using a different image format.

```
- train/
  - file1.xml
  - file1.jpg
  - file2.xml
  - file2.jpg
- New folder/  # Output folder where converted files will be saved
```

## Functions

### 1. `convert_xml_to_yolo_format(xml_file, img_width, img_height)`

Converts a PASCAL VOC XML file to YOLO format. The output is a `.txt` file with image annotations.

#### Input:
- `xml_file`: Path to the XML file containing annotations.
- `img_width`, `img_height`: Dimensions of the image.

#### Output:
- Returns a list of lines in YOLO format.

### 2. `convert_and_resize_image(img_path, output_folder, target_size=(640, 640))`

Resizes images to a standard size (default 640x640) and saves them to the output folder.

#### Input:
- `img_path`: Path to the original image.
- `output_folder`: Folder where the resized image will be saved.
- `target_size`: Size to which the image will be resized.

#### Output:
- Saves the resized image in the output folder.

### 3. `convert_all_xml_in_folder(xml_folder, image_folder, output_folder, target_size=(640, 640))`

Converts all XML files in the input folder to YOLO format, resizes the images, and saves both the resized images and `.txt` files in the output folder.

#### Input:
- `xml_folder`: Folder containing the XML files.
- `image_folder`: Folder containing the images.
- `output_folder`: Folder where the output files will be saved.
- `target_size`: Size of the resized images.

#### Output:
- YOLO `.txt` annotation files and resized images.

## Usage

### Step 1: Set up the paths

Make sure to correctly configure the paths for the XML files and images, as well as the output folder. For example:

```python
xml_folder = "C:/Users/ARCA/Downloads/death.v1i.yolokeras/train"  # Folder with your XML files
image_folder = "C:/Users/ARCA/Downloads/death.v1i.yolokeras/train"  # Folder with your images
output_folder = "C:/Users/ARCA/Downloads/New folder"  # Folder where the .txt files and resized images will be saved
```

### Step 2: Run the script

Run the following code to convert all XML files and resize the images:

```python
convert_all_xml_in_folder(xml_folder, image_folder, output_folder, target_size=(640, 640))
```

This will generate the `.txt` files in YOLO format and the resized images in the `output_folder`.

## Sample Output

The resulting `.txt` file will have the following format:

```
0 0.432 0.312 0.125 0.234
0 0.654 0.812 0.114 0.217
```

Where:
- The first value is the class ID (in this case, `0`).
- The next values are the normalized coordinates of the bounding box center (x_center, y_center) and the dimensions of the bounding box (width, height).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

