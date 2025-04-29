import os
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image
from tqdm import tqdm

def convert_xml_to_yolo_format(xml_file, img_width, img_height):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    txt_lines = []

    for obj in root.iter('object'):
        class_name = obj.find('name').text
        class_id = 0

        xml_box = obj.find('bndbox')
        x_min = int(xml_box.find('xmin').text)
        y_min = int(xml_box.find('ymin').text)
        x_max = int(xml_box.find('xmax').text)
        y_max = int(xml_box.find('ymax').text)

        x_center = (x_min + x_max) / 2.0 / img_width
        y_center = (y_min + y_max) / 2.0 / img_height
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        txt_lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

    return txt_lines

def convert_and_resize_image(img_path, output_folder, target_size=(640, 640)):
    img = Image.open(img_path)
    img = img.resize(target_size)
    img_name = os.path.basename(img_path)
    
    img.save(os.path.join(output_folder, img_name))

def convert_all_xml_in_folder(xml_folder, image_folder, output_folder, target_size=(640, 640)):
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith(".xml")]
    for xml_file in tqdm(xml_files, desc="Converting files", unit="file"):
        xml_path = os.path.join(xml_folder, xml_file)
        img_file = xml_file.replace(".xml", ".jpg")
        img_path = os.path.join(image_folder, img_file)

        convert_and_resize_image(img_path, output_folder, target_size)

        img = Image.open(os.path.join(output_folder, img_file))
        img_width, img_height = img.size

        txt_lines = convert_xml_to_yolo_format(xml_path, img_width, img_height)
        txt_file = os.path.join(output_folder, xml_file.replace(".xml", ".txt"))

        with open(txt_file, 'w') as f:
            for line in txt_lines:
                f.write(f"{line}\n")

    print(f"Annotation .txt files and resized images were saved in {output_folder}")

xml_folder = "path/to/your/xml/folder"
image_folder = "path/to/your/image/folder"
output_folder = "path/to/your/output/folder"

convert_all_xml_in_folder(xml_folder, image_folder, output_folder, target_size=(640, 640))
