# Environment

- python 2.7
- flask

# Install

```
$ pip install -r requirements.txt

$ FLASK_APP=app.py flask run
```

# Example

```
curl --request POST \
			 --url http://localhost:5000/summary \
			 --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
			 --form 'content=Automatic summarization is the process of reducing a text document with acomputer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another.'
```

# Response
```
{
	"keywords": [
		"document",
		"summarization",
		"writing",
		"summary"
	],
	"summary": [
		"Automatic summarization is the process of reducing a text document with acomputer program in order to create a summary that retains the most important points of the original document."
	]
}
```

