# French-English-Flashcard-App
<h2>This is a Tkinter-based GUI application that helps users learn French vocabulary through flashcards. <br>
  Each flashcard displays a French word, and after a short delay (3 seconds), it flips to show the English translation.</h2><br>
<h3>File/Folder Structure:</h3>
<p>
📁 Flashcard App/<br>
├── main.py (your main script)<br>
├── 📁 Data/<br>
│   ├── french_words.csv<br>
│   └── words_to_learn.csv (auto-generated)<br>
├── 📁 Images/<br>
│   ├── card_front.png<br>
│   ├── card_back.png<br>
│   ├── right.png<br>
│   └── wrong.png<br>
</p>
<h3>Modules Used:</h3>
<ul>
  <li><b>tkinter :</b>	Python’s built-in GUI toolkit used to create the app’s interface.</li>
  <li><b>pandas :</b>	Handles CSV file reading/writing and data manipulation.</li>
  <li><b>random :</b>	Used to randomly choose a new word from the list.</li>
</ul>
<h3>How to Run:</h3>
<ol>
  <li>Make sure the folder contains:
    <ul>
      <li>main.py</li>
      <li>Data/french_words.csv</li>
      <li>Images/ with required PNG images</li>
    </ul>
  </li>
  <li>Install required library:
    <p>pip install pandas</p>
  </li>
  <li>Run the script:
    <p></p>
  </li>python main.py
</ol>
