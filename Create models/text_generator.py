from transformers import pipeline
import torch

def generate_sales_copy(input_data, is_image=False):
    # Initialize text generation pipeline
    generator = pipeline('text-generation', 
                        model='gpt2-medium',
                        device=0 if torch.cuda.is_available() else -1)
    
    if is_image:
        # TODO: Integrate image captioning model
        image_caption = "product photography"  # Placeholder
        prompt = f"Generate marketing copy based on this image description: {image_caption}"
    else:
        prompt = f"Generate sales copy using these keywords: {input_data}"
    
    # Generate text
    result = generator(prompt, 
                      max_length=200,
                      num_return_sequences=1,
                      temperature=0.7)
    
    return result[0]['generated_text']
