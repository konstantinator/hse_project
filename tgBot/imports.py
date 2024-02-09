import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import nltk
import joblib
from collections import Counter

nltk.download('stopwords')
from pandarallel import pandarallel
import re
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords
pd.set_option('max_colwidth', None)
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from scipy.sparse import hstack
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import warnings
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

# Импорты для тг бота
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram import html
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import default_state
import emoji
import aiofiles