## Requirements

To run the Streamlit app, you'll need to have Python and the necessary libraries installed. You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository:

```bash
git clone https://github.com/Inti06/data_tools_submission.git
cd data_tools_submission
```

2. Install the required packages as mentioned in the "Requirements" section.

3. Run the Streamlit app:

```bash
streamlit run uber_pickups.py
```

The app will launch in your default web browser, and you can start using it.

### OR

1. Build a Docker image

```bash
docker build -t image_name .
```

2. Run the image:

```bash
docker run -p 8501:8501 image_name
```

3. type http://0.0.0.0:8501 or http://localhost:8501 in your browser to start using the app!