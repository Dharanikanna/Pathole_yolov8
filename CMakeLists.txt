cmake_minimum_required(VERSION 3.0)
project(YOLO_CPP)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Find OpenCV
set(OpenCV_DIR "D:/opencv/opencv/build_d/") # Path to OpenCV build directory
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Find LibTorch
set(Torch_DIR "D:/libtorch/torch") # Path to LibTorch cmake directory
find_package(Torch REQUIRED)

# Add an executable target
add_executable(${PROJECT_NAME} detection.cpp)

# Link the executable target with OpenCV and LibTorch
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS} ${TORCH_LIBRARIES})
