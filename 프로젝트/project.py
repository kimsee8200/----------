import modi_plus as md
import cv2
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import time

# MODI+ 모듈 초기화
bundle = md.MODIPlus()

# MODI+ 모듈 가져오기
led = bundle.leds[0]
display = bundle.displays[0]
speaker = bundle.speakers[0]
motors = bundle.motors  # 모터 모듈을 모두 가져오기
button = bundle.buttons[0]

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("C:/Users/user/Downloads/converted_keras/keras_Model.h5", compile=False)

# Load the labels with the correct encoding
with open("C:/Users/user/Downloads/converted_keras/labels.txt", "r", encoding="utf-8") as f:
    class_names = f.readlines()

# 물질별 RGB 색상 정의 (한국어 이름 사용)
substance_colors = {
    "1 물": (0, 0, 255),           # 파란색
    "2 베이킹소다": (255, 255, 255), # 흰색
    "3 과산화수소": (0, 255, 255), # 노란색
    "0 염산": (255, 0, 0),         # 빨간색
    "4 질산": (0, 255, 0)          # 녹색
}

# 물질별 추가 정보 정의
substance_info = {
    "1 물": "위험도: 매우 낮음, 일반적으로 무해함 특징: 용매로 자주 사용되며, 다양한 실험에서 중요한 역할을 함 주의사항: 전기 실험 시 전도성으로 인해 주의 필요",
    "2 베이킹소다": "위험도: 낮음, 일반적으로 무해함 특징: 산과 반응하여 이산화탄소 발생, 완충제로 사용 주의사항: 과량 사용 시 피부 및 눈 자극",
    "3 과산화수소": "위험도: 중간, 고농도에서는 강한 산화제 혼합 주의: 유기 물질과 혼합하면 폭발 위험, 염소계 화합물과 혼합하면 독성 가스 발생",
    "0 염산": "위험도: 강산, 피부 및 눈에 자극적, 흡입 시 호흡기 자극 혼합 금지 물질: 강염기 (수산화 나트륨), 산화제 (과산화수소) 대응: 보호 장비 착용, 환기 필요",
    "4 질산": "위험도: 강산, 산화제, 피부 및 눈에 심한 화상 유발 혼합 금지 물질: 강염기, 가연성 물질 (알코올 등) 대응: 보호 장비 착용, 적절한 환기 필요"
}

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image
    image = Image.fromarray(rgb_frame)

    # Resize and crop the image to 224x224
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convert the image to a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    if button.clicked:
        print("in")
        for motor in motors:
                motor.speed = 0
        break
    time.sleep(1)
    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name, "Confidence Score:", confidence_score)

    # Check if the detected class is in the substance list
    if class_name in substance_colors:
        # Get the RGB color for the substance
        color = substance_colors[class_name]

        # LED 색상 변경
        led.set_rgb(color[0], color[1], color[2])

        # 물질 정보 출력
        info = substance_info.get(class_name, "물질 정보 없음")
        display.text = f"{class_name}\nConfidence: {confidence_score:.2f}\n{info}"

        # 위험 물질에 대한 추가 경고 (예: 염산, 질산, 과산화수소)
        if class_name in ["0 염산", "4 질산", "3 과산화수소"]:
            # 경고음 재생
            speaker.set_tune(554, 80)
            time.sleep(2)
            count = 1
            # 모든 모터 작동
            for motor in motors:
                if(count == 1):
                  motor.speed = 50
                else:
                  motor.speed = -50
                count = count+1
                    

    else:
        # 감지된 물질이 정의된 리스트에 없을 경우, LED 색상 꺼짐
        led.set_rgb(0, 0, 0)
        display.text = f"알 수 없는 물질\nConfidence: {confidence_score:.2f}"

    # 버튼을 누르면 모든 모터 정지
   

    # Display the resulting frame
    cv2.putText(frame, f"Class: {class_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f"Confidence: {confidence_score:.2f}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Webcam', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
