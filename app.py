from ultralytics import YOLO
import streamlit as st
import skimage
model = YOLO('model.pt')

new_class_names = ['Pas dla autobusów', 'Żółte oznaczenie', 'Linia 1', 'Linia 2',
                   'Przejście dla pieszych', 'Romboid', 'Zwolnij', 'Strzałka w lewo',
                   'Strzałka do przodu', 'Strzałka do przodu i w lewo',
                   'Strzałka do przodu i w prawo', 'Strzałka w prawo', 'Rower']








st.title("Recognition of Road Surface Signs")

uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
if uploaded_file is not None:
    image=skimage.io.imread(uploaded_file)
    results = model(image)  # Replace with the path to your test image
    # Update class names in the results
    for result in results:
        # Map old class IDs to new class names
        result.names = {i: name for i, name in enumerate(new_class_names)}
        print(result.names)  # Verify the updated names
    result = results[0]
    img_with_detections = result.plot()
    st.image(img_with_detections)
    # print(type(result))
    # st.image(result)
    # result.show()  # Show predictions
    # result.save()  # Save the predictions

