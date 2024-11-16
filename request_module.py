{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a9e3a620",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n",
      "200\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "x = requests.get(\"https://github.com/\")\n",
    "print(x)\n",
    "print(x.status_code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "787d2fa2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<Response [200]>\n",
      "200\n",
      "Following:  1\n",
      "Followers:  560\n"
     ]
    }
   ],
   "source": [
    "import requests \n",
    "res = requests.get(\"https://api.github.com/users/sana-rasheed\")\n",
    "print(res)\n",
    "print(res.status_code)\n",
    "data = res.json()\n",
    "print(\"Following: \", data['following'])\n",
    "print(\"Followers: \", data['followers'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7febb394",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "url = 'https://official-joke-api.appspot.com/jokes/programming/random'\n",
    "res = requests.get(url)\n",
    "data = res.json()[0]\n",
    "for key in data:\n",
    "    print(key, \":\", data[key])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
