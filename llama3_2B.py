import subprocess

def run_ollama_model(model_name, input_text):
    # Pull the model
    try:
        print(f"Pulling model: {model_name}...")
        subprocess.run(['ollama', 'pull', model_name], check=True)
        print("Model pulled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error pulling model: {e}")
        return None

    # Run the model
    try:
        print(f"Running model: {model_name}...")
        # Run the model and capture output
        result = subprocess.run(['ollama', 'run', model_name],
                                input=input_text,
                                text=True,
                                capture_output=True,
                                check=True)

        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error running model: {e}")
        return None



def llama_model(text,model):
    output = run_ollama_model(model, text)
    
    if output:
        print("Model Output:")
        print(output)
