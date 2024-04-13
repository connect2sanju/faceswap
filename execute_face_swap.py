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

    # Run the provided Python script to generate swapped video
    # run_command("python run.py --target roop/data/test_video.mp4 --source roop/data/salman.jpeg -o /roop/data/swapped.mp4 --execution-provider cpu --frame-processor face_swapper face_enhancer")
    
    # Run the provided Python script to generate swapped images
    run_command("python run.py --target roop/data/aamir.jpeg --source roop/data/salman.jpeg -o roop/data/swapped.jpeg --execution-provider cpu --frame-processor face_swapper face_enhancer")

if __name__ == "__main__":
    main()

