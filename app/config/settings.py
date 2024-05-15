import google.generativeai as gem
from .local_settings import API_KEY


gem.configure(api_key=API_KEY)
model = gem.GenerativeModel('gemini-pro')