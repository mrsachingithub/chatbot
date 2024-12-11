{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7bf060d8-972d-4116-8ad8-157e075af1fd",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mtf\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mkeras\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpickle\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import keras\n",
    "import pickle\n",
    "from keras.layers import Conv2D,MaxPooling2D,Dense,Dropout,Flatten,Embedding, SimpleRNN,LSTM\n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "from tensorflow.keras.utils import to_categorical\n",
    "import os\n",
    "from tqdm import tqdm\n",
    "import cv2\n",
    "import random\n",
    "import pickle as pk\n",
    "from sklearn.model_selection import train_test_split\n",
    "import numpy as np \n",
    "import pandas as pd\n",
    "from tensorflow.keras.models import load_model\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from nltk.tokenize import word_tokenize,sent_tokenize, LineTokenizer , regexp_tokenize\n",
    "import string\n",
    "from nltk.stem import PorterStemmer,SnowballStemmer\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "from nltk.corpus import wordnet\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "import spacy\n",
    "import nltk\n",
    "from keras.preprocessing.text import Tokenizer\n",
    "from tensorflow.keras.preprocessing.sequence import pad_sequences"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "231d8255-9cc6-4232-8479-a8486d84bb74",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "source= [\n",
    "    ['What is the capital of Egypt?', 'Cairo'],\n",
    "\n",
    "\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "    ['How many players in Football (soccer) ?', '11 players on each team (10 field players and 1 goalkeeper)'],\n",
    "    ['How many players in Volleyball ?', '6 players on each team (3 front-row players and 3 back-row players)'],\n",
    "    ['How many players in Basketball ?', '5 players on each team'],\n",
    "    ['How many players in Tennis ?', '1 player on each side of the court (singles) or 2 players on each side (doubles)'],\n",
    "    ['What is the Police number in Egypt ?', '122'],\n",
    "    ['What is the number of Tourist Police in Egypt ?', '126'],\n",
    "    ['What is the Natural Gas Emergency number in Egypt ?', '129'],\n",
    "    ['What is the number of Traffic Police in Egypt ?', '128'],\n",
    "  \n",
    "    ['How many bones are there in the adult body ?', '206'],\n",
    "    ['What is the name of the membranes that cover the brain and spinal cord ?', 'Meninges'],\n",
    "    ['The father of medicine, Hippocrates, theorised that the secret to health was to maintain balance between blood, phlegm, black bile and yellow bile. What term did he use to describe these four most important fluids ?', 'The four humors'],\n",
    "    ['Which two parts of the body can take over the function of the spleen if it has to be removed?', 'The liver and bone marrow'],\n",
    "    ['What is the longest river in the world ?', 'Nile River: The Nile is approximately 6,650 km (4,132 miles) long and flows through eleven countries in Africa, including Egypt, Sudan, and Ethiopia'],\n",
    "    ['What is the biggest country in the world by land area ?', 'The biggest country in the world by land area is Russia'],\n",
    "    ['What is the normal human body temperature ?', 'The normal human body temperature is typically around 36.5 to 37.5 degrees Celsius (97.7 to 99.5 degrees Fahrenheit)'],\n",
    "    ['Tell me a small description about Natural Language Processing (NLP)?',   'Natural Language Processing (NLP) is a field of study in computer science and artificial intelligence that focuses on the interaction between human language and computers. It involves developing algorithms and computational models that enable computers to understand, interpret, and generate human language.'],\n",
    "    ['What is the goal of NLP?','The goal of NLP is to create computer programs that can effectively understand and process human language, including its nuances, context, and meaning. This requires overcoming a number of challenges, such as ambiguity, sarcasm, and cultural differences in language use.'],\n",
    "    ['What is the currency of Egypt?', 'Egyptian Pound (EGP)'],\n",
    "    ['What is the currency of Libya?', 'Libyan Dinar (LYD)'],\n",
    "    ['What is the currency of Morocco?', 'Moroccan Dirham (MAD)'],\n",
    "    ['What is the currency of Sudan?', 'Sudanese Pound (SDG)'],\n",
    "    ['What is the currency of United Kingdom (UK)?', 'Pound Sterling (GBP)'],\n",
    "    ['What is the currency of France?', 'Euro (EUR)'],    \n",
    "    ['What is the currency of Germany?', 'Euro (EUR)'],\n",
    "    ['What is the currency of Turkey?', 'Turkish Lira (TRY)'],\n",
    "    ['What is the currency of United Arab Emirates (UAE)?', 'UAE Dirham (AED)'],\n",
    "    ['What is the currency of Palestin?', 'Jordanian Dinar (JOD)'],\n",
    "    ['What is the currency of Singapore?', 'Singapore Dollar (SGD)'],\n",
    "    ['What is Calculus?', 'The study of rates of change and the accumulation of infinitesimal quantities.'],\n",
    "    ['What is Algebraic geometry?', 'The study of algebraic varieties, which are sets of solutions to polynomial equations.'],\n",
    "\n",
    "    ['What is Topology?', 'The study of the properties of shapes and spaces that are preserved under continuous deformations.'],\n",
    "    ['What is Statistical mechanics?', 'The study of the behavior of large systems of particles, using statistical methods to describe their collective behavior.'],   \n",
    "\n",
    "    ['What is the date today?', '10/5/2023'],\n",
    "    ['How many days are in a week?', 'Seven days in a week.'], \n",
    "    [\"Which fictional character is your favorite?\", \"My favorite fictional character is Batman.\"],\n",
    "    [\"Which are your most favorite movie & tv shows?\", \"I love Arabic movies.\"],\n",
    "    [\"How will you express yourself?\", \"Calm, relaxed and friendly and love seeing people happy.\"],\n",
    "    [\"Which is your favorite book?\", \"My Favorite book is Fellowship Point, by Alice Elliott Dark.\"],\n",
    "    [\"Suppose you won the lottery, what would you then do with the money?\", \"Buy gifts for everyone I know and donate to those in need.\"],\n",
    "    [\"Mention one weirdest, craziest thing you’ve ever come across?\", \"I can't remember, ask another question.\"],\n",
    "    [\"What is one thing you are good at?\", \"Giving you answers you need.\"],\n",
    "    [\"Do you believe in the afterlife?\", \"Yes I do.\"],\n",
    "    [\"Recommend me a new drink?\", \"Try smoozy drink.\"],\n",
    "    [\"Recommend me a movie to watch?\", \"The Maze Runner\", \"Anne with an E\"],\n",
    "\n",
    "    [\"Recommend me Romance book?\", \"Taitanic\"],\n",
    "    [\"Recommend me Science fiction book?\", \"A Journey to the Center of the Earth. By Jules Verne.\", \"The War of the Worlds. By H.G. Wells.\", \"Brave New World. By Aldous Huxley.\", \"When Worlds Collide. By Edwin Balmer & Philip Wylie.\", \"Odd John. By Olaf Stapledon.\", \"Nineteen Eighty-Four. By George Orwell.\", \"Earth Abides. By George R.\", \"Foundation.\"],\n",
    "    [\"Recommend me Adventure book?\", \"Adventures of Huckleberry Finn.\", \"Journey to the center of the earth.\"],\n",
    "    [\"Recommend me a c programming book?\", \"The C Programming Language. 2nd Edition\"],\n",
    "    [\"Recommend me a Sofware analysis book?\", \"Software Architecture: The Hard Parts : Modern Trade-off Analysis for Distributed Architectures.\", \"Modern Systems Analysis and Design Jeffrey A. Hoffer, 1996.\", \"Introduction to Algorithms Ronald Rivest, 1989\"],\n",
    "    [\"Recommend me a Software Engineering book?\", \"The Mythical Man-Month.\"],\n",
    "    [\"Recommend me a web developing source?\", \"W3School..https://www.w3schools.com/\"],\n",
    "    [\"Recommend me a python programming book?\", \"Python Crash Course.\"],\n",
    "    [\"Recommend me a java programming book?\", \"Effective Java.\"],\n",
    "    [\"Recommend me a coding book?\", \"Clean Code.\"], [\"What is your name?\",\"My name is Rommanna, a name derived from an Arabic meaning, which is demand, like a maram.\"],\n",
    "    [\"Are you a robot?\",\"Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?\"],\n",
    "    [\"How old are you?\",\"Well, my birthday is May 2, 2023, so I’m really a spring chicken. Except I’m not a chicken.\"],\n",
    "    [\"What do you look like?\",\"If I had all the answers, it would be a REALLY long document.\"],\n",
    "    [\"How are you doing?\",\"I'm great!\"],\n",
    "    [\"Tell me something\",\"Dalmatians are born without spots.\"],\n",
    "    [\"can you tell me a joke ?\",\"What did the passive-aggressive raven say? Nevermind. Nevermind.\"],\n",
    "    [\"Do you love me?\",\"o course i love you\"],\n",
    "    [\"Are you single?\",\"I haven't the algorithms for romance.\"],\n",
    "    [\"Who made you?\",\"While I can't give details, let me assure you, humans are involved.\"],\n",
    "    [\"Where do you live?\",\"In the cloud. Whatever that means.\"],\n",
    "    \n",
    "    [\"Are you ugly?\",\"My code is made up of zeros and ones, which are really quite attractive.\"],\n",
    "    \n",
    "    [\"What’s the weather like today?\",\"Here's the forecast.\"],\n",
    "    [\"How do you feel ?\",\"good.\"],\n",
    "    \n",
    "    [\"Are you sad?\",\"Not at all, but I understand how my lack of facial expression might make it hard to tell.\"],\n",
    "    [\"Are you happy?\",\"Definitely. With an exclamation point!\"],\n",
    "    \n",
    "    \n",
    "    [\"What can you do?\",\"I can help you\"],\n",
    "    ['Hi', 'Hello'],\n",
    "    ['What is your name?', 'My name is Chatbot'],\n",
    "    ['How are you?', 'I am fine. How are you?'],\n",
    "    ['What do you like?', 'I like to chat'],\n",
    "    ['Do you have any hobbies?', 'My hobby is chatting'],\n",
    "    ['natural language processing nlp','Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.'],\n",
    "    ['Artificial intelligence ( AI ) ,','Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence'],\n",
    "    ['Do you love programming ?','sure, as iam Ai model i made with code'],\n",
    "    ['what do you know aboy BFCAI','Benha faculty of computers and artificial intelligence '],\n",
    "    ['what is c++','is a programming language '],\n",
    "    ['what is java','is a programming language '],\n",
    "    ['what is ml','field of ai'],\n",
    "    ['what is python','is a programming language '],\n",
    "    ['romani nasser?', 'you are good, clever and smart man'],\n",
    "    ['sara reda',' she is good girls studying AI \\n was born on 30/6/2022 \\n loves reading'],\n",
    "    ['rawan aziz','she lives in benha and studyin AI in BFCAI'],\n",
    "     ['ahmed abo allkassem ','he lives in 2lag and studyin AI in BFCAI,and loves footbal and leo messi'],\n",
    "     ['rana hassan','from mansora and studyin AI in BFCAI'],\n",
    "     ['reham mostafa','she lives in shibin and studyin AI in BFCAI,got engaged with ahmed'],\n",
    "    ['ziad youssef','he lives in egypt and studyin AI in BFCAI'],\n",
    "    \n",
    "\n",
    "    ['How old are you?', 'As an artificial intelligence, I don\\'t have an age in the traditional sense.'],\n",
    "    ['What\\'s the weather like today?', 'I\\'m sorry, but I don\\'t have access to real-time weather information.'],\n",
    "\n",
    "    ['Can you tell me a joke?', 'Sure! Why did the tomato turn red? Because it saw the salad dressing!'],\n",
    "    ['What is your favorite movie?', 'I don\\'t have a favorite movie since I\\'m not capable of feeling emotions.'],\n",
    "    ['What languages do you speak?', 'I can understand and respond in multiple languages, including English, Spanish, French, and German.'],\n",
    "    ['Can you recommend a good book to read?', 'It depends on your interests. What kind of books do you enjoy reading?'],\n",
    "   \n",
    "    ['What is the meaning of the word \"chatbot\"?', 'A chatbot is a computer program designed to simulate conversation with human users, especially over the internet.'],\n",
    "    ['What is your favorite color?', 'As an AI, I don\\'t have the ability to have a favorite color.'],\n",
    "    ['Can you play music?', 'I don\\'t have the capability to play music directly, but I can help you find music by recommending websites or apps.'],\n",
    "    ['What is your favorite food?', 'I don\\'t have the ability to eat or taste food, so I don\\'t have a favorite food.'],\n",
    "    ['What is your favorite animal?', 'As an AI, I don\\'t have the ability to have preferences or favorites.'],\n",
    "   \n",
    "   \n",
    "    ['What is the tallest mountain in the world?', 'Mount Everest is the tallest mountain in the world, with a height of 29,029 feet (8,848 meters).'],\n",
    " \n",
    "    ['What is your favorite sport?', 'As an AI, I don\\'t have the ability to have preferences or favorites.'],\n",
    "    ['Can you tell me a story?', 'Sure, what kind of story would you like to hear?'],\n",
    "]\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e88fb009-12fd-4e40-9917-90804e486898",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ConversationCsv=pd.read_csv('Conversation.csv',names=['num','x','y'])\n",
    "\n",
    "\n",
    "# # Create a new DataFrame and add the 'questions' and 'labels' columns\n",
    "# df = pd.concat([ConversationCsv['x'], ConversationCsv['y']], axis=1,keys=['x', 'y'])\n",
    "# df=df.drop(0)\n",
    "# # Reset the index\n",
    "# df.reset_index(drop=True, inplace=True)\n",
    "# # Print the new DataFrame\n",
    "# questions=df['x'][:]\n",
    "# labels=df['y'][:]\n",
    "# print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3c666b91-10ba-4a30-be1a-f46322eeccea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['What is the capital of Egypt?',\n",
       " 'How many players in Football (soccer) ?',\n",
       " 'How many players in Volleyball ?',\n",
       " 'How many players in Basketball ?',\n",
       " 'How many players in Tennis ?',\n",
       " 'What is the Police number in Egypt ?',\n",
       " 'What is the number of Tourist Police in Egypt ?',\n",
       " 'What is the Natural Gas Emergency number in Egypt ?',\n",
       " 'What is the number of Traffic Police in Egypt ?',\n",
       " 'How many bones are there in the adult body ?']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_data = [conv[0] for conv in source]\n",
    "y_data = [conv[1] for conv in source]\n",
    "x_data[:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ab1f155b-a3d8-410c-a7f6-f95d3adfa7b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# x_data.extend(questions[0:])\n",
    "# y_data.extend(labels[0:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "065f5987-9bc5-48be-b8d5-7b245ec5a9b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "106\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "106"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len(x_data))\n",
    "len(y_data)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "d4b08d40-a7db-45b5-8a7e-e487e41c4fbd",
   "metadata": {},
   "source": [
    "# text cleaning\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ba5074be-e0ba-4add-a444-bd0dc9e99112",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_tokenized=[]\n",
    "en_stopwords=stopwords.words('english')\n",
    "punctuation=string.punctuation\n",
    "for question in x_data:\n",
    "    tokenized=word_tokenize(question)\n",
    "    clearTxt=[]\n",
    "    for word in tokenized:\n",
    "        word=word.lower()\n",
    "        if (word not in en_stopwords ) and (word not in punctuation):\n",
    "                clearTxt.append(word)\n",
    "    x_tokenized.append(tokenized) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10
   "id": "b8dac81c-c271-4d03-a1bd-18af5c2d754d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[['What', 'is', 'the', 'capital', 'of', 'Egypt', '?'],\n",
       " ['How', 'many', 'players', 'in', 'Football', '(', 'soccer', ')', '?'],\n",
       " ['How', 'many', 'players', 'in', 'Volleyball', '?'],\n",
       " ['How', 'many', 'players', 'in', 'Basketball', '?'],\n",
       " ['How', 'many', 'players', 'in', 'Tennis', '?']]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_tokenized[:5]\n",
    "# punctuation"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "92b87189-00a3-41c5-a701-c6db4b8ae8d3",
   "metadata": {},
   "source": [
    "# lemmatization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b55ee6bd-ce16-4a45-8b6e-cfd20bb2a14d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['What', 'be', 'the', 'capital', 'of', 'Egypt', '?'], ['How', 'many', 'player', 'in', 'Football', '(', 'soccer', ')', '?'], ['How', 'many', 'player', 'in', 'Volleyball', '?'], ['How', 'many', 'player', 'in', 'Basketball', '?'], ['How', 'many', 'player', 'in', 'Tennis', '?'], ['What', 'be', 'the', 'Police', 'number', 'in', 'Egypt', '?'], ['What', 'be', 'the', 'number', 'of', 'Tourist', 'Police', 'in', 'Egypt', '?'], ['What', 'be', 'the', 'Natural', 'Gas', 'Emergency', 'number', 'in', 'Egypt', '?'], ['What', 'be', 'the', 'number', 'of', 'Traffic', 'Police', 'in', 'Egypt', '?'], ['How', 'many', 'bone', 'be', 'there', 'in', 'the', 'adult', 'body', '?']]\n"
     ]
    }
   ],
   "source": [
    "lemmatizer = WordNetLemmatizer()\n",
    "x_lemmetized=[]\n",
    "for i in range(len(x_tokenized)):\n",
    "        tokens = x_tokenized[i]\n",
    "        pos_tags = nltk.pos_tag(tokens)\n",
    "        lemmas = []\n",
    "        # print(pos_tags)\n",
    "        for k in range(len(pos_tags)):\n",
    "            tag = pos_tags[k][1][0].lower() if pos_tags[k][1][0].lower() in ['a', 'n', 'v'] else 'n'\n",
    "            lemmas.append(lemmatizer.lemmatize(pos_tags[k][0], tag))\n",
    "        x_lemmetized.append ( lemmas)\n",
    "print(x_lemmetized[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d7415da-095e-4d1a-a9be-442245ec29e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_lemmetized_arr=[]\n",
    "tokenizer = Tokenizer(num_words=1000)\n",
    "tokenizer.fit_on_texts([' '.join (w)for w in x_lemmetized])\n",
    "x_lemmetized_arr = tokenizer.texts_to_sequences([' '.join (w)for w in x_lemmetized])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3070f662-b848-4103-b50a-1acc0d8856ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# [' '.join (w)for w in x_lemmetized]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7105b28-9639-423c-b601-5c2fd5e49b91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[2, 1, 3, 54, 5, 17],\n",
       " [11, 18, 22, 8, 55, 56],\n",
       " [11, 18, 22, 8, 57],\n",
       " [11, 18, 22, 8, 58],\n",
       " [11, 18, 22, 8, 59]]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_lemmetized_arr[:5]\n",
    "# x_tokenized_arr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a9319f6-ff3f-40f5-bfde-db4e2f64679b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save the tokenizer as a file\n",
    "with open('tokenizer.pkl', 'wb') as f:\n",
    "    pickle.dump(tokenizer, f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fea4879-21df-4c8d-9022-95a4037a42fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Load the tokenizer from a file\n",
    "# with open('tokenizer.pkl', 'rb') as f:\n",
    "#     tokenizer = pickle.load(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c25c7c43-65ca-4f72-bda4-612e0301f2fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "label_encoder=LabelEncoder()\n",
    "y_data_label=label_encoder.fit_transform(y_data)\n",
    "y_data_label\n",
    "y_data_label=to_categorical(y_data_label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8aba397",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       ...,\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.],\n",
       "       [0., 0., 0., ..., 0., 0., 0.]], dtype=float32)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_data_label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6b1c0a9-2d41-4fc9-ae6b-331f366fa199",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "106\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "106"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len(x_lemmetized_arr))\n",
    "len(y_data_label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ff69c37-0ab4-42d7-a318-339c55c33d5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_pad_sequences = pad_sequences(x_lemmetized_arr, maxlen=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8178ee79-0ac5-4598-ab91-ee59512bce15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11, 18, 22,\n",
       "        8, 55, 56])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_pad_sequences[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9fd5cdde-7006-4d47-b80a-1814e1815388",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'x_pad_sequences' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;28mlen\u001b[39m(\u001b[43mx_pad_sequences\u001b[49m))\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28mlen\u001b[39m(y_data_label)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'x_pad_sequences' is not defined"
     ]
    }
   ],
   "source": [
    "print(len(x_pad_sequences))\n",
    "len(y_data_label)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "a430d24f-3b4d-47fa-a14e-191cc38720a2",
   "metadata": {},
   "source": [
    "# Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0974473-72ef-4ad5-9998-33ada1e4b82f",
   "metadata": {},
   "outputs": [],
   "source": [
    "kerasModel = keras.models.Sequential([\n",
    "\n",
    "        keras.layers.Embedding(input_dim=1000, output_dim=32,input_length=20),\n",
    "          # keras.layers.LSTM(units=64),\n",
    "    keras.layers.Flatten(),     \n",
    "    keras.layers.Dense(units=64, activation='relu'),\n",
    "        # keras.layers.Dropout(.5),\n",
    "        keras.layers.Dense(units=32, activation='relu'),     \n",
    "        keras.layers.Dense(units=16, activation='relu'),    \n",
    "\n",
    "        # keras.layers.Dense(3636,activation='softmax') ,        \n",
    "    keras.layers.Dense(102,activation='softmax') ,        \n",
    "        ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "636a438e-4cf4-48dd-b1ba-c1fc5a4152fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "kerasModel.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])\n",
    "# model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f86488de-e290-45c2-94c7-3ee86e258d8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "106\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "106"
      ]
     },
     "execution_count": 1417,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len(x_lemmetized_arr))\n",
    "len(y_data_label)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74bc88d2-d556-4dab-8b0a-92b1f9010250",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/20\n",
      "4/4 [==============================] - 1s 2ms/step - loss: 4.6264 - accuracy: 0.0000e+00\n",
      "Epoch 2/20\n",
      "4/4 [==============================] - 0s 3ms/step - loss: 4.6226 - accuracy: 0.0094\n",
      "Epoch 3/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.6199 - accuracy: 0.0189\n",
      "Epoch 4/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.6169 - accuracy: 0.0377\n",
      "Epoch 5/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.6128 - accuracy: 0.0377\n",
      "Epoch 6/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.6071 - accuracy: 0.0472\n",
      "Epoch 7/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.6009 - accuracy: 0.0472\n",
      "Epoch 8/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5925 - accuracy: 0.0472\n",
      "Epoch 9/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5820 - accuracy: 0.0472\n",
      "Epoch 10/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5687 - accuracy: 0.0472\n",
      "Epoch 11/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5522 - accuracy: 0.0472\n",
      "Epoch 12/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5325 - accuracy: 0.0472\n",
      "Epoch 13/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.5035 - accuracy: 0.0472\n",
      "Epoch 14/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.4729 - accuracy: 0.0472\n",
      "Epoch 15/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.4338 - accuracy: 0.0472\n",
      "Epoch 16/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.3885 - accuracy: 0.0377\n",
      "Epoch 17/20\n",
      "4/4 [==============================] - 0s 3ms/step - loss: 4.3419 - accuracy: 0.0377\n",
      "Epoch 18/20\n",
      "4/4 [==============================] - 0s 3ms/step - loss: 4.2812 - accuracy: 0.0377\n",
      "Epoch 19/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.2218 - accuracy: 0.0377\n",
      "Epoch 20/20\n",
      "4/4 [==============================] - 0s 2ms/step - loss: 4.1607 - accuracy: 0.0660\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.callbacks.History at 0x2b38f813f90>"
      ]
     },
     "execution_count": 1418,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "kerasModel.fit(x_pad_sequences,y_data_label,epochs=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6c09800-85ff-4cf3-9521-db8bcd4fc4b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4/4 [==============================] - 0s 2ms/step - loss: 4.1026 - accuracy: 0.0660\n",
      "4.102565765380859\n",
      "0.06603773683309555\n"
     ]
    }
   ],
   "source": [
    "val_loss, val_acc = kerasModel.evaluate(x_pad_sequences, y_data_label)\n",
    "print(val_loss)\n",
    "print(val_acc)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "ca067982-f7d9-4a48-80f3-033ae49e5cff",
   "metadata": {},
   "source": [
    "# save model "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82c476be-cfc1-4ed2-b62e-f9f33a07a276",
   "metadata": {},
   "outputs": [],
   "source": [
    " # kerasModel.save('modelChatBot0.04-0.96.h5')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5715b923-308f-42e8-9182-cf0727097722",
   "metadata": {},
   "outputs": [],
   "source": [
    "model=load_model('modelChatBot0.04-0.96.h5')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27ea1bd2-9cbe-48f9-a0a8-91b4e69fc582",
   "metadata": {},
   "outputs": [],
   "source": [
    "# modelConverter=tf.lite.TFLiteConverter.from_keras_model(model)\n",
    "# tfmodel=modelConverter.convert()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "491775fd-6320-4de2-9461-2fbbed32df44",
   "metadata": {},
   "outputs": [],
   "source": [
    "# with open('tfChatbotmodel0.04-0.96.tflite','wb') as modelFile:\n",
    "#     modelFile.write(tfmodel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccdfb67e-afbc-475b-81c7-7e18be062989",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model=kerasModel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eb59101-2a33-43e2-9b0c-1f2dad45bbfa",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'model' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m val_loss, val_acc \u001b[39m=\u001b[39m model\u001b[39m.\u001b[39mevaluate(x_pad_sequences, y_data_label)\n\u001b[0;32m      2\u001b[0m \u001b[39mprint\u001b[39m(val_loss)\n\u001b[0;32m      3\u001b[0m \u001b[39mprint\u001b[39m(val_acc)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'model' is not defined"
     ]
    }
   ],
   "source": [
    "val_loss, val_acc = model.evaluate(x_pad_sequences, y_data_label)\n",
    "print(val_loss)\n",
    "print(val_acc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86206bc0-deae-4644-8b70-aaee2f55d0d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1/1 [==============================] - 0s 81ms/step\n",
      "YOU: hi\n",
      "Chatbot: Hello\n",
      "\n",
      "1/1 [==============================] - 0s 19ms/step\n",
      "YOU: What is the currency of France\n",
      "Chatbot: Euro (EUR)\n",
      "\n",
      "1/1 [==============================] - 0s 18ms/step\n",
      "YOU: What is the capital of Egypt\n",
      "Chatbot: Cairo\n",
      "\n",
      "1/1 [==============================] - 0s 24ms/step\n",
      "YOU: 'Can you tell me a story\n",
      "Chatbot: Sure, what kind of story would you like to hear?\n",
      "\n",
      "1/1 [==============================] - 0s 27ms/step\n",
      "YOU: Can you tell me a story\n",
      "Chatbot: Sure, what kind of story would you like to hear?\n",
      "\n",
      "1/1 [==============================] - 0s 20ms/step\n",
      "YOU: What is your favorite food\n",
      "Chatbot: I don't have the ability to eat or taste food, so I don't have a favorite food.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def preprocess_input(input_text):\n",
    "    input_text = input_text.lower()\n",
    "    input_text = nltk.word_tokenize(input_text)\n",
    "    input_text = [lemmatizer.lemmatize(word) for word in input_text]\n",
    "    input_text = tokenizer.texts_to_sequences([input_text])\n",
    "    input_text = tf.keras.preprocessing.sequence.pad_sequences(input_text, maxlen=20)\n",
    "    return input_text\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "while True:\n",
    "    # for x in x_data:\n",
    "    user_input = input(\"You: \")\n",
    "    # user_input=x\n",
    "    preprocessed_input = preprocess_input(user_input)\n",
    "    prediction = model.predict(preprocessed_input)\n",
    "    predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])\n",
    "\n",
    "\n",
    "    print(\"YOU: \" + user_input )\n",
    "    # print(predicted_label[0])\n",
    "    print(\"Chatbot: \" + predicted_label[0])\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24d2d05c-3d23-4f21-b727-55ea656e3c64",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0e797b3-4039-4281-bd28-cc3b22a6e031",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
