import streamlit as st
import time
import subprocess


def set_background_color():
    st.markdown(
        f"""
        <style>
        html, body, [data-testid="stAppViewContainer"] {{
            background: linear-gradient(135deg,#2ecc71,#ffffff);
            height: 100vh;#VIEWPORT HEIGHT
            background-attachment: fixed;#IT IS FIXED DURING SCROLLING
        }}
        header,footer {{
            visibility: hidden;#REMOVE THE HEADER AND FOOTER
        }}
        .button_styles_bubble, .button_styles_selection, .button_styles_insertion, .button_styles, .button_styles_graphs, .button_styles_optimized_graphs {{
            font-size: 20px;
            border-radius: 5px;
            text-align: center;
            display: inline-block;#controls the possible spacing here and makes sure that the texts are aligned
            cursor: pointer;#typically indicating that an elemnt is clickable
            box-shadow: 0 0 5px rgba(52, 152, 219, 0.5); 
        }}#BUTTON PROPERTIES
        .button_styles_bubble:hover,
        .button_styles_selection:hover,
        .button_styles_insertion:hover,
        .button_styles:hover,
        .button_styles_graphs:hover,
        .button_styles_optimized_graphs:hover {{
                background:#0000FF
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Sorting algorithms implementation
def bubble_sort(arr):
    n = len(arr)
    is_sorted = True  # boolean variable
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return arr, is_sorted
    return arr, is_sorted


def selection_sort(arr):
    n = len(arr)
    is_sorted = True  # boolean variable
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                is_sorted = False
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if is_sorted:
            return arr, is_sorted
    return arr, is_sorted  # for false


def insertion_sort(arr):
    n = len(arr)
    is_sorted = True
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            is_sorted = False
        arr[j + 1] = key
        if is_sorted:
            return arr, is_sorted
    return arr, is_sorted


# Main Streamlit application
def main():
    set_background_color()  # backgroung color
    st.title("Sorting Algorithms")  # title display

    uploaded_file = st.file_uploader(
        "Choose a file to read the array:", type=["txt"]
    )  # Accesses the folder
    if uploaded_file is not None:
        contents = uploaded_file.read().decode("utf-8").split()
        array = [int(x) for x in contents]
        st.write("File read successfully!")
    else:
        array = []  # empty array

    result_text = ""  # Initialize result_text to prevent UnboundLocalError

    if array:
        if st.button("Bubble Sort", key="button_styles_bubble"):
            start_time = time.perf_counter()  # gives more precise time
            sorted_arr, is_sorted = bubble_sort(array.copy())  # passing the array
            end_time = time.perf_counter()  # winding up
            time_taken = end_time - start_time
            if is_sorted:  # True
                result_text += f"The array was already sorted:{sorted_arr}\n"
            else:
                result_text = f"The sorted array is: {sorted_arr}\n"
            result_text += f"Time taken by Bubble Sort: {time_taken:.6f} seconds"
            st.text(result_text)

        if st.button("Selection Sort", key="button_styles_selection"):
            start_time = time.perf_counter()
            sorted_arr, is_sorted = selection_sort(array.copy())
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            if is_sorted:
                result_text += f"The array was already sorted:{sorted_arr}\n"
            else:
                result_text = f"The sorted array is: {sorted_arr}\n"
            result_text += f"Time taken by Selection Sort: {time_taken:.6f} seconds"
            st.text(result_text)

        if st.button("Insertion Sort", key="button_styles_insertion"):
            start_time = time.perf_counter()
            sorted_arr, is_sorted = insertion_sort(array.copy())
            end_time = time.perf_counter()
            time_taken = end_time - start_time
            if is_sorted:
                result_text += f"The array was already sorted:{sorted_arr}\n"
            else:
                result_text = f"The sorted array is: {sorted_arr}\n"
            result_text += f"Time taken by Insertion Sort: {time_taken:.6f} seconds"
            st.text(result_text)

        if st.button("View time taken by all methods", key="button_styles"):
            start_time1 = time.perf_counter()
            _, is_sorted1 = bubble_sort(array.copy())  # we do not need the array
            end_time1 = time.perf_counter()
            time1 = end_time1 - start_time1

            start_time2 = time.perf_counter()
            _, is_sorted2 = selection_sort(array.copy())
            end_time2 = time.perf_counter()
            time2 = end_time2 - start_time2

            start_time3 = time.perf_counter()  # it will give you even more precise time
            _, is_sorted3 = insertion_sort(array.copy())
            end_time3 = time.perf_counter()
            time3 = end_time3 - start_time3

            result_text = "Summary of time taken by each sorting technique:\n"
            result_text += f"Bubble Sort: {time1:.6f} seconds\n"
            result_text += f"Selection Sort: {time2:.6f} seconds\n"
            result_text += f"Insertion Sort: {time3:.6f} seconds\n"
            st.text(result_text)

        if st.button("Graph for 3 sorting methods", key="button_styles_graphs"):
            script_path = r"C:\Users\Ananya\OneDrive\Desktop\ADA\testing1.py"  # The file which I want to execute
            streamlit_path = r"C:\Users\Ananya\AppData\Roaming\Python\Python311\Scripts\streamlit.exe"  # Path of the streamlit server
            subprocess.Popen([streamlit_path, "run", script_path])

        if st.button("Optimized graph", key="button_styles_optimized_graphs"):
            script_path = r"C:\Users\Ananya\OneDrive\Desktop\ADA\testing.py"  # The file which I want to execute
            streamlit_path = r"C:\Users\Ananya\AppData\Roaming\Python\Python311\Scripts\streamlit.exe"  # Path of the streamlit server
            subprocess.Popen([streamlit_path, "run", script_path])


if __name__ == "__main__":  # incase it gets imported it will not run
    main()
