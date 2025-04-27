s
import os

def convert_images_to_pdf(input_folder):
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    images = []
    
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        images.append(image.convert('RGB'))

    pdf_filename = os.getenv('PDF_NAME', 'output.pdf')
    output_pdf_path = os.path.join(output_folder, pdf_filename)

    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF successfully created: {output_pdf_path}")
    else:
        print("No images found in the folder.")

if len(sys.argv) > 1:
    convert_images_to_pdf(sys.argv[1])
else:
    print("Please provide the image folder name as a parameter.")

