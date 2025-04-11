import base64
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def number_detect(file_name):
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    client = genai.Client(
        api_key=GEMINI_API_KEY,
    )
    # Use absolute path to the image file
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                             "assets", "images", "photo_2025-04-10_10-44-28.jpg")
    files = [
        client.files.upload(file=image_path),
    ]
    files_param = [
        client.files.upload(file=file_name),
    ]
    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
                types.Part.from_text(text="""Nhận diện tất cả số màu đỏ và vị trí của nó
chỉ trả về kết quả có tại row, col và value
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""[
  {\"row\": \"0\", \"col\": \"0\", \"value\": \"6.2\"},
  {\"row\": \"0\", \"col\": \"1\", \"value\": \"16\"},
  {\"row\": \"0\", \"col\": \"2\", \"value\": \"19\"},
  {\"row\": \"1\", \"col\": \"0\", \"value\": \"5.2\"},
  {\"row\": \"1\", \"col\": \"1\", \"value\": \"7\"},
  {\"row\": \"1\", \"col\": \"2\", \"value\": \"45\"},
  {\"row\": \"2\", \"col\": \"0\", \"value\": \"5.3\"},
  {\"row\": \"2\", \"col\": \"1\", \"value\": \"10\"},
  {\"row\": \"2\", \"col\": \"2\", \"value\": \"15\"},
  {\"row\": \"3\", \"col\": \"0\", \"value\": \"6\"},
  {\"row\": \"3\", \"col\": \"1\", \"value\": \"39\"},
  {\"row\": \"3\", \"col\": \"2\", \"value\": \"130\"},
  {\"row\": \"4\", \"col\": \"0\", \"value\": \"5.5\"},
  {\"row\": \"4\", \"col\": \"1\", \"value\": \"150\"},
  {\"row\": \"4\", \"col\": \"2\", \"value\": \"49\"},
  {\"row\": \"5\", \"col\": \"0\", \"value\": \"12\"},
  {\"row\": \"5\", \"col\": \"2\", \"value\": \"36\"},
  {\"row\": \"6\", \"col\": \"0\", \"value\": \"7\"},
  {\"row\": \"6\", \"col\": \"2\", \"value\": \"178\"},
  {\"row\": \"7\", \"col\": \"0\", \"value\": \"7\"},
  {\"row\": \"7\", \"col\": \"2\", \"value\": \"138\"},
  {\"row\": \"8\", \"col\": \"0\", \"value\": \"17\"},
  {\"row\": \"8\", \"col\": \"2\", \"value\": \"130\"},
  {\"row\": \"9\", \"col\": \"0\", \"value\": \"57\"},
  {\"row\": \"9\", \"col\": \"2\", \"value\": \"138\"}
]"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
               types.Part.from_uri(
                    file_uri=files_param[0].uri,
                    mime_type=files_param[0].mime_type,
                ),
                types.Part.from_text(text=""""""),
            ],
        ),
    ]
    # generate_content_config = types.GenerateContentConfig(
    #     response_mime_type="application/json",
    # )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        # config=generate_content_config,
    )
    return response.text

