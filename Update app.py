# PDFGPT
#### Video Demo:  <https://youtu.be/-p2tEfgyBEw>
#### Description:
This code creats a Generative pre-trained transformer, that can parse through pdf files and answeruser prompts about the pdf files

### Requirements
PyPDF2
langchain
elasticsearch
pinecone-client
weaviate-client
faiss-cpu
openai
numpy
numpy

### Functions

# Autentication Functions

At the moment the authentication is only limited to a dictionary that has two users. At a future time the autentication function will be connected  to a live database to validate current users and let new users sign up.

# read_pdf
This function iterates through the given pages and returns a list of texts in all the pages of the pdf

# split_text
The split_text function splits the text into smaller chuncks that can be passed to the aimodel function(see below). A new line "\n" character is used to separate text. The model allows for small overlapping  to improve accuray

# aimodel

The aimodel is user to produces answers to the questions users ask about the pdf file they upload. We use OpenAIs embeddings to convert the string text to numbers that the aimodel can process. We use FAISS docsearch function to find specific emeddings/data that is relvan to the search query. Finally we build a question and answer Machine learning piple line with Langchain and pass the OpenAI langauge model into the piple line to process qurey

#gr Interface and main function
The gr Interface provides us with the UI to interact with the user. Th UI has three input dialog boxes. A dialog box where a user can enter pdf files from their devices. A question dialog box where a user can type their question and an OpenAI dialog box where a user can enter their api key. It is import that a user fills in each dialog box in order to submit a query. If a user inputs an invalid file an error will be thrown. The PDF2 module used in the code is outdated and dependencies have been dropped so it is difficult to check for that specific error but a general exception is raised. If the api key is invalid an exception is also raised. There is one output dialog that outputs the aimodels answers.

## Contributing

Feel free to fork the repository to make it more interactive or expand its capabilities by incorporating audio files, images etc. Alsoa a better interface in a flask or django interface to allow more funcationality

## License
MIT License
