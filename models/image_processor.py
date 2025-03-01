from PIL import Image, ImageDraw, ImageFont
import os

def generate_poster(image_path, text):
    # Create output directory if not exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    
    # Open base image
    base_image = Image.open(image_path).convert("RGBA")
    
    # Create text layer
    txt_layer = Image.new('RGBA', base_image.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt_layer)
    
    # Configure font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # Add text to image
    draw.text((50, 50), text, fill=(255,255,255,255), font=font)
    
    # Combine layers
    combined = Image.alpha_composite(base_image, txt_layer)
    
    # Save result
    output_path = f"static/posters/{os.path.basename(image_path)}"
    combined.save(output_path)
    
    return output_path
