import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "sk-proj-mFS5RTWRQi3ilvYnUYAnT3BlbkFJ1CDVKFlTvH8u7wtJ3i0O"

# Function to generate itinerary using OpenAI API
def generate_itinerary(destination, budget, days):
    # Define the prompt
    prompt = f"Generate a {days}-day itinerary for a trip to {destination} with a budget of ${budget}. Include activities, attractions, and places to visit."

    # Generate response using the GPT-3 model
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.5,
        max_tokens=150
    )

    # Extract the generated itinerary from the response
    itinerary = response.choices[0].text.strip()
    
    return itinerary

# Streamlit UI
def main():
    st.title("Travel Activity Planner")

    # Get user inputs
    destination = st.text_input("Enter destination:")
    budget = st.number_input("Enter budget:")
    days = st.number_input("Enter number of days:")

    # Generate itinerary button
    if st.button("Generate Itinerary"):
        if destination and budget and days:
            itinerary = generate_itinerary(destination, budget, days)
            st.success("Here's your itinerary:")
            st.write(itinerary)
        else:
            st.warning("Please fill in all fields.")

if __name__ == "__main__":
    main()
