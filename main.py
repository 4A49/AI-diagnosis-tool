import openai
import time

# Replace this with your own API key
openai.api_key = "YOUR_API_KEY"

# The name of the OpenAI model to use
model_engine = "text-davinci-002"

# A cache of previous API responses, mapping from prompts to generated diagnoses
diagnosis_cache = {}

# The minimum amount of time (in seconds) to wait between API requests
throttle_time = 1

# The current time (used for throttling)
current_time = time.time()

while True:
    # Prompt the user for their age, symptoms, duration of symptoms, and underlying medical conditions
    gender = input("What is your gender: ")
    age = input("Please enter your age: ")
    symptoms = input("Please enter your symptoms: ")
    duration = input("Please enter the duration of your symptoms: ")
    conditions = input("Please enter any underlying medical conditions: ")

    # Use the user's input to create a prompt for the OpenAI API
    prompt = (f"Please provide a medical diagnosis based on the following information: "
             f"age={age}, gender={gender}, symptoms={symptoms}, duration={duration}, underlying medical conditions={conditions}. "
             f"In addition, please provide information on possible causes of the diagnosis and suggested treatment options or medications.")

    # Check the cache for a previous response to this prompt
    if prompt in diagnosis_cache:
        # If a previous response is found, use it
        diagnosis = diagnosis_cache[prompt]
    else:
        # If no previous response is found, use the OpenAI API to generate a new one

        # Throttle the API request if necessary
        elapsed_time = time.time() - current_time
        if elapsed_time < throttle_time:
            time.sleep(throttle_time - elapsed_time)

        # Make the API request
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Get the generated diagnosis from the API response
        diagnosis = completions.choices[0].text

        # Update the cache with the new response
        diagnosis_cache[prompt] = diagnosis

        # Update the current time
        current_time = time.time()

    # Print the diagnosis
    print(diagnosis)
    exit = input("Do you want to exit?(type 'yes' to quit or No to continue): ")
    if exit == 'yes':
        break
