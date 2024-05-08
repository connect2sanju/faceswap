import subprocess
import os

def run_command(command):
    """Utility function to run a shell command."""
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        raise

def setup(repo_url):
    # Check if the repository directory exists
    if not os.path.isdir("roop"):
        # Clone the Git repository
        run_command(f"git clone {repo_url}")
        
        # Change directory to the newly cloned repo's directory
        # os.chdir("roop")
    else:
        print("Setup repo already exist!")  
        # Install requirements
        run_command("pip install -r requirements.txt")

        # Download the ONNX model
        run_command("wget https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx -O inswapper_128.onnx")

        # Create a models directory and move the downloaded model file into it
        os.makedirs("models", exist_ok=True)
        os.rename("inswapper_128.onnx", "./models/inswapper_128.onnx")
    
        
def main():
    repo_url = "https://github.com/s0md3v/roop.git"
    setup(repo_url)
    
    source_dir = "roop//data//salman.jpeg" #will be image for image and video swapping
    target_dir = "roop//data//aamir.jpeg" #change to video path for swapped video generation
    output_dir = "roop//data//swapped.jpeg" #change to video path for swapped video generation
    
    # Run the provided Python script to generate swapped image/s/videos
    run_command(f"python run.py --source {source_dir} --target {target_dir} -o {output_dir} --execution-provider cpu --frame-processor face_swapper face_enhancer")

if __name__ == "__main__":
    main()

