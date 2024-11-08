from my_module import generate_recipe
from transformers import T5ForConditionalGeneration, T5Tokenizer
import streamlit as st

# Load the model and tokenizer
model_name = "google/flan-t5-large"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Define the function to generate a recipe
def generate_recipe(ingredients):
    ingredients_text = ", ".join(ingredients)
    prompt = f"Create a recipe using these ingredients: {ingredients_text}."
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=150, num_beams=5, early_stopping=True)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return recipe

# Streamlit app code
st.title("Recipe Generator")
ingredients = st.text_input("Enter ingredients (comma-separated):")
if st.button("Generate Recipe"):
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    recipe = generate_recipe(ingredients_list)
    st.write("### Your Recipe:")
    st.write(recipe)

