{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "# participants.py\n",
    "#   A simple python program to print the participants from the class.\n",
    "#   Intended as an example of updating code on GitHub.\n",
    "\n",
    "def main():\n",
    "    numPeople = 13 # number of students + instructor\n",
    "    \n",
    "    # Add your name to the list below to the right of any other names.  \n",
    "    # I have added my name plus a placeholder for your name. Replace the placeholder with your name.\n",
    "    # The last person to push the file to the repository should ensure the <your name here> placeholder is removed.\n",
    "    \n",
    "    people = [\"Christopher Harris\", \"<your name here>\"]\n",
    "    \n",
    "    # don't change anything below this line\n",
    "    \n",
    "    for i in range(len(people)):\n",
    "        print(\"{0:2d}. {1}\".format(i+1, people[i]))   \n",
    "    print(\"\\nNumber of People: %2d\" %(i+1))\n",
    "    print(\"Percentage of People: {:.1%}\".format((i+1)/numPeople))\n",
    "    \n",
    "if __name__ == '__main __': main() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1. Christopher Harris\n",
      " 2. <your name here>\n",
      "\n",
      "Number of People:  2\n",
      "Percentage of People: 15.4%\n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
