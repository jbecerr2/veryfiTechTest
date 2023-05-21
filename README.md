# Veryfi Technical test for Data Acquisiton Specialist

This project consist in a program that process documents from a directory using the veryfi API, extract specific information from them and saves it in a JSON file.

## Dependencies & Requirements

- Python version: 3.x
- veryfi-python library (`pip install veryfi-python`)
- python-env library (`pip install python-dotenv`)

### Important information regarding the veryfi API

For this program to work properly, is necesary to create an .env file containing your veryfi API credentials, the file should be as follows:

```
VERYFI_CLIENT_ID="your_client_id"
VERYFI_CLIENT_SECRET="your_client_secret"
VERYFI_USERNAME="your_username"
VERYFI_API_KEY="your_api_key"
```

Is important that the file is named: envfile.env (I'll modify this later, but for now use this exact name)

You can obtain this credentials creating an OCR API account in [veryfi] (https://app.veryfi.com)

Make sure the env file is located outside the source directory.

## Usage

- Save the documents needed to process in the `docs/`directory
- Run the `main.py`script located in the `source/` directory, to process the documents and extract the information to a JSON file
- The ouput file will be located in the project directory, it will be called `output.json`

### Optional Configuration

- If you want to modify the location or the name of the documents directory, update the `directory_path` variable in `main.py` as follows:

```python
docs_directory = os.path.join(source_dir, "new/path/here", "newdirectoryname")
```

-If you want to change the output file name or location, update the `output_path` variable in `main.py` as follows:

```python
output_path = os.path.join(source_dir, "new/path/here", "newname.json")
```

## Additional information

In the begginning of the project, I used `docReader.py` as the only file of the project to 
learn better about how to use the API and finding a working solution as quickly as possible,
But of course, the code is not entirely following good coding practices as it should be. So, after testing and studying this initial script, I decided to upgrade it into a better solution.

### Coding practices and paradigms

- #### Procedural and Functional Programming: 
In this project, I structured the code in separate modules, each one of them responsible for specific tasks using functions, for example, the `credentials.py` module focuses only on retrieving and validate the API credentials using the function: `load_veryfi_credentials()`. 
This makes the code easier to understand, reuse if necessary, test and maintain.

- #### Separation of Concerns: 
Each module has a clear responsibility and performs specific functions, for example, `doc_processor.py`module focuses on processing the documents using the veryfi API, and the `extract_json.py`focuses on the extraction and saving the data.

- #### Configuration Management: 
Since is common sense to NEVER write ANY credentials or secrets into the code itself, I decided to use an environment file, separated from the source code, to save securely the API credentials and secrets.
This helps to keep sensitive information a little bit more safe and easy to configure.

- #### Error handling: 
Here I decided to implement a little bit of error handling in `credentials.py` to validate the API credentials.

### Version Control:
In this case, I created 3 specific branches:
- main: main default branch, here I started the project and push the main completed and functional project up to date.
- dev: here in this branch, I focused on finding the solution to the test as quickly as I could.
- optimize: in this branch, I focused on optimizing and polishing the initial solution to a more approachable and understandable solution using good coding practices.









