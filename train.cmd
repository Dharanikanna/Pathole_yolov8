%echo on
call conda.bat activate yolov5
if errorlevel 1 (
    echo "Failed to activate Conda environment."
    exit /b 1
)
echo "Successfully entered to the environment..."
python train.py > log.txt