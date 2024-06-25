import os
import google.generativeai as genai
api_key = "AIzaSyB0DSsK10DRx0TsI-9YTeWVpZzDdccHnaY"
genai.configure(api_key = api_key)


# for m in genai.list_models():
#   print(m.name)

model = genai.GenerativeModel("gemini-pro")
model

respone = model.generate_content("list of top 5 Indian cricketer")
print(respone.text)