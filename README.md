# taptap2
This is python app that helps users who type a lot with multple languages.
Before taptap, users have to switch keyboard layout and only then the can type in desired language.

Taptap changes the game. Now you just begin typing. If the text you just started typing is in wrong language, just tap caps lock twice. Taptap will:
 - remove all characters you typed after the last space
 - switch the language
 - simulate keyboard input of the deleted characters, now in the correct language

 If you have more than 2 languages installed, taptap again to switch to next language.

 Example:
 Imaging that you have 2 languages installed: English and Russian.
 You have typed:
 '''
 In russian, word hello is "ghbd
 '''

 So you mentioned "ghbd" and then you tap caps lock twice.
 Taptap removes "ghbd" and simulates keyboard input of the deleted characters, now in the correct language.

 So the text you see now is:
  '''
 In russian, word hello is "Прив
 '''

 As soon as you see that the text is in the correct language, you can continue typing.

 
 # technical details
 - pip for dependency management
 - uv for python version management
 - uv as pip replacement
 - no poetry
 - pynput for global keyboard listening
 - strive to high test coverage
 - macos first

