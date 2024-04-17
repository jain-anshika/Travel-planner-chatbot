import streamlit as st
from openai import OpenAI

api_key = "sk-proj-mFS5RTWRQi3ilvYnUYAnT3BlbkFJ1CDVKFlTvH8u7wtJ3i0O"

client = OpenAI(api_key=api_key)

def generate_itinerary(destination, budget, num_days):
    prompt = f"User is planning a trip from their current location to {destination} with a budget of {budget} and plans to stay for {num_days} days. Generate a personalized itinerary based on these details."

    response = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt
    )
    itinerary = response.choices[0].text.strip()
    
    return itinerary

def main():
    st.title("Travel Activity Planner")

    destination = st.text_input("Destination", "")
    budget = st.number_input("Budget", min_value=0, step=100, value=1000)
    num_days = st.number_input("Number of Days", min_value=1, step=1, value=3)

    if st.button("Generate Itinerary"):
        if destination:
            itinerary = generate_itinerary(destination, budget, num_days)
            st.subheader("Generated Itinerary:")
            st.write(itinerary)
        else:
            st.error("Please enter a destination.")

if __name__ == "__main__":
    main()
