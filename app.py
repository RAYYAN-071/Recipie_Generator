import streamlit as st

st.title("Recipe Generator")
ingredients = st.text_input("Enter ingredients (comma-separated):")
if st.button("Generate Recipe"):
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]
    recipe = generate_recipe(ingredients_list)
    st.write("### Your Recipe:")
    st.write(recipe)
