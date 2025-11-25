from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt



def preprocessing_image(input_img, desired_width, output_img, contrast_factor):

    """
    Resize image to desired width (maintaining aspect ratio), convert to grayscale,
    normalize pixel values to [0,1], and optionally adjust contrast.
    
    Returns:
        image_normalized: 2D numpy array of normalized grayscale pixels
    """
    img = Image.open(input_img)

    #compute the height to maintain aspect ratio. 
    # Keeping the image proportional without strecthing
    wpercent = (desired_width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))   

    #Lanczos filter for high-quality downsampling
    img = img.resize((desired_width,hsize), Image.LANCZOS)
    img = img.convert('L') # convert to grayscale l - luminance Channel

    img.save(output_img)
    # Convert image to numpy array for further processing
    img_array = np.array(img)

    # Normalize pixel values to [0, 1]
    img_normalized = img_array / 255.0 

    #Enhances contrast to make dark/light regions more pronounced.
    image_normalized = np.clip(0.5 + contrast_factor * (img_normalized - 0.5), 0, 1)

    plt.imshow(image_normalized, cmap='gray')
    plt.title('Preprocessed Image')
    plt.axis('off')
    plt.show()

    return image_normalized

input_image_path = "../samples/rush.jpg"
desired_width = 400
output_image_path = "../outputs/resize_rush.jpg"

if os.path.exists(input_image_path):
    preprocessing_image(input_image_path, desired_width, output_image_path, contrast_factor=1.2)
    print(f"Image resized and saved to {output_image_path}")
else:
    print(f"Input image not found at {input_image_path}")